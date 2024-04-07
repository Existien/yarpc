# Generated by YARPC
# Version:  0.1.0+editable
# Definition:
#   File: /workspace/tests/definitions/05.4_dictionaries_keys.yml
#   Object: DictKeys
#   Template: py/client_mock.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
from unittest.mock import Mock
import sys
import asyncio
from .struct_dict import StructDict
from .simons_dict import SimonsDict


class DictKeysClientMock():
    """
    Mock client implementation of the DictKeys D-Bus interface

    The Mock instance can be accessed via the `mock` attribute.
    All received signals will be forwarded to the mock using keyword arguments.
    E.g.
    A received signal `Fooed('bar')`
    might result in the following call of the mock:
    `client.mock.Fooed(msg='bar')`
    """

    def __init__(self):
        self.name = "com.yarpc.testservice.dictKeys"
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
            value: 'a{ys}',
    ):
        self.mock.Uint8Signal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _BoolSignal_handler(
        self,
            value: 'a{bs}',
    ):
        self.mock.BoolSignal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _Int16Signal_handler(
        self,
            value: 'a{ns}',
    ):
        self.mock.Int16Signal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _Uint16Signal_handler(
        self,
            value: 'a{qs}',
    ):
        self.mock.Uint16Signal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _Int32Signal_handler(
        self,
            value: 'a{is}',
    ):
        self.mock.Int32Signal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _Uint32Signal_handler(
        self,
            value: 'a{us}',
    ):
        self.mock.Uint32Signal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _Int64Signal_handler(
        self,
            value: 'a{xs}',
    ):
        self.mock.Int64Signal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _Uint64Signal_handler(
        self,
            value: 'a{ts}',
    ):
        self.mock.Uint64Signal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _DoubleSignal_handler(
        self,
            value: 'a{ds}',
    ):
        self.mock.DoubleSignal(
            { k0: v0 for k0, v0 in value.items() },
        )

    def _StringSignal_handler(
        self,
            value: 'a{ss}',
    ):
        self.mock.StringSignal(
            { k0: v0 for k0, v0 in value.items() },
        )

    async def Uint8Method(
        self,
        value: Dict[int, str],
    ) -> Dict[int, str]:
        """
        a method

        Args:
            value (Dict[int, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint8_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def BoolMethod(
        self,
        value: Dict[bool, str],
    ) -> Dict[bool, str]:
        """
        a method

        Args:
            value (Dict[bool, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_bool_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def Int16Method(
        self,
        value: Dict[int, str],
    ) -> Dict[int, str]:
        """
        a method

        Args:
            value (Dict[int, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_int16_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def Uint16Method(
        self,
        value: Dict[int, str],
    ) -> Dict[int, str]:
        """
        a method

        Args:
            value (Dict[int, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint16_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def Int32Method(
        self,
        value: Dict[int, str],
    ) -> Dict[int, str]:
        """
        a method

        Args:
            value (Dict[int, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_int32_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def Uint32Method(
        self,
        value: Dict[int, str],
    ) -> Dict[int, str]:
        """
        a method

        Args:
            value (Dict[int, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint32_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def Int64Method(
        self,
        value: Dict[int, str],
    ) -> Dict[int, str]:
        """
        a method

        Args:
            value (Dict[int, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_int64_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def Uint64Method(
        self,
        value: Dict[int, str],
    ) -> Dict[int, str]:
        """
        a method

        Args:
            value (Dict[int, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_uint64_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def DoubleMethod(
        self,
        value: Dict[float, str],
    ) -> Dict[float, str]:
        """
        a method

        Args:
            value (Dict[float, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_double_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    async def StringMethod(
        self,
        value: Dict[str, str],
    ) -> Dict[str, str]:
        """
        a method

        Args:
            value (Dict[str, str]): the value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_string_method(
            { k0: v0 for k0, v0 in value.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }
