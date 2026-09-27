#!/usr/bin/env python3
"""Masar Lakehouse environment doctor — the single source of truth for setup.

    make doctor
    python scripts/doctor.py
    python scripts/doctor.py --check spark --check delta --check kafka --check redis

Every check answers one question and, when it fails, names the fix. A red line
here on Day 1 costs the capstone on Day 5, because every lab writes into the
same working tree: a broken JAVA_HOME on Monday is a missing feature table on
Friday.

Design rules this file follows, because a doctor that crashes is worse than no
doctor at all:

  * **Never crash.** A missing service, an absent package, an unreadable
    directory — each becomes a red row with a fix, never a traceback.
  * **No project imports at module scope.** ``import masar`` is itself one of
    the things being checked, so it happens inside a check, guarded.
  * **Stdlib only.** The doctor must work in the environment it is diagnosing.
  * **Exit non-zero on any [fail].** Warnings (Kafka/Redis before Day 4) do
    not fail the run; missing Java does.
"""

from __future__ import annotations

import argparse
import importlib
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

OK, WARN, FAIL = "ok", "warn", "fail"
GLYPH = {OK: "✓", WARN: "!", FAIL: "✗"}

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PYTHON = (3, 11)
REQUIRED_JAVA = 17
PINS = {
    "pyspark": "3.5",
    "delta-spark": "3.2",
    "dbt-core": "1.7",
    "dbt-spark": "1.7",
    "great_expectations": "0.18",
}


@dataclass
class Result:
    """One row of the doctor's report."""

    name: str
    status: str
    detail: str = ""
    fix: str = ""

    def render(self, width: int = 20) -> str:
        """Render as ``✓ [ok]   name   detail`` plus an indented fix when red."""
        head = f"{GLYPH[self.status]} [{self.status}]".ljust(11)
        line = f"{head}{self.name.ljust(width)}{self.detail}"
        if self.status in (WARN, FAIL) and self.fix:
            line += f"\n{' ' * 11}-> {self.fix}"
        return line


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def _version_of(module_name: str) -> str | None:
    """Installed version of a distribution, or ``None`` if it is absent."""
    from importlib import metadata

    try:
        return metadata.version(module_name)
    except Exception:
        try:
            module = importlib.import_module(module_name.replace("-", "_"))
            return getattr(module, "__version__", None)
        except Exception:
            return None


def _matches(version: str | None, pin: str) -> bool:
    """True when ``version`` starts with the pinned ``major.minor``."""
    return bool(version) and version.split("+")[0].startswith(pin)


def _run(cmd: list[str], timeout: int = 20) -> tuple[int, str]:
    """Run a command, returning ``(returncode, combined output)``.

    A missing binary returns ``(127, "")`` rather than raising, so a machine
    without Docker produces a warning row instead of a stack trace.
    """
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        return proc.returncode, (proc.stdout + proc.stderr).strip()
    except FileNotFoundError:
        return 127, ""
    except subprocess.TimeoutExpired:
        return 124, "timed out"
    except Exception as exc:  # noqa: BLE001 - the doctor never crashes
        return 1, str(exc)


def _port_open(host: str, port: int, timeout: float = 2.0) -> bool:
    """True when a TCP connection to ``host:port`` succeeds."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _pkg_row(name: str, pin: str, *, required: bool = True) -> Result:
    """Standard row for a pinned Python package."""
    version = _version_of(name)
    if version is None:
        status = FAIL if required else WARN
        return Result(
            name,
            status,
            "not installed",
            f"pip install -r requirements.txt  (pins {name}=={pin}.*)",
        )
    if not _matches(version, pin):
        return Result(
            name,
            FAIL,
            f"{version}  (required {pin}.x)",
            f"pip install '{name}=={pin}.*'  — do not 'upgrade to latest'",
        )
    return Result(name, OK, version)


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------


def check_python() -> Result:
    """Python must be 3.11.x: PySpark 3.5 wheels and dbt 1.7 are validated there."""
    v = sys.version_info
    detail = f"{v.major}.{v.minor}.{v.micro}"
    if (v.major, v.minor) != REQUIRED_PYTHON:
        return Result(
            "python",
            FAIL,
            f"{detail}  (required 3.11.x)",
            "install python3.11 and recreate .venv; see LAB_00 §1",
        )
    return Result("python", OK, f"{detail}            (required 3.11.x)")


def check_java() -> Result:
    """Spark 3.5 runs on Java 8/11/17. Java 21+ raises module-access errors."""
    code, out = _run(["java", "-version"])
    if code == 127:
        return Result(
            "java",
            FAIL,
            "not found on PATH",
            "install Temurin 17 (JDK, not JRE) and export JAVA_HOME; LAB_00 §2",
        )
    # `java -version` writes to stderr, and a wrapper (JAVA_TOOL_OPTIONS, a
    # proxy shim) may prepend its own lines — so parse the whole output, never
    # just the first line.
    match = re.search(r'version "(\d+)(?:[.\d_]*)"', out)
    if not match:
        first = out.splitlines()[0] if out else "unknown version"
        return Result(
            "java", WARN, first, "could not parse the version; confirm `java -version` reports 17.x"
        )
    major = int(match.group(1))
    version = match.group(0).split('"')[1]
    if major != REQUIRED_JAVA:
        return Result(
            "java",
            FAIL,
            f"{version}  (required {REQUIRED_JAVA}.x)",
            "install Temurin 17 and put $JAVA_HOME/bin first on PATH; LAB_00 §2",
        )
    return Result("java", OK, f"{version}")


def check_java_home() -> Result:
    """JAVA_HOME must point at a JDK 17 directory that actually exists."""
    java_home = os.environ.get("JAVA_HOME", "").strip()
    if not java_home:
        return Result(
            "JAVA_HOME",
            WARN,
            "not set",
            "export JAVA_HOME=$(/usr/libexec/java_home -v 17)  (macOS) or "
            "/usr/lib/jvm/java-17-openjdk-amd64 (Linux)",
        )
    if not Path(java_home).is_dir():
        return Result(
            "JAVA_HOME",
            FAIL,
            f"{java_home}  (directory does not exist)",
            "point JAVA_HOME at a real JDK 17 install",
        )

    # JAVA_HOME set is not the same as JAVA_HOME correct. Ask the JDK it points
    # at what version it is — a stale JAVA_HOME beside a different `java` on
    # PATH is the most confusing failure in this whole setup.
    java_bin = Path(java_home) / "bin" / "java"
    if java_bin.is_file():
        code, out = _run([str(java_bin), "-version"])
        match = re.search(r'version "(\d+)(?:[.\d_]*)"', out)
        if match and int(match.group(1)) != REQUIRED_JAVA:
            return Result(
                "JAVA_HOME",
                FAIL,
                f"{java_home}  (points at Java {match.group(1)}, required {REQUIRED_JAVA})",
                "export JAVA_HOME at a JDK 17 install; see LAB_00 §2",
            )
    else:
        return Result(
            "JAVA_HOME",
            WARN,
            f"{java_home}  (no bin/java inside — is it a JDK?)",
            "JAVA_HOME must point at a JDK root, not at bin/ and not at a JRE",
        )
    return Result("JAVA_HOME", OK, java_home)


def check_pyspark() -> Result:
    """PySpark 3.5.x — Delta 3.2 is compiled against Spark 3.5 only."""
    return _pkg_row("pyspark", PINS["pyspark"])


def check_delta() -> Result:
    """delta-spark 3.2.x — the transaction log, MERGE and time travel."""
    return _pkg_row("delta-spark", PINS["delta-spark"])


def check_spark_session() -> Result:
    """Start a real session and confirm the Delta extension is active.

    This is the check that catches "installed but misconfigured": both packages
    present, session built without ``spark.sql.extensions``, and every Delta
    read failing with a message that sounds like a missing dependency.
    """
    if _version_of("pyspark") is None:
        return Result(
            "spark session",
            WARN,
            "skipped (pyspark not installed)",
            "pip install -r requirements.txt",
        )
    import time

    try:
        sys.path.insert(0, str(REPO_ROOT / "src"))
        from masar.spark import get_spark  # noqa: PLC0415

        t0 = time.time()
        spark = get_spark("doctor")
        extensions = spark.conf.get("spark.sql.extensions", "")
        elapsed = time.time() - t0
        if "DeltaSparkSessionExtension" not in extensions:
            return Result(
                "spark session",
                FAIL,
                f"started in {elapsed:.1f}s, Delta NOT active",
                "always build the session with masar.spark.get_spark()",
            )
        return Result("spark session", OK, f"started in {elapsed:.1f}s, delta extension active")
    except Exception as exc:  # noqa: BLE001
        return Result(
            "spark session",
            FAIL,
            f"{type(exc).__name__}: {str(exc)[:90]}",
            "check Java 17 and JAVA_HOME first; see LAB_00 §11",
        )


def check_delta_roundtrip() -> Result:
    """Write and read five rows through Delta — the end-to-end smoke test."""
    if _version_of("pyspark") is None or _version_of("delta-spark") is None:
        return Result(
            "delta write/read",
            WARN,
            "skipped (pyspark/delta-spark not installed)",
            "pip install -r requirements.txt",
        )
    try:
        sys.path.insert(0, str(REPO_ROOT / "src"))
        from masar.spark import get_spark  # noqa: PLC0415

        probe = str(Path(tempfile.gettempdir()) / "masar_delta_check")
        spark = get_spark("doctor")
        spark.range(5).write.format("delta").mode("overwrite").save(probe)
        n = spark.read.format("delta").load(probe).count()
        if n != 5:
            return Result(
                "delta write/read",
                FAIL,
                f"read back {n} rows, expected 5",
                "the Delta jars may be partially resolved; clear ~/.ivy2 and retry",
            )
        return Result("delta write/read", OK, f"5 rows round-tripped at {probe}")
    except Exception as exc:  # noqa: BLE001
        return Result(
            "delta write/read",
            FAIL,
            f"{type(exc).__name__}: {str(exc)[:90]}",
            "first run downloads the Delta jars — allow 1-2 minutes and retry",
        )


def check_dbt_core() -> Result:
    """dbt-core 1.7.x — the ELT framework for Labs 3 and 8."""
    return _pkg_row("dbt-core", PINS["dbt-core"])


def check_dbt_spark() -> Result:
    """dbt-spark 1.7.x with the `session` method, so no Thrift server is needed."""
    row = _pkg_row("dbt-spark", PINS["dbt-spark"])
    if row.status == OK:
        profiles = REPO_ROOT / "dbt" / "masar" / "profiles.yml"
        method = (
            "session" if profiles.is_file() and "method: session" in profiles.read_text() else "?"
        )
        row.detail = f"{row.detail}  (method={method})"
    return row


def check_great_expectations() -> Result:
    """Great Expectations 0.18.x — 1.x renamed the API the shipped suites use."""
    return _pkg_row("great_expectations", PINS["great_expectations"])


def check_docker() -> Result:
    """Docker + compose v2 run the Kafka and Redis stack (Days 4-5)."""
    code, out = _run(["docker", "--version"])
    if code == 127:
        return Result(
            "docker",
            WARN,
            "not installed",
            "install Docker Desktop or Colima; only required from Day 4",
        )
    if code != 0:
        return Result(
            "docker",
            WARN,
            "installed but not responding",
            "start Docker Desktop, or `colima start --cpu 4 --memory 8`",
        )
    version = out.replace("Docker version ", "").split(",")[0]
    ccode, cout = _run(["docker", "compose", "version"])
    compose = cout.split()[-1] if ccode == 0 and cout else "missing"
    return Result("docker", OK, f"{version}  (compose {compose})")


def check_kafka() -> Result:
    """The broker must accept a TCP connection on its advertised port."""
    host, _, port = os.environ.get("MASAR_KAFKA_BOOTSTRAP", "localhost:9092").partition(":")
    port = int(port or 9092)
    if _port_open(host, port):
        return Result("kafka broker", OK, f"{host}:{port} reachable")
    return Result(
        "kafka broker",
        WARN,
        f"{host}:{port} unreachable",
        "docker compose up -d kafka   (only required from Day 4)",
    )


def check_redis() -> Result:
    """Redis is the online feature store for Lab 8."""
    host = os.environ.get("MASAR_REDIS_HOST", "localhost")
    port = int(os.environ.get("MASAR_REDIS_PORT", "6379"))
    if not _port_open(host, port):
        return Result(
            "redis",
            WARN,
            f"{host}:{port} unreachable",
            "docker compose up -d redis   (only required from Day 5)",
        )
    if shutil.which("redis-cli"):
        code, out = _run(["redis-cli", "-h", host, "-p", str(port), "ping"], timeout=5)
        if code == 0 and "PONG" in out:
            return Result("redis", OK, f"{host}:{port} PONG")
    return Result("redis", OK, f"{host}:{port} reachable")


def check_masar_import() -> Result:
    """``import masar`` must work — every lab runs ``python -m masar.…``."""
    try:
        sys.path.insert(0, str(REPO_ROOT / "src"))
        masar = importlib.import_module("masar")
        return Result("masar package", OK, f"v{masar.__version__} importable")
    except Exception as exc:  # noqa: BLE001
        return Result(
            "masar package",
            FAIL,
            f"{type(exc).__name__}: {str(exc)[:80]}",
            "pip install -e .   (or export PYTHONPATH=$PWD/src)",
        )


def check_raw_data() -> Result:
    """The raw feeds must be present, with the expected trips row count."""
    raw = Path(os.environ.get("MASAR_RAW_ROOT", REPO_ROOT / "data" / "raw"))
    if not raw.is_dir():
        return Result(
            "data/raw",
            WARN,
            f"{raw} not found",
            "make data   (or point MASAR_RAW_ROOT at the course dataset)",
        )
    feeds = sorted({p.name.split("_")[0] for p in raw.glob("*.csv")})
    gps = list((raw / "gps").glob("gps_*.ndjson*")) if (raw / "gps").is_dir() else []
    if not feeds:
        return Result(
            "data/raw",
            WARN,
            "0 feeds present",
            "make data   (git lfs pull first if the repo uses LFS)",
        )
    trips = sorted(raw.glob("trips_*.csv"))
    detail = f"{len(feeds)} feeds, {len(gps)} gps files"
    if trips:
        with trips[0].open() as fh:
            rows = sum(1 for _ in fh) - 1
        detail += f", {trips[0].name} = {rows:,} rows"
    return Result("data/raw", OK, detail)


def check_lakehouse_dirs() -> Result:
    """bronze/, silver/ and gold/ must exist and be writable."""
    root = Path(os.environ.get("MASAR_LAKEHOUSE_ROOT", REPO_ROOT / "lakehouse"))
    try:
        for zone in ("bronze", "silver", "gold"):
            (root / zone).mkdir(parents=True, exist_ok=True)
        probe = root / ".doctor_write_probe"
        probe.write_text("ok")
        probe.unlink()
        return Result("lakehouse dirs", OK, f"bronze/ silver/ gold/ writable under {root}")
    except Exception as exc:  # noqa: BLE001
        return Result(
            "lakehouse dirs",
            FAIL,
            f"{type(exc).__name__}: {str(exc)[:70]}",
            f"check write permissions on {root}",
        )


CHECKS = {
    "python": check_python,
    "java": check_java,
    "java_home": check_java_home,
    "pyspark": check_pyspark,
    "delta": check_delta,
    "spark": check_spark_session,
    "delta_roundtrip": check_delta_roundtrip,
    "dbt": check_dbt_core,
    "dbt_spark": check_dbt_spark,
    "gx": check_great_expectations,
    "docker": check_docker,
    "kafka": check_kafka,
    "redis": check_redis,
    "masar": check_masar_import,
    "data": check_raw_data,
    "lakehouse": check_lakehouse_dirs,
}

#: Checks that are slow (they start a JVM). Skipped by --fast.
SLOW = {"spark", "delta_roundtrip"}


def main() -> int:
    """Run the selected checks and return the process exit code."""
    p = argparse.ArgumentParser(
        description="Masar Lakehouse environment doctor",
        epilog="Any [fail] must be fixed before Day 1. Kafka/Redis [warn] is fine until Day 4.",
    )
    p.add_argument(
        "--check",
        action="append",
        choices=sorted(CHECKS),
        default=None,
        help="run only this check (repeatable)",
    )
    p.add_argument("--fast", action="store_true", help="skip the checks that start a JVM")
    a = p.parse_args()

    selected = a.check or list(CHECKS)
    if a.fast:
        selected = [name for name in selected if name not in SLOW]

    print("Masar Lakehouse — environment doctor (scripts/doctor.py)")
    print("-" * 72)

    results: list[Result] = []
    for name in selected:
        try:
            result = CHECKS[name]()
        except Exception as exc:  # noqa: BLE001 - a check must never take the doctor down
            result = Result(
                name,
                FAIL,
                f"check crashed: {type(exc).__name__}: {exc}",
                "report this to the instructor; it is a bug in doctor.py",
            )
        results.append(result)
        print(result.render())

    n_ok = sum(1 for r in results if r.status == OK)
    n_warn = sum(1 for r in results if r.status == WARN)
    n_fail = sum(1 for r in results if r.status == FAIL)

    print("-" * 72)
    verdict = "you are ready for Day 1." if not n_fail else "fix the [fail] lines before Day 1."
    print(f"{n_ok} ok, {n_warn} warn, {n_fail} fail — {verdict}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
