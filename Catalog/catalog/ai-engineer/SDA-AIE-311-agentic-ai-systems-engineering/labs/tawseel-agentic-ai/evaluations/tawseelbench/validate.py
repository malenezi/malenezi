"""TawseelBench — a tiny stdlib JSON Schema validator.

`jsonschema` is not installable in this build sandbox (SPEC §1), and
TawseelBench's own verification obligation (SPEC §8) requires every
scenario to validate against `schema.json`. This module implements just
enough of draft-07 to check `schema.json`: `type` (incl. lists of types),
`required`, `properties`, `additionalProperties: false`, `items`, `enum`,
`minLength`, `minItems`, `pattern`. That is the full vocabulary
`schema.json` uses — this is not a general-purpose validator and does not
try to be one.
"""
from __future__ import annotations

import re
from typing import Any

_TYPE_MAP: dict[str, type | tuple[type, ...]] = {
    "object": dict,
    "array": list,
    "string": str,
    "number": (int, float),
    "boolean": bool,
    "null": type(None),
}


def _check_type(value: Any, type_spec: str | list[str], path: str, errors: list[str]) -> bool:
    types = type_spec if isinstance(type_spec, list) else [type_spec]
    py_types = tuple(_TYPE_MAP[t] if not isinstance(_TYPE_MAP[t], tuple) else _TYPE_MAP[t] for t in types)
    flat: list[type] = []
    for t in py_types:
        flat.extend(t if isinstance(t, tuple) else (t,))
    # bool is a subclass of int in Python -- only accept bool for boolean type explicitly
    if isinstance(value, bool) and bool not in flat:
        errors.append(f"{path}: expected type {type_spec}, got boolean")
        return False
    if not isinstance(value, tuple(flat)):
        errors.append(f"{path}: expected type {type_spec}, got {type(value).__name__}")
        return False
    return True


def _validate(instance: Any, schema: dict[str, Any], path: str, errors: list[str]) -> None:
    if "type" in schema:
        if not _check_type(instance, schema["type"], path, errors):
            return

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} not in enum {schema['enum']}")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: string shorter than minLength {schema['minLength']}")
        if "pattern" in schema and instance is not None and not re.match(schema["pattern"], instance):
            errors.append(f"{path}: {instance!r} does not match pattern {schema['pattern']!r}")

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(instance) - set(properties)
            if extra:
                errors.append(f"{path}: unexpected additional propert(y/ies) {sorted(extra)}")
        for key, sub_schema in properties.items():
            if key in instance:
                _validate(instance[key], sub_schema, f"{path}.{key}", errors)

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: array shorter than minItems {schema['minItems']}")
        if "items" in schema:
            for idx, item in enumerate(instance):
                _validate(item, schema["items"], f"{path}[{idx}]", errors)


def validate_scenario(instance: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    """Return a list of human-readable error strings (empty list == valid)."""
    errors: list[str] = []
    _validate(instance, schema, "$", errors)
    return errors
