# Generated by YARPC
# Version:  0.1.0+editable
# Definition:
#   File: /workspace/tests/definitions/04.1_arrays.yml
#   Object: Arrays
#   Template: py/client_mock.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
from unittest.mock import Mock
import sys
import asyncio
from .struct_array import StructArray
from .simons_array import SimonsArray


class ArraysClientMock():
    """
    Mock client implementation of the Arrays D-Bus interface

    The Mock instance can be accessed via the `mock` attribute.
    All received signals will be forwarded to the mock using keyword arguments.
    E.g.
    A received signal `Fooed('bar')`
    might result in the following call of the mock:
    `client.mock.Fooed(msg='bar')`
    """

    def __init__(self):
        self.name = "com.yarpc.testservice.arrays"
        self._interface = None
        self._property_interface = None
        self.mock = Mock()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.testservice",
                "/com/yarpc/testservice",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.testservice",
                "/com/yarpc/testservice",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            self._interface.on_array_signal(self._ArraySignal_handler)

            self._property_interface = proxy_object.get_interface(
                "org.freedesktop.DBus.Properties"
            )
            if self._properties_changed_handler:
                self._property_interface.on_properties_changed(self._properties_changed_handler)

            await bus.wait_for_disconnect()
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)

    def _unpack_prop(self, name, variant):
        prop_map = {
            "ArrayProperty": lambda value: [ [ x1 for x1 in x0 ] for x0 in value ],
        }
        if name in prop_map:
            return prop_map[name](variant.value)
        return None

    def _unpack_properties(self, packed_properties):
        return {
            key: self._unpack_prop(key, packed_properties[key])
            for key in packed_properties.keys()
        }

    async def get_all_properties(self) -> dict:
        """Getter for all properties

        Returns:
            dict: a dictionary containing the current state of all properties
        """
        properties = await self._property_interface.call_get_all(self.name)
        return self._unpack_properties(properties)

    def _properties_changed_handler(self, interface: str, properties: dict, _invalidated: list):
        if interface == self.name:
            properties = self._unpack_properties(properties)
            self.mock.on_properties_changed(properties=properties)

    async def ArrayMethod(
        self,
        numbers: List[List[int]],
    ) -> List[List[float]]:
        """
        a simple method with one argument

        Args:
            numbers (List[List[int]]): Some numbers
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_array_method(
            [ [ x1 for x1 in x0 ] for x0 in numbers ],
        )
        return [ [ x1 for x1 in x0 ] for x0 in raw_return ]

    def _ArraySignal_handler(
        self,
            numbers: 'aad',
    ):
        self.mock.ArraySignal(
            [ [ x1 for x1 in x0 ] for x0 in numbers ],
        )

    async def get_ArrayProperty(self) -> List[List[str]]:
        """Getter for property 'ArrayProperty'

        a simple property

        Returns:
            List[List[str]]: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_array_property()
        unmarshalled = [ [ x1 for x1 in x0 ] for x0 in raw_return ]
        return unmarshalled

    async def set_ArrayProperty(self, value: List[List[str]]) -> None:
        """Setter for property 'ArrayProperty'

        a simple property

        Args:
            value (List[List[str]]): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = [ [ x1 for x1 in x0 ] for x0 in value ]
        return await self._interface.set_array_property(marshalled)
