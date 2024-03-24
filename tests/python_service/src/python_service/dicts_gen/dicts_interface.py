# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/05.1_dictionaries.yml
#   Object: Dicts
#   Template: py/service.j2

from typing import Protocol, List, Dict
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from copy import deepcopy
from enum import Enum
from .struct_dict import StructDict
from .simons_dict import SimonsDict


class ProvidesDictsInterfaceProperties(Protocol):
    """Protocol for property providers of DictsInterface
    """

    async def get_DictProperty(self) -> Dict[str, int]:
        """Getter for DictProperty property

        Returns:
            Dict[str, int]: the current value
        """
        ...

    async def set_DictProperty(self, value: Dict[str, int]) -> dict:
        """Setter for DictProperty property

        Args:
            value (Dict[str, int]): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        ...


class DictsInterfaceProperties:
    """Manages the state of the properties for DictsInterface

    Args:
        DictProperty (Dict[str, int]): a prop
    """

    def __init__(
        self,
        DictProperty: Dict[str, int],
    ):
        self._properties = {
            "DictProperty": DictProperty,
        }

    async def get_DictProperty(self) -> Dict[str, int]:
        """Getter for DictProperty property

        Returns:
            Dict[str, int]: the current value
        """
        return self._properties["DictProperty"]

    async def set_DictProperty(self, value: Dict[str, int]) -> dict:
        """Setter for DictProperty property

        Args:
            value (Dict[str, int]): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        if value == self._properties["DictProperty"]:
            return {}
        self._properties["DictProperty"] = value
        return {"DictProperty": value}


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for Dicts

    Args:
        wrapper(DictsInterface): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.testservice.dicts")
        self.object_path = "/com/yarpc/testservice"
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


class DictsInterface():
    """
    A interface using dictionaries

    Args:
        property_provider (ProvidesDictsInterfaceProperties): provider for interface properties
    """

    def __init__(
        self,
        property_provider: ProvidesDictsInterfaceProperties,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path

        self._DictMethod_handler = None
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

    def on_DictMethod(self, handler) -> None:
        """
        Set handler for DictMethod method

        Args:
            handler (Callable[[Dict[str, int]], Awaitable[Dict[str, str]]]): the method handler
        """
        self._DictMethod_handler = handler

    async def DictMethod(
        self,
        keysNValues: Dict[str, int],
    ) -> Dict[str, str]:
        """
        a simple method with one argument

        Args:
            keysNValues (Dict[str, int]): a dictionary

        Returns:
            Dict[str, str]: another one
        """
        if self._DictMethod_handler is None:
            raise NotImplementedError()

        return await self._DictMethod_handler(
            keysNValues,
        )

    def DictSignal(
        self,
        keysNValues: Dict[str, int],
    ) -> None:
        """
        a signal

        Args:
            keysNValues (Dict[str, int]): a dictionary
        """
        self.interface.DictSignal(
            { k0: v0 for k0, v0 in keysNValues.items() },
        )

    async def get_DictProperty(self) -> Dict[str, int]:
        """Getter for property DictProperty

        a prop

        Returns:
            Dict[str, int]: the current value
        """
        return await self._properties.get_DictProperty()

    async def set_DictProperty(self, value: Dict[str, int]):
        """Setter for property DictProperty

        a prop

        Args:
            value (Dict[str, int]): the new value
        """
        changed_properties = await self._properties.set_DictProperty(value)

        self.emit_properties_changed(changed_properties)
