# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/05.3_dictionaries_with_arrays.yml
#   Object: DictsWithArrays
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
    D-Bus interface implementation for DictsWithArrays

    Args:
        wrapper(BackendDictsWithArraysInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.dictsWithArrays")
        self.object_path = "/com/yarpc/backend/dicts"
        self._wrapper = wrapper

    @method()
    async def DictsArrayMethod(
        self,
        numbers: 'a{saa{su}}',
    ) -> 'a{saa{su}}':
        raw_return = await self._wrapper.DictsArrayMethod(
            { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in numbers.items() },
        )
        return { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in raw_return.items() }

    @signal()
    def DictsArraySignal(
        self,
        numbers: 'a{saa{su}}',
    ) -> 'a{saa{su}}':
        return numbers

    @dbus_property(access=PropertyAccess.READWRITE)
    async def DictArrayProperty(self) -> 'a{saa{su}}':
        unmarshalled = await self._wrapper.get_DictArrayProperty()
        return { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in unmarshalled.items() }

    @DictArrayProperty.setter
    async def DictArrayProperty(self, value: 'a{saa{su}}'):
        unmarshalled = { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in value.items() }
        await self._wrapper.set_DictArrayProperty(unmarshalled)


class BackendDictsWithArraysInterfaceMock():
    """
    Mock service implementation of the DictsWithArrays D-Bus interface.

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
        DictArrayProperty (Dict[str, List[Dict[str, int]]]): a simple property
    """

    def __init__(
        self,
        DictArrayProperty: Dict[str, List[Dict[str, int]]],
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.DictsArrayMethod.return_value = None

        self._properties = {}
        self._properties["DictArrayProperty"] = DictArrayProperty
        self._DictArrayProperty_change_handler = BackendDictsWithArraysInterfaceMock._default_DictArrayProperty_change_handler
        self.mock.on_DictArrayProperty_changed = AsyncMock(wraps=self._DictArrayProperty_change_handler)

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

    async def DictsArrayMethod(
        self,
        numbers: Dict[str, List[Dict[str, int]]],
    ) -> Dict[str, List[Dict[str, int]]]:
        """
        a simple method with one argument

        Args:
            numbers (Dict[str, List[Dict[str, int]]]): some numbers

        Returns:
            Dict[str, List[Dict[str, int]]]: some numbers
        """
        return await self._await_mock_method("DictsArrayMethod", locals())

    def DictsArraySignal(
        self,
        numbers: Dict[str, List[Dict[str, int]]],
    ) -> None:
        """
        a simple signal with one argument

        Args:
            numbers (Dict[str, List[Dict[str, int]]]): some numbers
        """
        self.interface.DictsArraySignal(
            { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in numbers.items() },
        )

    async def get_DictArrayProperty(self) -> Dict[str, List[Dict[str, int]]]:
        """Getter for property DictArrayProperty

        a simple property

        Returns:
            Dict[str, List[Dict[str, int]]]: the current value
        """
        return self._properties["DictArrayProperty"]

    def on_DictArrayProperty_changed(self, handler) -> None:
        """
        Set handler for property changes due to DictArrayProperty changes

        The handler takes the new DictArrayProperty value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[Dict[str, List[Dict[str, int]]], dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._DictArrayProperty_change_handler = handler
        self.mock.on_DictArrayProperty_changed = AsyncMock(wraps=self._DictArrayProperty_change_handler)

    async def _default_DictArrayProperty_change_handler(value: Dict[str, List[Dict[str, int]]], _: dict) -> dict:
        return { "DictArrayProperty": value }

    async def set_DictArrayProperty(self, value: Dict[str, List[Dict[str, int]]]):
        """Setter for property DictArrayProperty

        a simple property

        Args:
            value (Dict[str, List[Dict[str, int]]]): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_DictArrayProperty_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)
