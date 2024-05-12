from yarpc.languages.base_language import BaseLanguage, ObjectKind, Target, DBusTypes
from typing import List, Dict, Callable

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
        return {}

    def get_jinja_globals(self) -> Dict[str, object]:
        """Returns a dictionary containing language-specific
        global objects.

        Returns:
            Dict[str, object]: the language-specific jinja globals
        """
        return {}
