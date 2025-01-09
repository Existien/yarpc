from yarpc.languages.base_language import BaseLanguage, ObjectKind, Target, DBusTypes
from typing import List, Dict, Callable
from yarpc.utils import extract_inner_names, find_type


def _get_list_of_types(objects):
    def get_inner(name):
        inner_types = []
        if name.startswith('array'):
            inner = extract_inner_names(name, find_type(name, objects))
            inner_types.append(inner[0])
            inner_types.extend(get_inner(inner[0]))
        if name.startswith('dict'):
            inner = extract_inner_names(name, find_type(name, objects))
            inner_types.extend(inner)
            inner_types.extend(get_inner(inner[1]))
        return inner_types

    list_of_types = []
    for item in filter(lambda x: x['kind'] == 'struct', objects):
        for member in item.get('members', []):
            list_of_types.append(member['type'])
    for item in filter(lambda x: x['kind'] == 'interface', objects):
        for member in item.get('members', []):
            for arg in member.get('args', []):
                list_of_types.append(arg['type'])
            if member.get('returns'):
                list_of_types.append(member['returns']['type'])
            if member.get('type'):
                list_of_types.append(member['type'])
    for type in set(list_of_types):
        list_of_types.extend(get_inner(type))
    return set(list_of_types)


def _get_list_of_arrays(objects):
    return list(filter(lambda x: x.startswith('array'), _get_list_of_types(objects)))


def _get_list_of_dicts(objects):
    return list(filter(lambda x: x.startswith('dict'), _get_list_of_types(objects)))


def _get_array_types(name, objects):
    return list(map(
        lambda x: x.replace(' ',""),
        filter(
            lambda x: f"<{name}>" in x,
            _get_list_of_arrays(objects)
        )
    ))


def _get_dict_types(name, objects):
    return list(map(
        lambda x: x.replace(' ',""),
        filter(
            lambda x: f"{name}>" in x,
            _get_list_of_dicts(objects)
        )
    ))


def _needs_marshalling(name, objects):
    type_object = find_type(name, objects)
    if type_object.get('kind', "") == 'enum':
        return False
    if type_object.get('kind', "") == 'builtin':
        obj_name = type_object.get('name', "")
        if obj_name != 'array' and obj_name != 'dict':
            return False
    return True


class Language(BaseLanguage):

    def get_output_targets(self) -> List[Target]:
        """Returns a list of targets that are object-independent,
        such as package information.

        Returns:
            List[Target]: a list of targets to be generated.
        """
        return [
            Target(
                filename="CMakeLists.txt",
                template="CMakeLists"
            ),
            Target(
                filename="DBusError.hpp",
                template="error_header"
            ),
            Target(
                filename="DBusError.cpp",
                template="error_source"
            ),
            Target(
                filename="Connection.hpp",
                template="connection_header"
            ),
            Target(
                filename="Connection.cpp",
                template="connection_source"
            ),
            Target(
                filename="types.hpp",
                template="types_header"
            ),
            Target(
                filename="types.cpp",
                template="types_source"
            ),
        ]

    def get_object_targets(self, name: str, object_kind: ObjectKind) -> List[Target]:
        """Returns a list of targets for an object that need to be generated.

        Args:
            name (str): Name of the object
            object_kind (ObjectKind): the kind of object
        Returns:
            List[Target]: a list of targets to be generated.
                Empty for non-supported ObjectKinds.
        """
        if object_kind == ObjectKind.Service:
            return [
                Target(
                    filename=f"{name}Adaptor.hpp",
                    template=f"adaptor_header"
                ),
                Target(
                    filename=f"{name}Adaptor.cpp",
                    template=f"adaptor_source"
                ),
                Target(
                    filename=f"{name}.hpp",
                    template=f"{object_kind.value}_header"
                ),
                Target(
                    filename=f"{name}.cpp",
                    template=f"{object_kind.value}_source"
                ),
            ]
        else:
            return [
                Target(
                    filename=f"{name}.hpp",
                    template=f"{object_kind.value}_header"
                ),
                Target(
                    filename=f"{name}.cpp",
                    template=f"{object_kind.value}_source"
                ),
            ]

    def get_dbus_types(self) -> DBusTypes:
        """Returns the mapping from D-Bus types to types of this language.

        Returns:
            DBusTypes: the mapping between D-Bus types and types of this language
        """
        return DBusTypes(
            uint8='uchar',
            bool='bool',
            int16='short',
            uint16='ushort',
            int32='int',
            uint32='uint',
            int64='qlonglong',
            uint64='qulonglong',
            double='double',
            string='QString',
            array='QList<$1>',
            dict='QMap<$1, $2>',
        )

    def get_jinja_filters(self) -> Dict[str, Callable[... ,object]]:
        """Returns a dictionary containing language-specific
        jinja filters.

        Returns:
            Dict[str, Callable[... ,object]: the language-specific jinja filters
        """
        return {
            "array_types": _get_array_types,
            "dict_types": _get_dict_types,
            "needs_marshalling": _needs_marshalling,
        }

    def get_jinja_globals(self) -> Dict[str, object]:
        """Returns a dictionary containing language-specific
        global objects.

        Returns:
            Dict[str, object]: the language-specific jinja globals
        """
        return {
            'get_list_of_arrays': _get_list_of_arrays,
            'get_list_of_dicts': _get_list_of_dicts,
        }
