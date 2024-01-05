import yaml
import sys
import json
import re
from itertools import chain
from pathlib import Path
from jsonschema import Draft7Validator, RefResolver

def __load_yaml(filename: Path, validator: Draft7Validator):
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
        obj['regex'] = re.compile('^' + obj['regex' if 'regex' in obj else 'name'] + '$')
    return parsed

def __get_schema_validator():
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

def __get_builtins():
    return {
        "objects": [
            {
                "name": "uint8",
                "kind": "builtin",
                "dbus": "y",
                "py": "int"
            },
            {
                "name": "bool",
                "kind": "builtin",
                "dbus": "b",
                "py": "bool"
            },
            {
                "name": "int16",
                "kind": "builtin",
                "dbus": "n",
                "py": "int"
            },
            {
                "name": "uint16",
                "kind": "builtin",
                "dbus": "q",
                "py": "int"
            },            
            {
                "name": "int32",
                "kind": "builtin",
                "dbus": "i",
                "py": "int"
            },
            {
                "name": "uint32",
                "kind": "builtin",
                "dbus": "u",
                "py": "int"
            },
            {
                "name": "int64",
                "kind": "builtin",
                "dbus": "x",
                "py": "int"
            },
            {
                "name": "uint64",
                "kind": "builtin",
                "dbus": "t",
                "py": "int"
            },
            {
                "name": "double",
                "kind": "builtin",
                "dbus": "d",
                "py": "float"
            },
            {
                "name": "string",
                "kind": "builtin",
                "dbus": "s",
                "py": "str"
            },
        ]
    }

def load_specifications(spec_dir: str):

    validator = __get_schema_validator()
    specifications = [__get_builtins()]
    for filename in chain(Path(spec_dir).glob("*.yml"), Path(spec_dir).glob("*.yaml")):
        specifications.append(__load_yaml(filename, validator))
    return specifications
