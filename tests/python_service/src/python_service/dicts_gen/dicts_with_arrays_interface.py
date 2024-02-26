# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/05.3_dictionaries_with_arrays.yml
#   Object: DictsWithArrays
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


class ProvidesDictsWithArraysInterfaceProperties(Protocol):
    """Protocol for property providers of DictsWithArraysInterface
    """

    async def get_DictArrayProperty(self) -> Mapping[str, Sequence[Mapping[str, int]]]:
        """Getter for DictArrayProperty property

        Returns:
            Mapping[str, Sequence[Mapping[str, int]]]: the current value
        """
        ...

    async def set_DictArrayProperty(self, value: Mapping[str, Sequence[Mapping[str, int]]]) -> dict:
        """Setter for DictArrayProperty property

        Args:
            value (Mapping[str, Sequence[Mapping[str, int]]]): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        ...


class DictsWithArraysInterfaceProperties:
    """Manages the state of the properties for DictsWithArraysInterface

    Args:
        DictArrayProperty (Mapping[str, Sequence[Mapping[str, int]]]): a simple property
    """

    def __init__(
        self,
        DictArrayProperty: Mapping[str, Sequence[Mapping[str, int]]],
    ):
        self._properties = {
            "DictArrayProperty": DictArrayProperty,
        }

    async def get_DictArrayProperty(self) -> Mapping[str, Sequence[Mapping[str, int]]]:
        """Getter for DictArrayProperty property

        Returns:
            Mapping[str, Sequence[Mapping[str, int]]]: the current value
        """
        return self._properties["DictArrayProperty"]

    async def set_DictArrayProperty(self, value: Mapping[str, Sequence[Mapping[str, int]]]) -> dict:
        """Setter for DictArrayProperty property

        Args:
            value (Mapping[str, Sequence[Mapping[str, int]]]): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        if value == self._properties["DictArrayProperty"]:
            return {}
        self._properties["DictArrayProperty"] = value
        return {"DictArrayProperty": value}


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for DictsWithArrays

    Args:
        wrapper(DictsWithArraysInterface): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.testservice.dictsWithArrays")
        self.object_path = "/com/yarpc/testservice"
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


class DictsWithArraysInterface():
    """
    A interface using dicts using arrays using dicts

    Args:
        property_provider (ProvidesDictsWithArraysInterfaceProperties): provider for interface properties
    """

    def __init__(
        self,
        property_provider: ProvidesDictsWithArraysInterfaceProperties,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path

        self._DictsArrayMethod_handler = None
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

    def on_DictsArrayMethod(self, handler) -> None:
        """
        Set handler for DictsArrayMethod method

        Args:
            handler (Callable[[Mapping[str, Sequence[Mapping[str, int]]]], Awaitable[Mapping[str, Sequence[Mapping[str, int]]]]]): the method handler
        """
        self._DictsArrayMethod_handler = handler

    async def DictsArrayMethod(
        self,
        numbers: Mapping[str, Sequence[Mapping[str, int]]],
    ) -> Mapping[str, Sequence[Mapping[str, int]]]:
        """
        a simple method with one argument

        Args:
            numbers (Mapping[str, Sequence[Mapping[str, int]]]): some numbers

        Returns:
            Mapping[str, Sequence[Mapping[str, int]]]: some numbers
        """
        if self._DictsArrayMethod_handler is None:
            raise NotImplementedError()

        return await self._DictsArrayMethod_handler(
            numbers,
        )

    def DictsArraySignal(
        self,
        numbers: Mapping[str, Sequence[Mapping[str, int]]],
    ) -> None:
        """
        a simple signal with one argument

        Args:
            numbers (Mapping[str, Sequence[Mapping[str, int]]]): some numbers
        """
        self.interface.DictsArraySignal(
            { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in numbers.items() },
        )

    async def get_DictArrayProperty(self) -> Mapping[str, Sequence[Mapping[str, int]]]:
        """Getter for property DictArrayProperty

        a simple property

        Returns:
            Mapping[str, Sequence[Mapping[str, int]]]: the current value
        """
        return await self._properties.get_DictArrayProperty()

    async def set_DictArrayProperty(self, value: Mapping[str, Sequence[Mapping[str, int]]]):
        """Setter for property DictArrayProperty

        a simple property

        Args:
            value (Mapping[str, Sequence[Mapping[str, int]]]): the new value
        """
        changed_properties = await self._properties.set_DictArrayProperty(value)

        self.emit_properties_changed(changed_properties)
