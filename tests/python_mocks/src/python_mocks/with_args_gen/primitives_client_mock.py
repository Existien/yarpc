# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/02.2_primitives.yml
#   Object: Primitives
#   Template: py/client_mock.j2

from typing import Sequence, Mapping
from .connection import Connection
from dbus_next import Variant, DBusError
from unittest.mock import Mock
import sys
import asyncio


class PrimitivesClientMock():
    """
    Mock client implementation of the Primitives D-Bus interface

    The Mock instance can be accessed via the `mock` attribute.
    All received signals will be forwarded to the mock using keyword arguments.
    E.g.
    A received signal `Fooed('bar')`
    might result in the following call of the mock:
    `client.mock.Fooed(msg='bar')`
    """

    def __init__(self):
        self.name = "com.yarpc.testservice.primitives"
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

            self._interface.on_uint8_signal(self._Uint8Signal_handler)
            self._interface.on_bool_signal(self._BoolSignal_handler)
            self._interface.on_int16_signal(self._Int16Signal_handler)
            self._interface.on_uint16_signal(self._Uint16Signal_handler)
            self._interface.on_int32_signal(self._Int32Signal_handler)
            self._interface.on_uint32_signal(self._Uint32Signal_handler)
            self._interface.on_int64_signal(self._Int64Signal_handler)
            self._interface.on_uint64_signal(self._Uint64Signal_handler)
            self._interface.on_double_signal(self._DoubleSignal_handler)
            self._interface.on_string_signal(self._StringSignal_handler)

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

    def _Uint8Signal_handler(
        self,
            value: 'y',
    ):
        self.mock.Uint8Signal(
            value,
        )

    def _BoolSignal_handler(
        self,
            value: 'b',
    ):
        self.mock.BoolSignal(
            value,
        )

    def _Int16Signal_handler(
        self,
            value: 'n',
    ):
        self.mock.Int16Signal(
            value,
        )

    def _Uint16Signal_handler(
        self,
            value: 'q',
    ):
        self.mock.Uint16Signal(
            value,
        )

    def _Int32Signal_handler(
        self,
            value: 'i',
    ):
        self.mock.Int32Signal(
            value,
        )

    def _Uint32Signal_handler(
        self,
            value: 'u',
    ):
        self.mock.Uint32Signal(
            value,
        )

    def _Int64Signal_handler(
        self,
            value: 'x',
    ):
        self.mock.Int64Signal(
            value,
        )

    def _Uint64Signal_handler(
        self,
            value: 't',
    ):
        self.mock.Uint64Signal(
            value,
        )

    def _DoubleSignal_handler(
        self,
            value: 'd',
    ):
        self.mock.DoubleSignal(
            value,
        )

    def _StringSignal_handler(
        self,
            value: 's',
    ):
        self.mock.StringSignal(
            value,
        )

    async def Uint8Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint8_method(
            value,
        )
        return raw_return

    async def BoolMethod(
        self,
        value: bool,
    ) -> bool:
        """
        a method

        Args:
            value (bool): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_bool_method(
            value,
        )
        return raw_return

    async def Int16Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_int16_method(
            value,
        )
        return raw_return

    async def Uint16Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint16_method(
            value,
        )
        return raw_return

    async def Int32Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_int32_method(
            value,
        )
        return raw_return

    async def Uint32Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint32_method(
            value,
        )
        return raw_return

    async def Int64Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_int64_method(
            value,
        )
        return raw_return

    async def Uint64Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint64_method(
            value,
        )
        return raw_return

    async def DoubleMethod(
        self,
        value: float,
    ) -> float:
        """
        a method

        Args:
            value (float): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_double_method(
            value,
        )
        return raw_return

    async def StringMethod(
        self,
        value: str,
    ) -> str:
        """
        a method

        Args:
            value (str): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_string_method(
            value,
        )
        return raw_return
