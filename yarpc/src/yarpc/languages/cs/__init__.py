from yarpc.languages.base_language import BaseLanguage, ObjectKind, Target, DBusTypes
from typing import Callable, Dict, List


def _object_path_to_class_name(object_path):
    class_name = ""
    capitalize=False
    for i in range(0, len(object_path)):
        if (object_path[i] == "/"):
            capitalize=True
        elif (capitalize):
            class_name += object_path[i].upper()
            capitalize = False
        else:
            class_name += object_path[i]
    return class_name


class Language(BaseLanguage):

    def get_output_targets(self) -> List[Target]:
        """Returns a list of targets that are object-independent,
        such as package information.

        Returns:
            List[Target]: a list of targets to be generated.
        """
        return [
            Target(filename="Connection.cs", template="Connection"),
            Target(filename="IClient.cs", template="IClient"),
            Target(filename="NotConnectedException.cs", template="NotConnectedException"),
            Target(filename="ObjectPaths.cs", template="ObjectPaths"),
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
        return [Target(
            filename=f"{name}.cs",
            template=object_kind.value
        )]

    def get_dbus_types(self) -> DBusTypes:
        """Returns the mapping from D-Bus types to types of this language.

        Returns:
            DBusTypes: the mapping between D-Bus types and types of this language
        """
        return DBusTypes(
            uint8='byte',
            bool='bool',
            int16='Int16',
            uint16='UInt16',
            int32='Int32',
            uint32='UInt32',
            int64='Int64',
            uint64='UInt64',
            double='double',
            string='string',
            array='$1[]',
            dict='Dictionary<$1, $2>',
        )

    def get_jinja_filters(self) -> Dict[str, Callable[... ,object]]:
        """Returns a dictionary containing language-specific
        jinja filters.

        Returns:
            Dict[str, Callable[... ,object]: the language-specific jinja filters
        """
        return {
            "object_path_to_camel": _object_path_to_class_name,
        }

    def get_jinja_globals(self) -> Dict[str, object]:
        """Returns a dictionary containing language-specific
        global objects.

        Returns:
            Dict[str, object]: the language-specific jinja globals
        """
        return {}