import re

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
            if (output.get('dbusName')):
                self._validate_dbus_name(output.get('dbusName'))
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
        services = { x['spec']: {
            'template': 'service',
            'interface_name': x['name'],
            'object_path': x['path']
        } for x in output.get('services', [])}
        clients = { x['spec']: {
            'template': 'client',
            'interface_name': x['name'],
            'object_path': x['path']
        } for x in output.get('clients', [])}
        mocks = { x['spec']: {
            'template': 'mock',
            'interface_name': x['name'],
            'object_path': x['path']
        } for x in output.get('mocks', [])}
        all_names = set([*services.keys(), *clients.keys(), *mocks.keys()])

        interfaces = list(filter(
            lambda x: x['name'] in all_names,
            objects
        ))
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
            if not self._interface_name_pattern.match(target['interface_name']):
                raise RuntimeError(f"Invalid interface name: {target['interface_name']}")
            if not self._object_path_pattern.match(target['object_path']):
                raise RuntimeError(f"Invalid object path: {target['object_path']}")

    def _validate_dbus_name(self, dbus_name):
        if not self._bus_name_pattern.match(dbus_name):
            raise RuntimeError(f"Invalid D-Bus name: {dbus_name}")
