# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/primitives.yml
#   Object: Primitives
#   Template: service

from typing import Protocol
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from copy import deepcopy
import asyncio


class PrimitivesInterface(ServiceInterface):
    """
    A interface using all builtin primitive types
    """

    def __init__(
        self,
    ):
        super().__init__("com.yarpc.testservice.primitives")
        self.object_path = "/com/yarpc/testservice"

        self._Uint8Method_handler = None
        self._BoolMethod_handler = None
        self._Int16Method_handler = None
        self._Uint16Method_handler = None
        self._Int32Method_handler = None
        self._Uint32Method_handler = None
        self._Int64Method_handler = None
        self._Uint64Method_handler = None
        self._DoubleMethod_handler = None
        self._StringMethod_handler = None

    @signal()
    def Uint8Signal(
        self,
        value: int,
    ) -> 'y':
        """
        a signal

        Args:
            value (int): the value
        """
        return value

    @signal()
    def BoolSignal(
        self,
        value: bool,
    ) -> 'b':
        """
        a signal

        Args:
            value (bool): the value
        """
        return value

    @signal()
    def Int16Signal(
        self,
        value: int,
    ) -> 'n':
        """
        a signal

        Args:
            value (int): the value
        """
        return value

    @signal()
    def Uint16Signal(
        self,
        value: int,
    ) -> 'q':
        """
        a signal

        Args:
            value (int): the value
        """
        return value

    @signal()
    def Int32Signal(
        self,
        value: int,
    ) -> 'i':
        """
        a signal

        Args:
            value (int): the value
        """
        return value

    @signal()
    def Uint32Signal(
        self,
        value: int,
    ) -> 'u':
        """
        a signal

        Args:
            value (int): the value
        """
        return value

    @signal()
    def Int64Signal(
        self,
        value: int,
    ) -> 'x':
        """
        a signal

        Args:
            value (int): the value
        """
        return value

    @signal()
    def Uint64Signal(
        self,
        value: int,
    ) -> 't':
        """
        a signal

        Args:
            value (int): the value
        """
        return value

    @signal()
    def DoubleSignal(
        self,
        value: float,
    ) -> 'd':
        """
        a signal

        Args:
            value (float): the value
        """
        return value

    @signal()
    def StringSignal(
        self,
        value: str,
    ) -> 's':
        """
        a signal

        Args:
            value (str): the value
        """
        return value


    def on_Uint8Method(self, handler) -> None:
        """
        Set handler for Uint8Method method

        Args:
            handler (Callable[[int], Awaitable[None]]): the method handler
        """
        self._Uint8Method_handler = handler

    @method()
    async def Uint8Method(
        self,
        value: 'y',
    ) -> 'y':
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        if self._Uint8Method_handler is None:
            raise NotImplementedError()

        return await self._Uint8Method_handler(
            value,
        )

    def on_BoolMethod(self, handler) -> None:
        """
        Set handler for BoolMethod method

        Args:
            handler (Callable[[bool], Awaitable[None]]): the method handler
        """
        self._BoolMethod_handler = handler

    @method()
    async def BoolMethod(
        self,
        value: 'b',
    ) -> 'b':
        """
        a method

        Args:
            value (bool): the value

        Returns:
            bool: the return type
        """
        if self._BoolMethod_handler is None:
            raise NotImplementedError()

        return await self._BoolMethod_handler(
            value,
        )

    def on_Int16Method(self, handler) -> None:
        """
        Set handler for Int16Method method

        Args:
            handler (Callable[[int], Awaitable[None]]): the method handler
        """
        self._Int16Method_handler = handler

    @method()
    async def Int16Method(
        self,
        value: 'n',
    ) -> 'n':
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        if self._Int16Method_handler is None:
            raise NotImplementedError()

        return await self._Int16Method_handler(
            value,
        )

    def on_Uint16Method(self, handler) -> None:
        """
        Set handler for Uint16Method method

        Args:
            handler (Callable[[int], Awaitable[None]]): the method handler
        """
        self._Uint16Method_handler = handler

    @method()
    async def Uint16Method(
        self,
        value: 'q',
    ) -> 'q':
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        if self._Uint16Method_handler is None:
            raise NotImplementedError()

        return await self._Uint16Method_handler(
            value,
        )

    def on_Int32Method(self, handler) -> None:
        """
        Set handler for Int32Method method

        Args:
            handler (Callable[[int], Awaitable[None]]): the method handler
        """
        self._Int32Method_handler = handler

    @method()
    async def Int32Method(
        self,
        value: 'i',
    ) -> 'i':
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        if self._Int32Method_handler is None:
            raise NotImplementedError()

        return await self._Int32Method_handler(
            value,
        )

    def on_Uint32Method(self, handler) -> None:
        """
        Set handler for Uint32Method method

        Args:
            handler (Callable[[int], Awaitable[None]]): the method handler
        """
        self._Uint32Method_handler = handler

    @method()
    async def Uint32Method(
        self,
        value: 'u',
    ) -> 'u':
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        if self._Uint32Method_handler is None:
            raise NotImplementedError()

        return await self._Uint32Method_handler(
            value,
        )

    def on_Int64Method(self, handler) -> None:
        """
        Set handler for Int64Method method

        Args:
            handler (Callable[[int], Awaitable[None]]): the method handler
        """
        self._Int64Method_handler = handler

    @method()
    async def Int64Method(
        self,
        value: 'x',
    ) -> 'x':
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        if self._Int64Method_handler is None:
            raise NotImplementedError()

        return await self._Int64Method_handler(
            value,
        )

    def on_Uint64Method(self, handler) -> None:
        """
        Set handler for Uint64Method method

        Args:
            handler (Callable[[int], Awaitable[None]]): the method handler
        """
        self._Uint64Method_handler = handler

    @method()
    async def Uint64Method(
        self,
        value: 't',
    ) -> 't':
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        if self._Uint64Method_handler is None:
            raise NotImplementedError()

        return await self._Uint64Method_handler(
            value,
        )

    def on_DoubleMethod(self, handler) -> None:
        """
        Set handler for DoubleMethod method

        Args:
            handler (Callable[[float], Awaitable[None]]): the method handler
        """
        self._DoubleMethod_handler = handler

    @method()
    async def DoubleMethod(
        self,
        value: 'd',
    ) -> 'd':
        """
        a method

        Args:
            value (float): the value

        Returns:
            float: the return type
        """
        if self._DoubleMethod_handler is None:
            raise NotImplementedError()

        return await self._DoubleMethod_handler(
            value,
        )

    def on_StringMethod(self, handler) -> None:
        """
        Set handler for StringMethod method

        Args:
            handler (Callable[[str], Awaitable[None]]): the method handler
        """
        self._StringMethod_handler = handler

    @method()
    async def StringMethod(
        self,
        value: 's',
    ) -> 's':
        """
        a method

        Args:
            value (str): the value

        Returns:
            str: the return type
        """
        if self._StringMethod_handler is None:
            raise NotImplementedError()

        return await self._StringMethod_handler(
            value,
        )