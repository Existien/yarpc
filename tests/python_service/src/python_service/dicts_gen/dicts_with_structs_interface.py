# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/05.2_dictionaries_with_structs.yml
#   Object: DictsWithStructs
#   Template: py/service.j2

from typing import Protocol, Sequence, Mapping
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from copy import deepcopy
from .struct_dict import StructDict
from .simons_dict import SimonsDict


class ProvidesDictsWithStructsInterfaceProperties(Protocol):
    """Protocol for property providers of DictsWithStructsInterface
    """

    async def get_DictStructProperty(self) -> Mapping[str, StructDict]:
        """Getter for DictStructProperty property

        Returns:
            Mapping[str, StructDict]: the current value
        """
        ...

    async def set_DictStructProperty(self, value: Mapping[str, StructDict]) -> dict:
        """Setter for DictStructProperty property

        Args:
            value (Mapping[str, StructDict]): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        ...


class DictsWithStructsInterfaceProperties:
    """Manages the state of the properties for DictsWithStructsInterface

    Args:
        DictStructProperty (Mapping[str, StructDict]): a simple property
    """

    def __init__(
        self,
        DictStructProperty: Mapping[str, StructDict],
    ):
        self._properties = {
            "DictStructProperty": DictStructProperty,
        }

    async def get_DictStructProperty(self) -> Mapping[str, StructDict]:
        """Getter for DictStructProperty property

        Returns:
            Mapping[str, StructDict]: the current value
        """
        return self._properties["DictStructProperty"]

    async def set_DictStructProperty(self, value: Mapping[str, StructDict]) -> dict:
        """Setter for DictStructProperty property

        Args:
            value (Mapping[str, StructDict]): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        if value == self._properties["DictStructProperty"]:
            return {}
        self._properties["DictStructProperty"] = value
        return {"DictStructProperty": value}


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for DictsWithStructs

    Args:
        wrapper(DictsWithStructsInterface): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.testservice.dictsWithStructs")
        self.object_path = "/com/yarpc/testservice"
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


class DictsWithStructsInterface():
    """
    A interface using dicts using structs using dicts

    Args:
        property_provider (ProvidesDictsWithStructsInterfaceProperties): provider for interface properties
    """

    def __init__(
        self,
        property_provider: ProvidesDictsWithStructsInterfaceProperties,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path

        self._DictsStructMethod_handler = None
        self._properties = property_provider

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

    def on_DictsStructMethod(self, handler) -> None:
        """
        Set handler for DictsStructMethod method

        Args:
            handler (Callable[[Mapping[str, StructDict]], Awaitable[Mapping[str, SimonsDict]]]): the method handler
        """
        self._DictsStructMethod_handler = handler

    async def DictsStructMethod(
        self,
        numbers: Mapping[str, StructDict],
    ) -> Mapping[str, SimonsDict]:
        """
        a simple method with one argument

        Args:
            numbers (Mapping[str, StructDict]): Some numbers

        Returns:
            Mapping[str, SimonsDict]: more numbers
        """
        if self._DictsStructMethod_handler is None:
            raise NotImplementedError()

        return await self._DictsStructMethod_handler(
            numbers,
        )

    def DictStructSignal(
        self,
        numbers: Mapping[str, StructDict],
    ) -> None:
        """
        a simple signal with one argument

        Args:
            numbers (Mapping[str, StructDict]): numbers
        """
        self.interface.DictStructSignal(
            { k0: v0.to_dbus() for k0, v0 in numbers.items() },
        )

    async def get_DictStructProperty(self) -> Mapping[str, StructDict]:
        """Getter for property DictStructProperty

        a simple property

        Returns:
            Mapping[str, StructDict]: the current value
        """
        return await self._properties.get_DictStructProperty()

    async def set_DictStructProperty(self, value: Mapping[str, StructDict]):
        """Setter for property DictStructProperty

        a simple property

        Args:
            value (Mapping[str, StructDict]): the new value
        """
        changed_properties = await self._properties.set_DictStructProperty(value)

        self.emit_properties_changed(changed_properties)
