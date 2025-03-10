# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/06.4_enums_with_structs.yml
#   Object: EnumStruct
#   Template: py/struct.j2

from .color import Color
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class EnumStruct:
    """
    a struct

    Args:
        color (Color): a color
        colorArray (List[Color]): colors
        colorDict (Dict[Color, Color]): color map
    """
    color: Color
    colorArray: List[Color]
    colorDict: Dict[Color, Color]

    def to_dbus(self):
        """
        Marshals this object into an array compatible with dbus structs.

        Returns:
            list: the marshalled structure
        """
        return [
            self.color.value,
            [ x0.value for x0 in self.colorArray ],
            { k0.value: v0.value for k0, v0 in self.colorDict.items() },
        ]

    def from_dbus(dbus_struct: list):
        """
        Attempts to unmarshal a D-Bus struct array into this dataclass

        Args:
            dbus_struct (list): the marshalled D-Bus struct as array

        Returns:
            EnumStruct: the unmarshalled structure
        """
        return EnumStruct(
            color=Color(dbus_struct[0]),
            colorArray=[ Color(x0) for x0 in dbus_struct[1] ],
            colorDict={ Color(k0): Color(v0) for k0, v0 in dbus_struct[2].items() },
        )
