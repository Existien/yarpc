# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/02.2_primitives.yml
#   Object: Primitives
#   Template: py/service.j2

from typing import Protocol, List, Dict
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from copy import deepcopy
from enum import Enum



class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for Primitives

    Args:
        wrapper(PrimitivesInterface): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.testservice.primitives")
        self.object_path = "/com/yarpc/testservice/withArgs"
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


class PrimitivesInterface():
    """
    A interface using all builtin primitive types
    """

    def __init__(
        self,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path

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

    def emit_properties_changed(self, changed_properties: dict) -> None:
        """Informs clients about changed properties

        Args:
            changed_properties (dict): A dictionary containing all changed properties with their new values
        """
        if not changed_properties: return

        def marshal(data):
            if isinstance(data, dict):
                new_data = {}
                for key in data.keys():
                    new_data[key.value if isinstance(key, Enum) else key] = marshal(data[key])
                return new_data
            elif isinstance(data, list):
                for i in range(0, len(data)):
                    data[i] = marshal(data[i])
                return data
            elif isinstance(data, Enum):
                return data.value
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

    def on_Uint8Method(self, handler) -> None:
        """
        Set handler for Uint8Method method

        Args:
            handler (Callable[[int], Awaitable[int]]): the method handler
        """
        self._Uint8Method_handler = handler

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
        if self._Uint8Method_handler is None:
            raise NotImplementedError()

        return await self._Uint8Method_handler(
            value,
        )

    def on_BoolMethod(self, handler) -> None:
        """
        Set handler for BoolMethod method

        Args:
            handler (Callable[[bool], Awaitable[bool]]): the method handler
        """
        self._BoolMethod_handler = handler

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
        if self._BoolMethod_handler is None:
            raise NotImplementedError()

        return await self._BoolMethod_handler(
            value,
        )

    def on_Int16Method(self, handler) -> None:
        """
        Set handler for Int16Method method

        Args:
            handler (Callable[[int], Awaitable[int]]): the method handler
        """
        self._Int16Method_handler = handler

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
        if self._Int16Method_handler is None:
            raise NotImplementedError()

        return await self._Int16Method_handler(
            value,
        )

    def on_Uint16Method(self, handler) -> None:
        """
        Set handler for Uint16Method method

        Args:
            handler (Callable[[int], Awaitable[int]]): the method handler
        """
        self._Uint16Method_handler = handler

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
        if self._Uint16Method_handler is None:
            raise NotImplementedError()

        return await self._Uint16Method_handler(
            value,
        )

    def on_Int32Method(self, handler) -> None:
        """
        Set handler for Int32Method method

        Args:
            handler (Callable[[int], Awaitable[int]]): the method handler
        """
        self._Int32Method_handler = handler

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
        if self._Int32Method_handler is None:
            raise NotImplementedError()

        return await self._Int32Method_handler(
            value,
        )

    def on_Uint32Method(self, handler) -> None:
        """
        Set handler for Uint32Method method

        Args:
            handler (Callable[[int], Awaitable[int]]): the method handler
        """
        self._Uint32Method_handler = handler

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
        if self._Uint32Method_handler is None:
            raise NotImplementedError()

        return await self._Uint32Method_handler(
            value,
        )

    def on_Int64Method(self, handler) -> None:
        """
        Set handler for Int64Method method

        Args:
            handler (Callable[[int], Awaitable[int]]): the method handler
        """
        self._Int64Method_handler = handler

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
        if self._Int64Method_handler is None:
            raise NotImplementedError()

        return await self._Int64Method_handler(
            value,
        )

    def on_Uint64Method(self, handler) -> None:
        """
        Set handler for Uint64Method method

        Args:
            handler (Callable[[int], Awaitable[int]]): the method handler
        """
        self._Uint64Method_handler = handler

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
        if self._Uint64Method_handler is None:
            raise NotImplementedError()

        return await self._Uint64Method_handler(
            value,
        )

    def on_DoubleMethod(self, handler) -> None:
        """
        Set handler for DoubleMethod method

        Args:
            handler (Callable[[float], Awaitable[float]]): the method handler
        """
        self._DoubleMethod_handler = handler

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
        if self._DoubleMethod_handler is None:
            raise NotImplementedError()

        return await self._DoubleMethod_handler(
            value,
        )

    def on_StringMethod(self, handler) -> None:
        """
        Set handler for StringMethod method

        Args:
            handler (Callable[[str], Awaitable[str]]): the method handler
        """
        self._StringMethod_handler = handler

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
        if self._StringMethod_handler is None:
            raise NotImplementedError()

        return await self._StringMethod_handler(
            value,
        )
