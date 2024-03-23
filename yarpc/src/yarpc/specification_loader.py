import yaml
import sys
import json
import re
from itertools import chain
from pathlib import Path
from jsonschema import Draft7Validator, RefResolver

def __load_yaml(filename: Path, validator: Draft7Validator) -> dict:
    """Loads content from a yaml file and checks it using a jsonschema
    validator.

    Args:
        filename (Path): The filename of the yaml file to load
        validator (Draft7Validator): The jsonschema validator

    Returns:
        dict: The parsed and validated yaml content
    """
    parsed = {}
    with open(filename, "r") as f:
        parsed = yaml.safe_load(f)

    is_valid = True
    for error in validator.iter_errors(parsed):
        print("="*50, file=sys.stderr)
        print(error, file=sys.stderr)
        for context in error.context:
            print("-*50", file=sys.stderr)
            print(context, file=sys.stderr)
        print("="*50, file=sys.stderr)
        is_valid = False

    if not is_valid:
        raise RuntimeError("Spec invalid!")

    for obj in parsed.get('objects', []):
        obj['specName'] = filename.stem
        obj['specPath'] = str(filename.absolute().resolve())
        obj['regex'] = f"^{obj['regex' if 'regex' in obj else 'name']}$"
    return parsed

def __get_schema_validator() -> Draft7Validator:
    """Initializes and returns the jsonschema validator

    Returns:
        Draft7Validator: the validator
    """
    schema = {}
    schema_dir =f"{Path(__file__).parent}/schema"
    with open(f"{schema_dir}/root.schema.json", "r") as f:
        schema = json.load(f)
    return Draft7Validator(
        schema=schema,
        resolver=RefResolver(
            base_uri=f"file://{schema_dir}/",
            referrer=schema,
        )
    )

def __get_builtins() -> dict:
    """Returns builtin objects

    Returns:
        dict: builtin objects
    """
    return {
        "objects": [
            {
                "name": "uint8",
                "kind": "builtin",
                "dbus": "y",
                "py": "int",
            },
            {
                "name": "bool",
                "kind": "builtin",
                "dbus": "b",
                "py": "bool",
            },
            {
                "name": "int16",
                "kind": "builtin",
                "dbus": "n",
                "py": "int",
            },
            {
                "name": "uint16",
                "kind": "builtin",
                "dbus": "q",
                "py": "int",
            },
            {
                "name": "int32",
                "kind": "builtin",
                "dbus": "i",
                "py": "int",
            },
            {
                "name": "uint32",
                "kind": "builtin",
                "dbus": "u",
                "py": "int",
            },
            {
                "name": "int64",
                "kind": "builtin",
                "dbus": "x",
                "py": "int",
            },
            {
                "name": "uint64",
                "kind": "builtin",
                "dbus": "t",
                "py": "int",
            },
            {
                "name": "double",
                "kind": "builtin",
                "dbus": "d",
                "py": "float",
            },
            {
                "name": "string",
                "kind": "builtin",
                "dbus": "s",
                "py": "str",
            },
            {
                "name": "array",
                "kind": "builtin",
                "regex": "array<(.*)>",
                "dbus": "a$1",
                "py": "Sequence[$1]",
            },
            {
                "name": "dict",
                "kind": "builtin",
                "regex": "dict<(.*?), *(.*)>",
                "dbus": "a{$1$2}",
                "py": "Mapping[$1, $2]",
            },
        ]
    }

def load_specifications(spec_dir: str) -> list:
    """Loads and verifies specifications from yaml files in spec_dir and
    adds builtin objects.

    Args:
        spec_dir (str): The directory to look for specs in

    Returns:
        list: The list of loaded objects
    """
    validator = __get_schema_validator()
    specifications = [__get_builtins()]
    for filename in chain(Path(spec_dir).glob("**/*.yml"), Path(spec_dir).glob("**/*.yaml")):
        specifications.append(__load_yaml(filename, validator))
    return specifications
