# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/06.2_enums_with_structs.yml
#   Object: EnumsWithStructs
#   Template: py/client.j2

from typing import Sequence, Mapping
from .connection import Connection
from dbus_next import Variant, DBusError
import sys
import asyncio
from .enum_struct import EnumStruct
from .color import Color


class BackendEnumsWithStructsClient():
    """
    A interface using enums
    """

    def __init__(self):
        self.name = "com.yarpc.backend.enumsWithStructs"
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._EnumSignal_handler = None

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.backend",
                "/com/yarpc/backend",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.backend",
                "/com/yarpc/backend",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            if self._EnumSignal_handler:
                self._interface.on_enum_signal(self._EnumSignal_wrapper)

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
            "EnumProperty": lambda value: EnumStruct.from_dbus(value),
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

    async def EnumMethod(
        self,
        color: 'EnumStruct',
    ) -> EnumStruct:
        """
        a simple method with one argument

        Args:
            color (EnumStruct): a color

        Returns:
            EnumStruct: another color
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_enum_method(
            color.to_dbus(),
        )
        return EnumStruct.from_dbus(raw_return)

    def _EnumSignal_wrapper(
        self,
        color: '(iaia{ii})',
    ):
        self._EnumSignal_handler(
            EnumStruct.from_dbus(color),
        )

    def on_EnumSignal(self, handler):
        """
        Set handler for EnumSignal signal

        Args:
            handler (Callable[[EnumStruct], None]): the signal handler
        """
        self._EnumSignal_handler = handler
        if self._interface:
            self._interface.on_enum_signal(self._EnumSignal_wrapper)

    async def get_EnumProperty(self) -> EnumStruct:
        """Getter for property 'EnumProperty'

        a property

        Returns:
            EnumStruct: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_enum_property()
        unmarshalled = EnumStruct.from_dbus(raw_return)
        return unmarshalled


    async def set_EnumProperty(self, value: EnumStruct) -> None:
        """Setter for property 'EnumProperty'

        a property

        Args:
            value (EnumStruct): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = value.to_dbus()
        return await self._interface.set_enum_property(marshalled)
