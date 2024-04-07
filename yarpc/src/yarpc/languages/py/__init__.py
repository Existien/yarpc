from yarpc.languages.base_language import BaseLanguage, ObjectKind, Target, DBusTypes
from typing import List
from yarpc.utils import to_snake_case

class Language(BaseLanguage):

    def get_output_targets(self) -> List[Target]:
        """Returns a list of targets that are object-independent,
        such as package information.

        Returns:
            List[Target]: a list of targets to be generated.
        """
        return [
            Target(filename="__init__.py", template="__init__"),
            Target(filename="connection.py", template="bus"),
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
            filename=f"{to_snake_case(name)}.py",
            template=object_kind.value
        )]

    def get_dbus_types(self) -> DBusTypes:
        """Returns the mapping from D-Bus types to types of this language.

        Returns:
            DBusTypes: the mapping between D-Bus types and types of this language
        """
        return DBusTypes(
            uint8='int',
            bool='bool',
            int16='int',
            uint16='int',
            int32='int',
            uint32='int',
            int64='int',
            uint64='int',
            double='float',
            string='str',
            array='List[$1]',
            dict='Dict[$1, $2]',
        )