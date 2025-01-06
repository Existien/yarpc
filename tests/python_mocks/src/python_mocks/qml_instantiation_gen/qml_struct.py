# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/qt6/07_qml_instantiation.yml
#   Object: QmlStruct
#   Template: py/struct.j2

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class QmlStruct:
    """
    A struct

    Args:
        content (str): the content
        number (float): a number
    """
    content: str
    number: float

    def to_dbus(self):
        """
        Marshals this object into an array compatible with dbus structs.

        Returns:
            list: the marshalled structure
        """
        return [
            self.content,
            self.number,
        ]

    def from_dbus(dbus_struct: list):
        """
        Attempts to unmarshal a D-Bus struct array into this dataclass

        Args:
            dbus_struct (list): the marshalled D-Bus struct as array

        Returns:
            QmlStruct: the unmarshalled structure
        """
        return QmlStruct(
            content=dbus_struct[0],
            number=dbus_struct[1],
        )
