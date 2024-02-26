# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/03_structs.yml
#   Object: Item
#   Template: py/struct.j2

from dataclasses import dataclass
from typing import Sequence, Mapping

@dataclass
class Item:
    """
    an item

    Args:
        name (str): the name
        price (float): the price
    """
    name: str
    price: float

    def to_dbus(self):
        """
        Marshals this object into an array compatible with dbus structs.

        Returns:
            list: the marshalled structure
        """
        return [
            self.name,
            self.price,
        ]

    def from_dbus(dbus_struct: list):
        """
        Attempts to unmarshal a D-Bus struct array into this dataclass

        Args:
            dbus_struct (list): the marshalled D-Bus struct as array

        Returns:
            Item: the unmarshalled structure
        """
        return Item(
            name=dbus_struct[0],
            price=dbus_struct[1],
        )
