# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/primitives.yml
#   Object: Primitives
#   Template: service_mock

from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
from copy import deepcopy
import asyncio

class BackendPrimitivesInterfaceMock(ServiceInterface):
    """
    Mock service implementation of the Primitives D-Bus interface.

    The AsyncMock instance can be accessed via the `mock` attribute.
    All method calls will be forwarded to the mock using keyword arguments.
    E.g.
    `await service.Foo('bar')`
    might result in the following await of the mock:
    `await service.mock.Foo(msg='bar')`
    """

    def __init__(
        self,
    ):
        super().__init__("com.yarpc.backend.primitives")
        self.mock = AsyncMock()
        self.object_path = "/com/yarpc/backend"

        self.mock.Uint8Method.return_value = None
        self.mock.BoolMethod.return_value = None
        self.mock.Int16Method.return_value = None
        self.mock.Uint16Method.return_value = None
        self.mock.Int32Method.return_value = None
        self.mock.Uint32Method.return_value = None
        self.mock.Int64Method.return_value = None
        self.mock.Uint64Method.return_value = None
        self.mock.DoubleMethod.return_value = None
        self.mock.StringMethod.return_value = None

        self._properties = {}

    async def _await_mock_method(self, method, local_variables):
        kwargs = dict(filter(lambda kv: kv[0] != 'self', local_variables.items()))
        return await getattr(self.mock, method)(**kwargs)

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
        return await self._await_mock_method("Uint8Method", locals())
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
        return await self._await_mock_method("BoolMethod", locals())
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
        return await self._await_mock_method("Int16Method", locals())
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
        return await self._await_mock_method("Uint16Method", locals())
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
        return await self._await_mock_method("Int32Method", locals())
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
        return await self._await_mock_method("Uint32Method", locals())
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
        return await self._await_mock_method("Int64Method", locals())
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
        return await self._await_mock_method("Uint64Method", locals())
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
        return await self._await_mock_method("DoubleMethod", locals())
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
        return await self._await_mock_method("StringMethod", locals())