from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Callable


class ObjectKind(Enum):
    """The kind of object.
    Mainly used to determine the templates needed to generated
    the code for the object.
    """
    Bus='bus'
    Enum='enum'
    Struct='struct'
    Service='service'
    Client='client'
    ServiceMock='service_mock'
    ClientMock='client_mock'


@dataclass
class Target:
    """The name of the file to generate and the template to generate it with.

    Filename without paths, since the path will be determined by the output object.
    """
    filename: str
    template: str


@dataclass
class DBusTypes:
    """Mapping of D-Bus types to types of this language.

    Use $1 and $2 as placeholder for generics parameters.
    (e.g. std::array<$1> or std::dict<$1,$2>)
    """
    uint8: str
    bool: str
    int16: str
    uint16: str
    int32: str
    uint32: str
    int64: str
    uint64: str
    double: str
    string: str
    array: str
    dict: str


class BaseLanguage:

    def get_output_targets(self) -> List[Target]:
        """Returns a list of targets that are object-independent,
        such as package information.

        Returns:
            List[Target]: a list of targets to be generated.
        """
        raise NotImplementedError()

    def get_object_targets(self, name: str, object_kind: ObjectKind) -> List[Target]:
        """Returns a list of targets for an object that need to be generated.

        Args:
            name (str): Name of the object
            object_kind (ObjectKind): the kind of object
        Returns:
            List[Target]: a list of targets to be generated.
                Empty for non-supported ObjectKinds.
        """
        raise NotImplementedError()

    def get_dbus_types(self) -> DBusTypes:
        """Returns the mapping from D-Bus types to types of this language.

        Returns:
            DBusTypes: the mapping between D-Bus types and types of this language
        """
        raise NotImplementedError()

    def get_jinja_filters(self) -> Dict[str, Callable[... ,object]]:
        """Returns a dictionary containing language-specific
        jinja filters.

        Returns:
            Dict[str, Callable[... ,object]: the language-specific jinja filters
        """
        raise NotImplementedError()

