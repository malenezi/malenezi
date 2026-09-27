"""Run a Spark SQL query against the Masar lakehouse.

Delta paths work directly::

    SELECT * FROM delta.`./lakehouse/silver/trips` LIMIT 5

as do catalog names (``silver.trips``) once the tables are registered.

CLI::

    python -m masar.tools.sql --query "DESCRIBE HISTORY delta.\\`./lakehouse/silver/trips\\`"
    python -m masar.tools.sql --file serving/queries/exec_demand_dashboard.sql
"""

from __future__ import annotations

import argparse
import sys

from masar.spark import get_spark


def run_sql(query: str, limit: int = 50, truncate: bool = False) -> None:
    """Execute one statement and show the result.

    Statements that return no rows (OPTIMIZE, VACUUM, ALTER) still print their
    summary row — which for OPTIMIZE is the metrics you need for LAB4_NOTES.md.
    """
    spark = get_spark("tools-sql")
    df = spark.sql(query)
    df.show(limit, truncate=truncate)


def main() -> None:
    """CLI entry point."""
    p = argparse.ArgumentParser(description="Run Spark SQL against the Masar lakehouse")
    p.add_argument("--query", help="SQL text; use - to read stdin")
    p.add_argument("--file", help="path to a .sql file (statements split on ';')")
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--truncate", action="store_true")
    a = p.parse_args()

    if a.file:
        with open(a.file) as fh:
            body = fh.read()
        statements = [
            s.strip() for s in body.split(";") if s.strip() and not s.strip().startswith("--")
        ]
        for statement in statements:
            print(f"\n-- {statement.splitlines()[0][:100]}")
            run_sql(statement, a.limit, a.truncate)
        return

    query = sys.stdin.read() if a.query == "-" else a.query
    if not query:
        p.error("give --query or --file")
    run_sql(query, a.limit, a.truncate)


if __name__ == "__main__":
    main()
