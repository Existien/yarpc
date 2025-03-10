# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/06.1_enums.yml
#   Object: Enums
#   Template: py/client.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
import sys
import asyncio
from .enum_struct import EnumStruct
from .color import Color


class BackendEnumsClient():
    """
    A interface using enums
    """

    def __init__(self):
        self.name = "com.yarpc.backend.enums"
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._EnumSignal_handler = None
        self._close_event = asyncio.Event()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.backend",
                "/com/yarpc/backend/enums",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.backend",
                "/com/yarpc/backend/enums",
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
        if self._EnumSignal_handler:
            self._interface.off_enum_signal(self._EnumSignal_wrapper)
        if self._properties_changed_handler:
                self._property_interface.off_properties_changed(self._properties_changed_wrapper)
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._EnumSignal_handler = None

    def _unpack_prop(self, name, variant):
        prop_map = {
            "EnumProperty": lambda value: Color(value),
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
        color: 'Color',
    ) -> Color:
        """
        a simple method with one argument

        Args:
            color (Color): a color

        Returns:
            Color: another color
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_enum_method(
            color.value,
        )
        return Color(raw_return)

    def _EnumSignal_wrapper(
        self,
        color: 'i',
    ):
        self._EnumSignal_handler(
            Color(color),
        )

    def on_EnumSignal(self, handler):
        """
        Set handler for EnumSignal signal

        Args:
            handler (Callable[[Color], None]): the signal handler
        """
        self._EnumSignal_handler = handler
        if self._interface:
            self._interface.on_enum_signal(self._EnumSignal_wrapper)

    async def get_EnumProperty(self) -> Color:
        """Getter for property 'EnumProperty'

        a property

        Returns:
            Color: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_enum_property()
        unmarshalled = Color(raw_return)
        return unmarshalled


    async def set_EnumProperty(self, value: Color) -> None:
        """Setter for property 'EnumProperty'

        a property

        Args:
            value (Color): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = value.value
        return await self._interface.set_enum_property(marshalled)
