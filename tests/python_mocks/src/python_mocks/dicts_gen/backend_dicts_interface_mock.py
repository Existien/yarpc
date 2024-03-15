# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/05.1_dictionaries.yml
#   Object: Dicts
#   Template: py/service_mock.j2

from typing import Sequence, Mapping
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
from copy import deepcopy
from enum import Enum
from .struct_dict import StructDict
from .simons_dict import SimonsDict


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for Dicts

    Args:
        wrapper(BackendDictsInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.dicts")
        self.object_path = "/com/yarpc/backend"
        self._wrapper = wrapper

    @method()
    async def DictMethod(
        self,
        keysNValues: 'a{su}',
    ) -> 'a{ss}':
        raw_return = await self._wrapper.DictMethod(
            { k0: v0 for k0, v0 in keysNValues.items() },
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    @signal()
    def DictSignal(
        self,
        keysNValues: 'a{su}',
    ) -> 'a{su}':
        return keysNValues

    @dbus_property(access=PropertyAccess.READWRITE)
    async def DictProperty(self) -> 'a{su}':
        unmarshalled = await self._wrapper.get_DictProperty()
        return { k0: v0 for k0, v0 in unmarshalled.items() }

    @DictProperty.setter
    async def DictProperty(self, value: 'a{su}'):
        unmarshalled = { k0: v0 for k0, v0 in value.items() }
        await self._wrapper.set_DictProperty(unmarshalled)


class BackendDictsInterfaceMock():
    """
    Mock service implementation of the Dicts D-Bus interface.

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
        DictProperty (Mapping[str, int]): a prop
    """

    def __init__(
        self,
        DictProperty: Mapping[str, int],
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.DictMethod.return_value = None

        self._properties = {}
        self._properties["DictProperty"] = DictProperty
        self._DictProperty_change_handler = BackendDictsInterfaceMock._default_DictProperty_change_handler
        self.mock.on_DictProperty_changed = AsyncMock(wraps=self._DictProperty_change_handler)

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

    async def DictMethod(
        self,
        keysNValues: Mapping[str, int],
    ) -> Mapping[str, str]:
        """
        a simple method with one argument

        Args:
            keysNValues (Mapping[str, int]): a dictionary

        Returns:
            Mapping[str, str]: another one
        """
        return await self._await_mock_method("DictMethod", locals())

    def DictSignal(
        self,
        keysNValues: Mapping[str, int],
    ) -> None:
        """
        a signal

        Args:
            keysNValues (Mapping[str, int]): a dictionary
        """
        self.interface.DictSignal(
            { k0: v0 for k0, v0 in keysNValues.items() },
        )

    async def get_DictProperty(self) -> Mapping[str, int]:
        """Getter for property DictProperty

        a prop

        Returns:
            Mapping[str, int]: the current value
        """
        return self._properties["DictProperty"]

    def on_DictProperty_changed(self, handler) -> None:
        """
        Set handler for property changes due to DictProperty changes

        The handler takes the new DictProperty value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[Mapping[str, int], dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._DictProperty_change_handler = handler
        self.mock.on_DictProperty_changed = AsyncMock(wraps=self._DictProperty_change_handler)

    async def _default_DictProperty_change_handler(value: Mapping[str, int], _: dict) -> dict:
        return { "DictProperty": value }

    async def set_DictProperty(self, value: Mapping[str, int]):
        """Setter for property DictProperty

        a prop

        Args:
            value (Mapping[str, int]): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_DictProperty_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)
