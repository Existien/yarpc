# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/03_structs.yml
#   Object: Structs
#   Template: py/client.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
import sys
import asyncio
from .simple_struct import SimpleStruct
from .item import Item


class BackendStructsClient():
    """
    A interface with structures
    """

    def __init__(self):
        self.name = "com.yarpc.backend.structs"
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._StructReceived_handler = None
        self._close_event = asyncio.Event()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.backend",
                "/com/yarpc/backend/structs",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.backend",
                "/com/yarpc/backend/structs",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            if self._StructReceived_handler:
                self._interface.on_struct_received(self._StructReceived_wrapper)

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
        if self._StructReceived_handler:
            self._interface.off_struct_received(self._StructReceived_wrapper)
        if self._properties_changed_handler:
                self._property_interface.off_properties_changed(self._properties_changed_wrapper)
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._StructReceived_handler = None

    def _unpack_prop(self, name, variant):
        prop_map = {
            "Simple": lambda value: SimpleStruct.from_dbus(value),
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

    async def SendStruct(
        self,
        simpleStruct: 'SimpleStruct',
    ) -> SimpleStruct:
        """
        a method with a struct as args

        Args:
            simpleStruct (SimpleStruct): the SimpleStruct to send

        Returns:
            SimpleStruct: the SimpleStruct
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_send_struct(
            simpleStruct.to_dbus(),
        )
        return SimpleStruct.from_dbus(raw_return)

    def _StructReceived_wrapper(
        self,
        simpleStruct: '((sd)u)',
        totalCosts: 'd',
    ):
        self._StructReceived_handler(
            SimpleStruct.from_dbus(simpleStruct),
            totalCosts,
        )

    def on_StructReceived(self, handler):
        """
        Set handler for StructReceived signal

        Args:
            handler (Callable[[SimpleStruct, float], None]): the signal handler
        """
        self._StructReceived_handler = handler
        if self._interface:
            self._interface.on_struct_received(self._StructReceived_wrapper)

    async def get_Simple(self) -> SimpleStruct:
        """Getter for property 'Simple'

        a property for a simple struct

        Returns:
            SimpleStruct: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_simple()
        unmarshalled = SimpleStruct.from_dbus(raw_return)
        return unmarshalled


    async def set_Simple(self, value: SimpleStruct) -> None:
        """Setter for property 'Simple'

        a property for a simple struct

        Args:
            value (SimpleStruct): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = value.to_dbus()
        return await self._interface.set_simple(marshalled)
