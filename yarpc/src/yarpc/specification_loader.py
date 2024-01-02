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
        print("="*50)
        print(error)
        for context in error.context:
            print("-*50")
            print(context)
        print("="*50)
        is_valid = False

    if not is_valid:
        sys.exit(1)
    
    parsed['name'] = filename.stem
    parsed['path'] = str(filename.absolute().resolve())
    for obj in parsed.get('objects', []):
        obj['parent'] = parsed
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

def load_specifications(spec_dir: str):

    validator = __get_schema_validator()
    specifications = []
    for filename in chain(Path(spec_dir).glob("*.yml"), Path(spec_dir).glob("*.yaml")):
        specifications.append(__load_yaml(filename, validator))
    return specifications
