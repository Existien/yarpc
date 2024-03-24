# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/06.3_enums_with_dicts.yml
#   Object: EnumsWithDicts
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
from .enum_struct import EnumStruct
from .color import Color


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for EnumsWithDicts

    Args:
        wrapper(BackendEnumsWithDictsInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.enumsWithDicts")
        self.object_path = "/com/yarpc/backend"
        self._wrapper = wrapper

    @method()
    async def EnumMethod(
        self,
        color: 'a{ii}',
    ) -> 'a{ii}':
        raw_return = await self._wrapper.EnumMethod(
            { Color(k0): Color(v0) for k0, v0 in color.items() },
        )
        return { k0.value: v0.value for k0, v0 in raw_return.items() }

    @signal()
    def EnumSignal(
        self,
        color: 'a{ii}',
    ) -> 'a{ii}':
        return color

    @dbus_property(access=PropertyAccess.READWRITE)
    async def EnumProperty(self) -> 'a{ii}':
        unmarshalled = await self._wrapper.get_EnumProperty()
        return { k0.value: v0.value for k0, v0 in unmarshalled.items() }

    @EnumProperty.setter
    async def EnumProperty(self, value: 'a{ii}'):
        unmarshalled = { Color(k0): Color(v0) for k0, v0 in value.items() }
        await self._wrapper.set_EnumProperty(unmarshalled)


class BackendEnumsWithDictsInterfaceMock():
    """
    Mock service implementation of the EnumsWithDicts D-Bus interface.

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
        EnumProperty (Dict[Color, Color]): a property
    """

    def __init__(
        self,
        EnumProperty: Dict[Color, Color],
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.EnumMethod.return_value = None

        self._properties = {}
        self._properties["EnumProperty"] = EnumProperty
        self._EnumProperty_change_handler = BackendEnumsWithDictsInterfaceMock._default_EnumProperty_change_handler
        self.mock.on_EnumProperty_changed = AsyncMock(wraps=self._EnumProperty_change_handler)

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

    async def EnumMethod(
        self,
        color: Dict[Color, Color],
    ) -> Dict[Color, Color]:
        """
        a simple method with one argument

        Args:
            color (Dict[Color, Color]): a color

        Returns:
            Dict[Color, Color]: another color
        """
        return await self._await_mock_method("EnumMethod", locals())

    def EnumSignal(
        self,
        color: Dict[Color, Color],
    ) -> None:
        """
        a simple signal with one argument

        Args:
            color (Dict[Color, Color]): a color
        """
        self.interface.EnumSignal(
            { k0.value: v0.value for k0, v0 in color.items() },
        )

    async def get_EnumProperty(self) -> Dict[Color, Color]:
        """Getter for property EnumProperty

        a property

        Returns:
            Dict[Color, Color]: the current value
        """
        return self._properties["EnumProperty"]

    def on_EnumProperty_changed(self, handler) -> None:
        """
        Set handler for property changes due to EnumProperty changes

        The handler takes the new EnumProperty value and a dictionary of the current properties
        and returns a dictionary with the current property values, or just the changed ones

        Args:
            handler(Callable[[Dict[Color, Color], dict], Awaitable[dict]]): the properties change handler

        Returns:
            dict: the changed properties
        """
        self._EnumProperty_change_handler = handler
        self.mock.on_EnumProperty_changed = AsyncMock(wraps=self._EnumProperty_change_handler)

    async def _default_EnumProperty_change_handler(value: Dict[Color, Color], _: dict) -> dict:
        return { "EnumProperty": value }

    async def set_EnumProperty(self, value: Dict[Color, Color]):
        """Setter for property EnumProperty

        a property

        Args:
            value (Dict[Color, Color]): the new value
        """
        properties_working_copy = deepcopy(self._properties)
        changed_properties = await self.mock.on_EnumProperty_changed(value, properties_working_copy)
        properties_working_copy.update(changed_properties)
        for key in self._properties.keys():
            if key not in properties_working_copy:
                continue
            if properties_working_copy[key] == self._properties[key]:
                del properties_working_copy[key]
            else:
                self._properties[key] = properties_working_copy[key]

            self.emit_properties_changed(properties_working_copy)
