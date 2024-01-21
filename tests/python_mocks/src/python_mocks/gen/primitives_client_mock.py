# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/primitives.yml
#   Object: Primitives
#   Template: client_mock

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
        self._interface = None
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
                "com.yarpc.testservice.primitives"
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
            await bus.wait_for_disconnect()
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)

    def _Uint8Signal_handler(
        self,
            value: int,
    ):
        self.mock.Uint8Signal(
            value,
        )

    def _BoolSignal_handler(
        self,
            value: bool,
    ):
        self.mock.BoolSignal(
            value,
        )

    def _Int16Signal_handler(
        self,
            value: int,
    ):
        self.mock.Int16Signal(
            value,
        )

    def _Uint16Signal_handler(
        self,
            value: int,
    ):
        self.mock.Uint16Signal(
            value,
        )

    def _Int32Signal_handler(
        self,
            value: int,
    ):
        self.mock.Int32Signal(
            value,
        )

    def _Uint32Signal_handler(
        self,
            value: int,
    ):
        self.mock.Uint32Signal(
            value,
        )

    def _Int64Signal_handler(
        self,
            value: int,
    ):
        self.mock.Int64Signal(
            value,
        )

    def _Uint64Signal_handler(
        self,
            value: int,
    ):
        self.mock.Uint64Signal(
            value,
        )

    def _DoubleSignal_handler(
        self,
            value: float,
    ):
        self.mock.DoubleSignal(
            value,
        )

    def _StringSignal_handler(
        self,
            value: str,
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
        return await self._interface.call_uint8_method(
            value,
        )

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
        return await self._interface.call_bool_method(
            value,
        )

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
        return await self._interface.call_int16_method(
            value,
        )

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
        return await self._interface.call_uint16_method(
            value,
        )

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
        return await self._interface.call_int32_method(
            value,
        )

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
        return await self._interface.call_uint32_method(
            value,
        )

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
        return await self._interface.call_int64_method(
            value,
        )

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
        return await self._interface.call_uint64_method(
            value,
        )

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
        return await self._interface.call_double_method(
            value,
        )

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
        return await self._interface.call_string_method(
            value,
        )
