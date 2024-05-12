# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/06.2_enums_with_arrays.yml
#   Object: EnumsWithArrays
#   Template: py/client_mock.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
from unittest.mock import Mock
import sys
import asyncio
from .enum_struct import EnumStruct
from .color import Color


class EnumsWithArraysClientMock():
    """
    Mock client implementation of the EnumsWithArrays D-Bus interface

    The Mock instance can be accessed via the `mock` attribute.
    All received signals will be forwarded to the mock using keyword arguments.
    E.g.
    A received signal `Fooed('bar')`
    might result in the following call of the mock:
    `client.mock.Fooed(msg='bar')`
    """

    def __init__(self):
        self.name = "com.yarpc.testservice.enumsWithArrays"
        self._interface = None
        self._property_interface = None
        self.mock = Mock()
        self._close_event = asyncio.Event()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.testservice",
                "/com/yarpc/testservice/enums",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.testservice",
                "/com/yarpc/testservice/enums",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            self._interface.on_enum_signal(self._EnumSignal_handler)

            self._property_interface = proxy_object.get_interface(
                "org.freedesktop.DBus.Properties"
            )
            if self._properties_changed_handler:
                self._property_interface.on_properties_changed(self._properties_changed_handler)

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
            self._interface.off_enum_signal(self._EnumSignal_handler)
        if self._properties_changed_handler:
                self._property_interface.off_properties_changed(self._properties_changed_handler)
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._EnumSignal_handler = None

    def _unpack_prop(self, name, variant):
        prop_map = {
            "EnumProperty": lambda value: [ Color(x0) for x0 in value ],
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

    async def EnumMethod(
        self,
        color: List[Color],
    ) -> List[Color]:
        """
        a simple method with one argument

        Args:
            color (List[Color]): a color
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_enum_method(
            [ x0.value for x0 in color ],
        )
        return [ Color(x0) for x0 in raw_return ]

    def _EnumSignal_handler(
        self,
            color: 'ai',
    ):
        self.mock.EnumSignal(
            [ Color(x0) for x0 in color ],
        )

    async def get_EnumProperty(self) -> List[Color]:
        """Getter for property 'EnumProperty'

        a property

        Returns:
            List[Color]: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_enum_property()
        unmarshalled = [ Color(x0) for x0 in raw_return ]
        return unmarshalled

    async def set_EnumProperty(self, value: List[Color]) -> None:
        """Setter for property 'EnumProperty'

        a property

        Args:
            value (List[Color]): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = [ x0.value for x0 in value ]
        return await self._interface.set_enum_property(marshalled)
