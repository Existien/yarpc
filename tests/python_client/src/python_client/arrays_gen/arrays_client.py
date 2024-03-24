# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/04.1_arrays.yml
#   Object: Arrays
#   Template: py/client.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
import sys
import asyncio
from .struct_array import StructArray
from .simons_array import SimonsArray


class ArraysClient():
    """
    A interface using arrays
    """

    def __init__(self):
        self.name = "com.yarpc.testservice.arrays"
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._ArraySignal_handler = None

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

            if self._ArraySignal_handler:
                self._interface.on_array_signal(self._ArraySignal_wrapper)

            self._property_interface = proxy_object.get_interface(
                "org.freedesktop.DBus.Properties"
            )
            if self._properties_changed_handler:
                self._property_interface.on_properties_changed(self._properties_changed_wrapper)

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
        while not self._property_interface:
            await asyncio.sleep(0.1)
        properties = await self._property_interface.call_get_all(self.name)
        return self._unpack_properties(properties)

    def _properties_changed_wrapper(self, interface: str, properties: dict, _invalidated: list):
        if self._properties_changed_handler and interface == self.name:
            properties = self._unpack_properties(properties)
            self._properties_changed_handler(properties)

    def on_properties_changed(self, handler) -> None:
        """
        Set handler for property changes

        The handler takes a dictionary of the changed properties

        Args:
            handler(Callable[[dict], None]): the handler
        """
        self._properties_changed_handler = handler

    async def ArrayMethod(
        self,
        numbers: 'List[List[int]]',
    ) -> List[List[float]]:
        """
        a simple method with one argument

        Args:
            numbers (List[List[int]]): Some numbers

        Returns:
            List[List[float]]: normalized numbers
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_array_method(
            [ [ x1 for x1 in x0 ] for x0 in numbers ],
        )
        return [ [ x1 for x1 in x0 ] for x0 in raw_return ]

    def _ArraySignal_wrapper(
        self,
        numbers: 'aad',
    ):
        self._ArraySignal_handler(
            [ [ x1 for x1 in x0 ] for x0 in numbers ],
        )

    def on_ArraySignal(self, handler):
        """
        Set handler for ArraySignal signal

        Args:
            handler (Callable[[List[List[float]]], None]): the signal handler
        """
        self._ArraySignal_handler = handler
        if self._interface:
            self._interface.on_array_signal(self._ArraySignal_wrapper)

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
