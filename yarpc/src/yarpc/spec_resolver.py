import re
from copy import deepcopy
from .utils import find_types

class SpecResolver:
    """Accepts a list of specifications and turns it into outputs.

    Args:
        specs (list): a list of loaded specifications
    """

    def __init__(self, specs):
        self._specs = specs
        self._interface_name_pattern = re.compile("^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z0-9_])+")
        self._bus_name_pattern = re.compile("^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z0-9_])+")
        self._object_path_pattern = re.compile("^\/([a-zA-Z0-9_]+(\/[a-zA-Z0-9_]+)*)?")

    def get_outputs(self) -> list:
        """Returns a list of outputs that contain
        all information needed to generate them.

        Returns:
            list: A list of outputs to be generated
        """
        outputs = []
        for spec in filter(lambda x: 'outputs' in x, self._specs):
            outputs.extend(spec['outputs'])
        self._check_for_duplicate_names(outputs, kind='output name')
        for output in outputs:
            targets = []
            for key in filter(
                lambda x: x in ['services', 'clients', 'service_mocks', 'client_mocks'],
                output.keys()
            ):
                targets.extend(output[key])
            self._check_for_duplicate_names(targets, kind='class name', key='className')

        objects = []
        for spec in filter(lambda x: 'objects' in x, self._specs):
            objects.extend(spec['objects'])
        self._check_for_duplicate_names(objects, kind='object name')

        for output in outputs:
            output['objects'] = self._get_dependencies(output, objects)

        return outputs

    def _check_for_duplicate_names(self, items: list, kind='name', key='name'):
        """Checks for duplicate names and raises a RuntimeError if duplicates are found.

        Args:
            items (list): A list of items to search for duplicates
            kind (str): The string representation of the duplication to check for (only used in Error messages)
            key (str): The attribute to check duplication for
        Throws:
            RuntimeError: If a duplicate was found
        """
        names = []
        for item in items:
            if item[key] in names:
                raise RuntimeError(f"Duplicate {kind}: '{item[key]}'")
            else:
                names.append(item[key])

    def _get_dependencies(self, output: dict, objects: list) -> list:
        """Returns all dependencies of output found in objects

        Args:
            output (dict): The output to find dependencies for
            objects (list): A list of objects to look for dependencies in

        Returns:
            list: A list of objects needed for the output provided
        """
        interfaces = self._get_interfaces(output, objects)
        types = self._get_types(interfaces, objects)
        required_objects = [*types, *interfaces]
        return required_objects

    def _get_types(self, interfaces: list, objects: list) -> list:
        """Returns a list of types needed for the interfaces provided

        Args:
            interfaces (list): A list of interfaces to return the types for
            objects (list): The list of objects to search for the types in

        Returns:
            list: A list of types needed for the interfaces provided
        """
        types = []

        def is_already_accounted_for(type_name: str) -> bool:
            return bool(list(filter(lambda x: x.get('name') == type_name, types)))

        def add_type(type_name: str):
            type_objects = find_types(type_name, objects)
            for type_object in type_objects:
                if is_already_accounted_for(type_object.get('name')):
                    continue

                if type_object.get('kind') == 'builtin':
                    types.append(type_object)
                if type_object.get('kind') == 'struct':
                    types.append(type_object)
                    for member in type_object.get('members', []):
                        add_type(member['type'])
                if type_object.get('kind') == 'enum':
                    types.append(type_object)
                    add_type('int32')

        for interface in interfaces:
            for member in interface.get('members', []):
                if member.get('type'):
                    add_type(member['type'])
                for arg in member.get('args', []):
                    add_type(arg['type'])
                returns = member.get('returns')
                if returns:
                    add_type(returns.get('type'))

        return types

    def _get_interfaces(self, output: dict, objects: list) -> list:
        """Extracts interfaces needed for an output from a list of objects

        Args:
            output (dict): The output to find interfaces for
            objects (list): The list of objects to find the interfaces in

        Returns:
            list: The list of interfaces to generate
        """
        def interface_list_to_dict(list_key, template):
            return { x['spec']: {
            'className': x['className'],
            'template': template,
            'busName': x.get('busName', output['busName']),
            'objectPath': x['objectPath'],
            'interfaceName': x['interfaceName'],
        } for x in output.get(list_key, [])}

        services = interface_list_to_dict('services', 'service')
        clients = interface_list_to_dict('clients', 'client')
        service_mocks = interface_list_to_dict('service_mocks', 'service_mock')
        client_mocks = interface_list_to_dict('client_mocks', 'client_mock')
        all_names = set([*services.keys(), *clients.keys(), *service_mocks.keys(), *client_mocks.keys()])

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
            interface['targets'] = [
                {
                    'template': 'bus',
                    'className': 'Connection',
                }
            ]
            if name in services.keys():
                interface['targets'].append(services[name])
            if name in clients.keys():
                interface['targets'].append(clients[name])
            if name in service_mocks.keys():
                interface['targets'].append(service_mocks[name])
            if name in client_mocks.keys():
                interface['targets'].append(client_mocks[name])

            self._validate_interface_targets(interface['targets'][1:])
        return interfaces

    def _validate_interface_targets(self, targets: list):
        """Checks whether D-Bus attributes conform to D-Bus spec.
        Throws RuntimeErrors if not.

        Args:
            targets (list): A list of targets

        Throws:
            RuntimeError: If the target attributes do not conform to the D-Bus spec
        """
        for target in targets:
            if not self._interface_name_pattern.match(target['interfaceName']):
                raise RuntimeError(f"Invalid interface name: {target['interfaceName']}")
            if not self._object_path_pattern.match(target['objectPath']):
                raise RuntimeError(f"Invalid object path: {target['objectPath']}")
            if not self._bus_name_pattern.match(target['busName']):
                raise RuntimeError(f"Invalid D-Bus name: {target['busName']}")
