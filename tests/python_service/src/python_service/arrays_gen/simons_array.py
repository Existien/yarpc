# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/04.2_arrays_with_structs.yml
#   Object: SimonsArray
#   Template: py/struct.j2

from .struct_array import StructArray
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class SimonsArray:
    """
    A struct containing arrays

    Args:
        numbers (List[StructArray]): some struct arrays
    """
    numbers: List[StructArray]

    def to_dbus(self):
        """
        Marshals this object into an array compatible with dbus structs.

        Returns:
            list: the marshalled structure
        """
        return [
            [ x0.to_dbus() for x0 in self.numbers ],
        ]

    def from_dbus(dbus_struct: list):
        """
        Attempts to unmarshal a D-Bus struct array into this dataclass

        Args:
            dbus_struct (list): the marshalled D-Bus struct as array

        Returns:
            SimonsArray: the unmarshalled structure
        """
        return SimonsArray(
            numbers=[ StructArray.from_dbus(x0) for x0 in dbus_struct[0] ],
        )
