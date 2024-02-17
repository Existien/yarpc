# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/02.2_primitives.yml
#   Object: Primitives
#   Template: py/service_mock.j2

from typing import Sequence
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
from copy import deepcopy


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for Primitives

    Args:
        wrapper(BackendPrimitivesInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.primitives")
        self.object_path = "/com/yarpc/backend"
        self._wrapper = wrapper

    @signal()
    def Uint8Signal(
        self,
        value: 'y',
    ) -> 'y':
        return value

    @signal()
    def BoolSignal(
        self,
        value: 'b',
    ) -> 'b':
        return value

    @signal()
    def Int16Signal(
        self,
        value: 'n',
    ) -> 'n':
        return value

    @signal()
    def Uint16Signal(
        self,
        value: 'q',
    ) -> 'q':
        return value

    @signal()
    def Int32Signal(
        self,
        value: 'i',
    ) -> 'i':
        return value

    @signal()
    def Uint32Signal(
        self,
        value: 'u',
    ) -> 'u':
        return value

    @signal()
    def Int64Signal(
        self,
        value: 'x',
    ) -> 'x':
        return value

    @signal()
    def Uint64Signal(
        self,
        value: 't',
    ) -> 't':
        return value

    @signal()
    def DoubleSignal(
        self,
        value: 'd',
    ) -> 'd':
        return value

    @signal()
    def StringSignal(
        self,
        value: 's',
    ) -> 's':
        return value

    @method()
    async def Uint8Method(
        self,
        value: 'y',
    ) -> 'y':
        raw_return = await self._wrapper.Uint8Method(
            value,
        )
        return raw_return

    @method()
    async def BoolMethod(
        self,
        value: 'b',
    ) -> 'b':
        raw_return = await self._wrapper.BoolMethod(
            value,
        )
        return raw_return

    @method()
    async def Int16Method(
        self,
        value: 'n',
    ) -> 'n':
        raw_return = await self._wrapper.Int16Method(
            value,
        )
        return raw_return

    @method()
    async def Uint16Method(
        self,
        value: 'q',
    ) -> 'q':
        raw_return = await self._wrapper.Uint16Method(
            value,
        )
        return raw_return

    @method()
    async def Int32Method(
        self,
        value: 'i',
    ) -> 'i':
        raw_return = await self._wrapper.Int32Method(
            value,
        )
        return raw_return

    @method()
    async def Uint32Method(
        self,
        value: 'u',
    ) -> 'u':
        raw_return = await self._wrapper.Uint32Method(
            value,
        )
        return raw_return

    @method()
    async def Int64Method(
        self,
        value: 'x',
    ) -> 'x':
        raw_return = await self._wrapper.Int64Method(
            value,
        )
        return raw_return

    @method()
    async def Uint64Method(
        self,
        value: 't',
    ) -> 't':
        raw_return = await self._wrapper.Uint64Method(
            value,
        )
        return raw_return

    @method()
    async def DoubleMethod(
        self,
        value: 'd',
    ) -> 'd':
        raw_return = await self._wrapper.DoubleMethod(
            value,
        )
        return raw_return

    @method()
    async def StringMethod(
        self,
        value: 's',
    ) -> 's':
        raw_return = await self._wrapper.StringMethod(
            value,
        )
        return raw_return


class BackendPrimitivesInterfaceMock():
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
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

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

    def emit_properties_changed(self, changed_properties: dict) -> None:
        """Informs clients about changed properties

        Args:
            changed_properties (dict): A dictionary containing all changed properties with their new values
        """
        if not changed_properties: return

        def marshal(data):
            if isinstance(data, dict):
                for key in data.keys():
                    data[key] = marshal(data[key])
                return data
            elif isinstance(data, list):
                for i in range(0, len(data)):
                    data[i] = marshal(data[i])
                return data
            elif hasattr(data, 'to_dbus'):
                return data.to_dbus()
            else:
                return data
        marshalled = marshal(deepcopy(changed_properties))
        self.interface.emit_properties_changed(marshalled)

    def Uint8Signal(
        self,
        value: int,
    ) -> None:
        """
        a signal

        Args:
            value (int): the value
        """
        self.interface.Uint8Signal(
            value,
        )

    def BoolSignal(
        self,
        value: bool,
    ) -> None:
        """
        a signal

        Args:
            value (bool): the value
        """
        self.interface.BoolSignal(
            value,
        )

    def Int16Signal(
        self,
        value: int,
    ) -> None:
        """
        a signal

        Args:
            value (int): the value
        """
        self.interface.Int16Signal(
            value,
        )

    def Uint16Signal(
        self,
        value: int,
    ) -> None:
        """
        a signal

        Args:
            value (int): the value
        """
        self.interface.Uint16Signal(
            value,
        )

    def Int32Signal(
        self,
        value: int,
    ) -> None:
        """
        a signal

        Args:
            value (int): the value
        """
        self.interface.Int32Signal(
            value,
        )

    def Uint32Signal(
        self,
        value: int,
    ) -> None:
        """
        a signal

        Args:
            value (int): the value
        """
        self.interface.Uint32Signal(
            value,
        )

    def Int64Signal(
        self,
        value: int,
    ) -> None:
        """
        a signal

        Args:
            value (int): the value
        """
        self.interface.Int64Signal(
            value,
        )

    def Uint64Signal(
        self,
        value: int,
    ) -> None:
        """
        a signal

        Args:
            value (int): the value
        """
        self.interface.Uint64Signal(
            value,
        )

    def DoubleSignal(
        self,
        value: float,
    ) -> None:
        """
        a signal

        Args:
            value (float): the value
        """
        self.interface.DoubleSignal(
            value,
        )

    def StringSignal(
        self,
        value: str,
    ) -> None:
        """
        a signal

        Args:
            value (str): the value
        """
        self.interface.StringSignal(
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

        Returns:
            int: the return type
        """
        return await self._await_mock_method("Uint8Method", locals())

    async def BoolMethod(
        self,
        value: bool,
    ) -> bool:
        """
        a method

        Args:
            value (bool): the value

        Returns:
            bool: the return type
        """
        return await self._await_mock_method("BoolMethod", locals())

    async def Int16Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        return await self._await_mock_method("Int16Method", locals())

    async def Uint16Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        return await self._await_mock_method("Uint16Method", locals())

    async def Int32Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        return await self._await_mock_method("Int32Method", locals())

    async def Uint32Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        return await self._await_mock_method("Uint32Method", locals())

    async def Int64Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        return await self._await_mock_method("Int64Method", locals())

    async def Uint64Method(
        self,
        value: int,
    ) -> int:
        """
        a method

        Args:
            value (int): the value

        Returns:
            int: the return type
        """
        return await self._await_mock_method("Uint64Method", locals())

    async def DoubleMethod(
        self,
        value: float,
    ) -> float:
        """
        a method

        Args:
            value (float): the value

        Returns:
            float: the return type
        """
        return await self._await_mock_method("DoubleMethod", locals())

    async def StringMethod(
        self,
        value: str,
    ) -> str:
        """
        a method

        Args:
            value (str): the value

        Returns:
            str: the return type
        """
        return await self._await_mock_method("StringMethod", locals())
