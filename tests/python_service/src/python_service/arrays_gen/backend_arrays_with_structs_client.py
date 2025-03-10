# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
#   Object: ArraysWithStructs
#   Template: py/client.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
import sys
import asyncio
from .struct_array import StructArray
from .simons_array import SimonsArray


class BackendArraysWithStructsClient():
    """
    A interface using arrays using structs using arrays
    """

    def __init__(self):
        self.name = "com.yarpc.backend.arraysWithStructs"
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._ArrayStructSignal_handler = None
        self._close_event = asyncio.Event()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.backend",
                "/com/yarpc/backend/arrays",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.backend",
                "/com/yarpc/backend/arrays",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            if self._ArrayStructSignal_handler:
                self._interface.on_array_struct_signal(self._ArrayStructSignal_wrapper)

            self._property_interface = proxy_object.get_interface(
                "org.freedesktop.DBus.Properties"
            )
            if self._properties_changed_handler:
                self._property_interface.on_properties_changed(self._properties_changed_wrapper)

            self._close_event.clear()
            await asyncio.wait(
                map(
                    lambda x: asyncio.create_task(x),
                    [self._close_event.wait(), bus.wait_for_disconnect()]
                ),
                return_when=asyncio.FIRST_COMPLETED
            )
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)

    def disconnect(self):
        """
        Closes the D-Bus connection of this client
        """
        self._close_event.set()
        if self._ArrayStructSignal_handler:
            self._interface.off_array_struct_signal(self._ArrayStructSignal_wrapper)
        if self._properties_changed_handler:
                self._property_interface.off_properties_changed(self._properties_changed_wrapper)
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._ArrayStructSignal_handler = None

    def _unpack_prop(self, name, variant):
        prop_map = {
            "ArrayStructProperty": lambda value: [ StructArray.from_dbus(x0) for x0 in value ],
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

    async def ArrayStructMethod(
        self,
        numbers: 'List[StructArray]',
    ) -> List[SimonsArray]:
        """
        a simple method with one argument

        Args:
            numbers (List[StructArray]): Some numbers

        Returns:
            List[SimonsArray]: more numbers
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_array_struct_method(
            [ x0.to_dbus() for x0 in numbers ],
        )
        return [ SimonsArray.from_dbus(x0) for x0 in raw_return ]

    def _ArrayStructSignal_wrapper(
        self,
        numbers: 'a(aau)',
    ):
        self._ArrayStructSignal_handler(
            [ StructArray.from_dbus(x0) for x0 in numbers ],
        )

    def on_ArrayStructSignal(self, handler):
        """
        Set handler for ArrayStructSignal signal

        Args:
            handler (Callable[[List[StructArray]], None]): the signal handler
        """
        self._ArrayStructSignal_handler = handler
        if self._interface:
            self._interface.on_array_struct_signal(self._ArrayStructSignal_wrapper)

    async def get_ArrayStructProperty(self) -> List[StructArray]:
        """Getter for property 'ArrayStructProperty'

        a simple property

        Returns:
            List[StructArray]: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_array_struct_property()
        unmarshalled = [ StructArray.from_dbus(x0) for x0 in raw_return ]
        return unmarshalled


    async def set_ArrayStructProperty(self, value: List[StructArray]) -> None:
        """Setter for property 'ArrayStructProperty'

        a simple property

        Args:
            value (List[StructArray]): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = [ x0.to_dbus() for x0 in value ]
        return await self._interface.set_array_struct_property(marshalled)
