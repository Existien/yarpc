# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/03_structs.yml
#   Object: Structs
#   Template: py/service_mock.j2

from typing import List, Dict
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
from copy import deepcopy
from enum import Enum
from .simple_struct import SimpleStruct
from .item import Item


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for Structs

    Args:
        wrapper(BackendStructsInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.structs")
        self.object_path = "/com/yarpc/backend"
        self._wrapper = wrapper

    @method()
    async def SendStruct(
        self,
        simpleStruct: '((sd)u)',
    ) -> '((sd)u)':
        raw_return = await self._wrapper.SendStruct(
            SimpleStruct.from_dbus(simpleStruct),
        )
        return raw_return.to_dbus()

    @signal()
    def StructReceived(
        self,
        simpleStruct: '((sd)u)',
        totalCosts: 'd',
    ) -> '((sd)u)d':
        return [
            simpleStruct,
            totalCosts,
        ]

    @dbus_property(access=PropertyAccess.READWRITE)
    async def Simple(self) -> '((sd)u)':
        unmarshalled = await self._wrapper.get_Simple()
        return unmarshalled.to_dbus()

    @Simple.setter
    async def Simple(self, value: '((sd)u)'):
        unmarshalled = SimpleStruct.from_dbus(value)
        await self._wrapper.set_Simple(unmarshalled)


class BackendStructsInterfaceMock():
    """
    Mock service implementation of the Structs D-Bus interface.

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
        Simple (SimpleStruct): a property for a simple struct
    """

    def __init__(
        self,
        Simple: SimpleStruct,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.SendStruct.return_value = None

        self._properties = {}
        self._properties["Simple"] = Simple
        self._Simple_change_handler = BackendStructsInterfaceMock._default_Simple_change_handler
        self.mock.on_Simple_changed = AsyncMock(wraps=self._Simple_change_handler)

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

    async def SendStruct(
        self,
        simpleStruct: SimpleStruct,
    ) -> SimpleStruct:
        """
        a method with a struct as args

        Args:
            simpleStruct (SimpleStruct): the SimpleStruct to send

        Returns:
            SimpleStruct: the SimpleStruct
        """
        return await self._await_mock_method("SendStruct", locals())

    def StructReceived(
        self,
        simpleStruct: SimpleStruct,
        totalCosts: float,
    ) -> None:
        """
        a signal with a struct as args

        Args:
            simpleStruct (SimpleStruct): the SimpleStruct
            totalCosts (float): the total costs
        """
        self.interface.StructReceived(
            simpleStruct.to_dbus(),
            totalCosts,
        )

    async def get_Simple(self) -> SimpleStruct:
        """Getter for property Simple

        a property for a simple struct

        Returns:
            SimpleStruct: the current value
        """
        return self._properties["Simple"]

    def on_Simple_changed(self, handler) -> None:
        """
        Set handler for property changes due to Simple changes

        The handler takes the new Simple value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[SimpleStruct, dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._Simple_change_handler = handler
        self.mock.on_Simple_changed = AsyncMock(wraps=self._Simple_change_handler)

    async def _default_Simple_change_handler(value: SimpleStruct, _: dict) -> dict:
        return { "Simple": value }

    async def set_Simple(self, value: SimpleStruct):
        """Setter for property Simple

        a property for a simple struct

        Args:
            value (SimpleStruct): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_Simple_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)
