import sys

class SpecResolver:

    def __init__(self, specs):
        self._specs = specs

    def get_outputs(self):
        outputs = list(*map(
            lambda x: x['outputs'],
            filter(
                lambda x: 'outputs' in x,
                self._specs
            )
        ))
        self._check_for_duplicate_names(outputs)

        objects = list(*map(
            lambda x: x['objects'],
            filter(
                lambda x: 'objects' in x,
                self._specs
            )
        ))
        self._check_for_duplicate_names(objects)

        for output in outputs:
            output['objects'] = self._get_dependencies(output, objects)

        return outputs

    def _check_for_duplicate_names(self, items):
        names = []
        for item in items:
            if item['name'] in names:
                print(f"Duplicate name: '{item['name']}'", file=sys.stderr)
                sys.exit(1)
            else:
                names.append(item['name'])

    def _get_dependencies(self, output, objects) -> list:
        interface_names = self._get_interface_names(output)
        interfaces = list(filter(
            lambda x: x['name'] in interface_names,
            objects
        ))
        if len(interfaces) != len(interface_names):
            added_names = list(map(lambda x: x['name'], interfaces))
            for name in interface_names:
                if name not in added_names:
                    print(f"Interface spec not found: '{name}'", file=sys.stderr)
            sys.exit(1)

        required_objects = interfaces
        return required_objects



    def _get_interface_names(self, output) -> set:
        keys = filter(
            lambda x: x in ["services", "clients", "mocks"],
            output.keys()
        )
        interface_names = set()
        for key in keys:
            for interface in output[key]:
                interface_names.add(interface['spec'])
        return interface_names


