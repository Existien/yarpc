# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/02.1_with_args.yml
#   Object: WithArgs
#   Template: py/service_mock.j2

from typing import Sequence, Mapping
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
from copy import deepcopy


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for WithArgs

    Args:
        wrapper(BackendWithArgsInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.withArgs")
        self.object_path = "/com/yarpc/backend"
        self._wrapper = wrapper

    @signal()
    def Notified(
        self,
        message: 's',
    ) -> 's':
        return message

    @signal()
    def OrderReceived(
        self,
        item: 's',
        amount: 'u',
        pricePerItem: 'd',
    ) -> 'sud':
        return [
            item,
            amount,
            pricePerItem,
        ]

    @method()
    async def Notify(
        self,
        message: 's',
    ) -> None:
        await self._wrapper.Notify(
            message,
        )
        return None

    @method()
    async def Order(
        self,
        item: 's',
        amount: 'u',
        pricePerItem: 'd',
    ) -> 'd':
        raw_return = await self._wrapper.Order(
            item,
            amount,
            pricePerItem,
        )
        return raw_return

    @dbus_property(access=PropertyAccess.READWRITE)
    async def Speed(self) -> 'd':
        unmarshalled = await self._wrapper.get_Speed()
        return unmarshalled

    @Speed.setter
    async def Speed(self, value: 'd'):
        unmarshalled = value
        await self._wrapper.set_Speed(unmarshalled)

    @dbus_property(access=PropertyAccess.READWRITE)
    async def Distance(self) -> 'u':
        unmarshalled = await self._wrapper.get_Distance()
        return unmarshalled

    @Distance.setter
    async def Distance(self, value: 'u'):
        unmarshalled = value
        await self._wrapper.set_Distance(unmarshalled)

    @dbus_property(access=PropertyAccess.READ)
    async def Duration(self) -> 'd':
        unmarshalled = await self._wrapper.get_Duration()
        return unmarshalled


class BackendWithArgsInterfaceMock():
    """
    Mock service implementation of the WithArgs D-Bus interface.

    The AsyncMock instance can be accessed via the `mock` attribute.
    All method calls will be forwarded to the mock using keyword arguments.
    E.g.
    `await service.Foo('bar')`
    might result in the following await of the mock:
    `await service.mock.Foo(msg='bar')`

    Setting properties will trigger a on_<property>_changed call to the mock with
    the new value and a dictionary with the current properties as arguments. The mock is expected to return
    an updated dictionary of properties.

    Per default, the mock is configured to just return the updated value.

    Args:
        Speed (float): the speed
            in m/s

        Distance (int): the distance to travel in m
        Duration (float): the time until the distance is covered at the current speed
    """

    def __init__(
        self,
        Speed: float,
        Distance: int,
        Duration: float,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.Notify.return_value = None
        self.mock.Order.return_value = None

        self._properties = {}
        self._properties["Speed"] = Speed
        self._Speed_change_handler = BackendWithArgsInterfaceMock._default_Speed_change_handler
        self.mock.on_Speed_changed = AsyncMock(wraps=self._Speed_change_handler)
        self._properties["Distance"] = Distance
        self._Distance_change_handler = BackendWithArgsInterfaceMock._default_Distance_change_handler
        self.mock.on_Distance_changed = AsyncMock(wraps=self._Distance_change_handler)
        self._properties["Duration"] = Duration
        self._Duration_change_handler = BackendWithArgsInterfaceMock._default_Duration_change_handler
        self.mock.on_Duration_changed = AsyncMock(wraps=self._Duration_change_handler)

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

    def Notified(
        self,
        message: str,
    ) -> None:
        """
        a simple signal with one argument

        Args:
            message (str): The message
        """
        self.interface.Notified(
            message,
        )

    def OrderReceived(
        self,
        item: str,
        amount: int,
        pricePerItem: float,
    ) -> None:
        """
        a simple signal with
        multiple arguments


        Args:
            item (str): The item
            amount (int): a amount
            ordered

            pricePerItem (float): the price per item
        """
        self.interface.OrderReceived(
            item,
            amount,
            pricePerItem,
        )

    async def Notify(
        self,
        message: str,
    ) -> None:
        """
        a simple method with one argument

        Args:
            message (str): The message
        """
        return await self._await_mock_method("Notify", locals())

    async def Order(
        self,
        item: str,
        amount: int,
        pricePerItem: float,
    ) -> float:
        """
        a simple method
        with args and return value


        Args:
            item (str): The
                item

            amount (int): a amount ordered
            pricePerItem (float): the price per item

        Returns:
            float: the
                total price

        """
        return await self._await_mock_method("Order", locals())

    async def get_Speed(self) -> float:
        """Getter for property Speed

        the speed
        in m/s


        Returns:
            float: the current value
        """
        return self._properties["Speed"]

    def on_Speed_changed(self, handler) -> None:
        """
        Set handler for property changes due to Speed changes

        The handler takes the new Speed value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[float, dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._Speed_change_handler = handler
        self.mock.on_Speed_changed = AsyncMock(wraps=self._Speed_change_handler)

    async def _default_Speed_change_handler(value: float, _: dict) -> dict:
        return { "Speed": value }

    async def set_Speed(self, value: float):
        """Setter for property Speed

        the speed
        in m/s


        Args:
            value (float): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_Speed_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)

    async def get_Distance(self) -> int:
        """Getter for property Distance

        the distance to travel in m

        Returns:
            int: the current value
        """
        return self._properties["Distance"]

    def on_Distance_changed(self, handler) -> None:
        """
        Set handler for property changes due to Distance changes

        The handler takes the new Distance value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[int, dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._Distance_change_handler = handler
        self.mock.on_Distance_changed = AsyncMock(wraps=self._Distance_change_handler)

    async def _default_Distance_change_handler(value: int, _: dict) -> dict:
        return { "Distance": value }

    async def set_Distance(self, value: int):
        """Setter for property Distance

        the distance to travel in m

        Args:
            value (int): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_Distance_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)

    async def get_Duration(self) -> float:
        """Getter for property Duration

        the time until the distance is covered at the current speed

        Returns:
            float: the current value
        """
        return self._properties["Duration"]

    def on_Duration_changed(self, handler) -> None:
        """
        Set handler for property changes due to Duration changes

        The handler takes the new Duration value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[float, dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._Duration_change_handler = handler
        self.mock.on_Duration_changed = AsyncMock(wraps=self._Duration_change_handler)

    async def _default_Duration_change_handler(value: float, _: dict) -> dict:
        return { "Duration": value }

    async def set_Duration(self, value: float):
        """Setter for property Duration

        the time until the distance is covered at the current speed

        Args:
            value (float): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_Duration_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)
