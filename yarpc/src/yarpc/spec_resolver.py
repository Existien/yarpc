import re
from copy import deepcopy

class SpecResolver:

    def __init__(self, specs):
        self._specs = specs
        self._interface_name_pattern = re.compile("^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z0-9_])+")
        self._bus_name_pattern = re.compile("^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z0-9_])+")
        self._object_path_pattern = re.compile("^\/([a-zA-Z0-9_]+(\/[a-zA-Z0-9_]+)*)?")

    def get_outputs(self):
        outputs = []
        for spec in filter(lambda x: 'outputs' in x, self._specs):
            outputs.extend(spec['outputs'])
        self._check_for_duplicate_names(outputs)

        objects = []
        for spec in filter(lambda x: 'objects' in x, self._specs):
            objects.extend(spec['objects'])
        self._check_for_duplicate_names(objects)

        for output in outputs:
            output['objects'] = self._get_dependencies(output, objects)

        return outputs

    def _check_for_duplicate_names(self, items):
        names = []
        for item in items:
            if item['name'] in names:
                raise RuntimeError(f"Duplicate name: '{item['name']}'")
            else:
                names.append(item['name'])

    def _get_dependencies(self, output, objects) -> list:
        interfaces = self._get_interfaces(output, objects)
        required_objects = interfaces
        return required_objects

    def _get_interfaces(self, output, objects) -> list:
        def interface_list_to_dict(list_key, template):
            return { x['spec']: {
            'template': template,
            'busName': x['busName'],
            'objectPath': x['objectPath'],
            'interfaceName': x['interfaceName'],
        } for x in output.get(list_key, [])}

        services = interface_list_to_dict('services', 'service')
        clients = interface_list_to_dict('clients', 'client')
        mocks = interface_list_to_dict('mocks', 'mock')
        all_names = set([*services.keys(), *clients.keys(), *mocks.keys()])

        interfaces = list(map(
            lambda x: deepcopy(x),
            filter(
                lambda x: x['name'] in all_names,
                objects
        )))
        if len(interfaces) != len(all_names):
            added_names = list(map(lambda x: x['name'], interfaces))
            missing = []
            for name in all_names:
                if name not in added_names:
                    missing.append(name)
            raise FileNotFoundError(f"Interface specs not found: {missing}")

        for interface in interfaces:
            name = interface['name']
            interface['targets'] = []
            if name in services.keys():
                interface['targets'].append(services[name])
            if name in clients.keys():
                interface['targets'].append(clients[name])
            if name in mocks.keys():
                interface['targets'].append(mocks[name])

        self._validate_targets(interface['targets'])
        return interfaces

    def _validate_targets(self, targets):
        for target in targets:
            if not self._interface_name_pattern.match(target['interfaceName']):
                raise RuntimeError(f"Invalid interface name: {target['interfaceName']}")
            if not self._object_path_pattern.match(target['objectPath']):
                raise RuntimeError(f"Invalid object path: {target['objectPath']}")
            if not self._bus_name_pattern.match(target['busName']):
                raise RuntimeError(f"Invalid D-Bus name: {target['busName']}")
