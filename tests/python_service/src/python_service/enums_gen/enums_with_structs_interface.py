# Generated by YARPC
# Version:  0.1.0+editable
# Definition:
#   File: /workspace/tests/definitions/06.4_enums_with_structs.yml
#   Object: EnumsWithStructs
#   Template: py/service.j2

from typing import Protocol, List, Dict
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from copy import deepcopy
from enum import Enum
from .enum_struct import EnumStruct
from .color import Color


class ProvidesEnumsWithStructsInterfaceProperties(Protocol):
    """Protocol for property providers of EnumsWithStructsInterface
    """

    async def get_EnumProperty(self) -> EnumStruct:
        """Getter for EnumProperty property

        Returns:
            EnumStruct: the current value
        """
        ...

    async def set_EnumProperty(self, value: EnumStruct) -> dict:
        """Setter for EnumProperty property

        Args:
            value (EnumStruct): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        ...


class EnumsWithStructsInterfaceProperties:
    """Manages the state of the properties for EnumsWithStructsInterface

    Args:
        EnumProperty (EnumStruct): a property
    """

    def __init__(
        self,
        EnumProperty: EnumStruct,
    ):
        self._properties = {
            "EnumProperty": EnumProperty,
        }

    async def get_EnumProperty(self) -> EnumStruct:
        """Getter for EnumProperty property

        Returns:
            EnumStruct: the current value
        """
        return self._properties["EnumProperty"]

    async def set_EnumProperty(self, value: EnumStruct) -> dict:
        """Setter for EnumProperty property

        Args:
            value (EnumStruct): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        if value == self._properties["EnumProperty"]:
            return {}
        self._properties["EnumProperty"] = value
        return {"EnumProperty": value}


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for EnumsWithStructs

    Args:
        wrapper(EnumsWithStructsInterface): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.testservice.enumsWithStructs")
        self.object_path = "/com/yarpc/testservice"
        self._wrapper = wrapper

    @method()
    async def EnumMethod(
        self,
        color: '(iaia{ii})',
    ) -> '(iaia{ii})':
        raw_return = await self._wrapper.EnumMethod(
            EnumStruct.from_dbus(color),
        )
        return raw_return.to_dbus()

    @signal()
    def EnumSignal(
        self,
        color: '(iaia{ii})',
    ) -> '(iaia{ii})':
        return color

    @dbus_property(access=PropertyAccess.READWRITE)
    async def EnumProperty(self) -> '(iaia{ii})':
        unmarshalled = await self._wrapper.get_EnumProperty()
        return unmarshalled.to_dbus()

    @EnumProperty.setter
    async def EnumProperty(self, value: '(iaia{ii})'):
        unmarshalled = EnumStruct.from_dbus(value)
        await self._wrapper.set_EnumProperty(unmarshalled)


class EnumsWithStructsInterface():
    """
    A interface using enums

    Args:
        property_provider (ProvidesEnumsWithStructsInterfaceProperties): provider for interface properties
    """

    def __init__(
        self,
        property_provider: ProvidesEnumsWithStructsInterfaceProperties,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path

        self._EnumMethod_handler = None
        self._properties = property_provider

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

    def on_EnumMethod(self, handler) -> None:
        """
        Set handler for EnumMethod method

        Args:
            handler (Callable[[EnumStruct], Awaitable[EnumStruct]]): the method handler
        """
        self._EnumMethod_handler = handler

    async def EnumMethod(
        self,
        color: EnumStruct,
    ) -> EnumStruct:
        """
        a simple method with one argument

        Args:
            color (EnumStruct): a color

        Returns:
            EnumStruct: another color
        """
        if self._EnumMethod_handler is None:
            raise NotImplementedError()

        return await self._EnumMethod_handler(
            color,
        )

    def EnumSignal(
        self,
        color: EnumStruct,
    ) -> None:
        """
        a simple signal with one argument

        Args:
            color (EnumStruct): a color
        """
        self.interface.EnumSignal(
            color.to_dbus(),
        )

    async def get_EnumProperty(self) -> EnumStruct:
        """Getter for property EnumProperty

        a property

        Returns:
            EnumStruct: the current value
        """
        return await self._properties.get_EnumProperty()

    async def set_EnumProperty(self, value: EnumStruct):
        """Setter for property EnumProperty

        a property

        Args:
            value (EnumStruct): the new value
        """
        changed_properties = await self._properties.set_EnumProperty(value)

        self.emit_properties_changed(changed_properties)
