# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/05.2_dictionaries_with_structs.yml
#   Object: DictsWithStructs
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
from .struct_dict import StructDict
from .simons_dict import SimonsDict


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for DictsWithStructs

    Args:
        wrapper(BackendDictsWithStructsInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.dictsWithStructs")
        self.object_path = "/com/yarpc/backend"
        self._wrapper = wrapper

    @method()
    async def DictsStructMethod(
        self,
        numbers: 'a{s(a{sa{su}})}',
    ) -> 'a{s(a{s(a{sa{su}})})}':
        raw_return = await self._wrapper.DictsStructMethod(
            { k0: StructDict.from_dbus(v0) for k0, v0 in numbers.items() },
        )
        return { k0: v0.to_dbus() for k0, v0 in raw_return.items() }

    @signal()
    def DictStructSignal(
        self,
        numbers: 'a{s(a{sa{su}})}',
    ) -> 'a{s(a{sa{su}})}':
        return numbers

    @dbus_property(access=PropertyAccess.READWRITE)
    async def DictStructProperty(self) -> 'a{s(a{sa{su}})}':
        unmarshalled = await self._wrapper.get_DictStructProperty()
        return { k0: v0.to_dbus() for k0, v0 in unmarshalled.items() }

    @DictStructProperty.setter
    async def DictStructProperty(self, value: 'a{s(a{sa{su}})}'):
        unmarshalled = { k0: StructDict.from_dbus(v0) for k0, v0 in value.items() }
        await self._wrapper.set_DictStructProperty(unmarshalled)


class BackendDictsWithStructsInterfaceMock():
    """
    Mock service implementation of the DictsWithStructs D-Bus interface.

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
        DictStructProperty (Dict[str, StructDict]): a simple property
    """

    def __init__(
        self,
        DictStructProperty: Dict[str, StructDict],
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.DictsStructMethod.return_value = None

        self._properties = {}
        self._properties["DictStructProperty"] = DictStructProperty
        self._DictStructProperty_change_handler = BackendDictsWithStructsInterfaceMock._default_DictStructProperty_change_handler
        self.mock.on_DictStructProperty_changed = AsyncMock(wraps=self._DictStructProperty_change_handler)

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

    async def DictsStructMethod(
        self,
        numbers: Dict[str, StructDict],
    ) -> Dict[str, SimonsDict]:
        """
        a simple method with one argument

        Args:
            numbers (Dict[str, StructDict]): Some numbers

        Returns:
            Dict[str, SimonsDict]: more numbers
        """
        return await self._await_mock_method("DictsStructMethod", locals())

    def DictStructSignal(
        self,
        numbers: Dict[str, StructDict],
    ) -> None:
        """
        a simple signal with one argument

        Args:
            numbers (Dict[str, StructDict]): numbers
        """
        self.interface.DictStructSignal(
            { k0: v0.to_dbus() for k0, v0 in numbers.items() },
        )

    async def get_DictStructProperty(self) -> Dict[str, StructDict]:
        """Getter for property DictStructProperty

        a simple property

        Returns:
            Dict[str, StructDict]: the current value
        """
        return self._properties["DictStructProperty"]

    def on_DictStructProperty_changed(self, handler) -> None:
        """
        Set handler for property changes due to DictStructProperty changes

        The handler takes the new DictStructProperty value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[Dict[str, StructDict], dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._DictStructProperty_change_handler = handler
        self.mock.on_DictStructProperty_changed = AsyncMock(wraps=self._DictStructProperty_change_handler)

    async def _default_DictStructProperty_change_handler(value: Dict[str, StructDict], _: dict) -> dict:
        return { "DictStructProperty": value }

    async def set_DictStructProperty(self, value: Dict[str, StructDict]):
        """Setter for property DictStructProperty

        a simple property

        Args:
            value (Dict[str, StructDict]): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_DictStructProperty_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)
