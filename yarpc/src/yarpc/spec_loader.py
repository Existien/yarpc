import yaml
import sys
import json
from itertools import chain
from pathlib import Path
from jsonschema import Draft7Validator, RefResolver
from .languages import languages, DBusTypes


class SpecLoader:
    """Responsible for loading and verifying specifications from yaml files in spec_dir and
    adding builtin objects.
    """

    def load(self, spec_dir: str) -> list:
        """Loads and verifies specifications from yaml files in spec_dir and
        adds builtin objects.

        Args:
            spec_dir (str): The directory to look for specs in

        Returns:
            list: The list of loaded objects
        """
        validator = self._get_schema_validator()
        specifications = [self._get_builtins()]
        for filename in chain(Path(spec_dir).glob("**/*.yml"), Path(spec_dir).glob("**/*.yaml")):
            specifications.append(self._load_yaml(filename, validator))
        return specifications


    def _load_yaml(self, filename: Path, validator: Draft7Validator) -> dict:
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


    def _get_schema_validator(self) -> Draft7Validator:
        """Initializes and returns the jsonschema validator

        Returns:
            Draft7Validator: the validator
        """
        schema = {}
        base_dir =f"{Path(__file__).parent}/schema"
        with open(f"{base_dir}/root.schema.json", "r") as f:
            schema = json.load(f)
        outputs_schema = self._get_outputs_schema()
        schema["properties"]["outputs"] = outputs_schema
        return Draft7Validator(
            schema=schema,
            resolver=RefResolver(
                base_uri=f"file://{base_dir}/",
                referrer=schema,
            )
        )


    def _get_outputs_schema(self):
        outputs_schema = {
            "type": "array",
            "items": {
                "properties": {
                    "language": {
                        "type": "string"
                    }
                }
            }
        }
        outputs_schema["items"]["properties"]["language"]["enum"] = list(map(lambda x: x, languages().keys()))
        outputs_schema["items"]["allOf"] = list(map(
            lambda x: {
                "if": {
                    "properties": {
                        "language": {
                            "const": x
                        }
                    }
                },
                "then": {
                    "$ref": f"../languages/{x}/schema.json"
                }
            },
            languages().keys()
        ))
        return outputs_schema


    def _get_builtins(self) -> dict:
        """Returns builtin objects

        Returns:
            dict: builtin objects
        """
        language_types = {k: v.get_dbus_types() for k,v in languages().items()}
        language_types['dbus'] = DBusTypes(
            uint8='y',
            bool='b',
            int16='n',
            uint16='q',
            int32='i',
            uint32='u',
            int64='x',
            uint64='t',
            double='d',
            string='s',
            array='a$1',
            dict='a{$1$2}',
        )
        builtin_objects = [
            {
                "name": "uint8",
                "kind": "builtin",
            },
            {
                "name": "bool",
                "kind": "builtin",
            },
            {
                "name": "int16",
                "kind": "builtin",
            },
            {
                "name": "uint16",
                "kind": "builtin",
            },
            {
                "name": "int32",
                "kind": "builtin",
            },
            {
                "name": "uint32",
                "kind": "builtin",
            },
            {
                "name": "int64",
                "kind": "builtin",
            },
            {
                "name": "uint64",
                "kind": "builtin",
            },
            {
                "name": "double",
                "kind": "builtin",
            },
            {
                "name": "string",
                "kind": "builtin",
            },
            {
                "name": "array",
                "kind": "builtin",
                "regex": "array<(.*)>",
            },
            {
                "name": "dict",
                "kind": "builtin",
                "regex": "dict<(.*?), *(.*)>",
            },
        ]
        for object in builtin_objects:
            for language, types in language_types.items():
                if language in object:
                    continue
                object[language] = getattr(types, object['name'])
        return {
            "objects": builtin_objects
        }
