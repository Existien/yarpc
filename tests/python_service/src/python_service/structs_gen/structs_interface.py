# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/03_structs.yml
#   Object: Structs
#   Template: py/service.j2

from typing import Protocol, Sequence, Mapping
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from copy import deepcopy
from .simple_struct import SimpleStruct
from .item import Item


class ProvidesStructsInterfaceProperties(Protocol):
    """Protocol for property providers of StructsInterface
    """

    async def get_Simple(self) -> SimpleStruct:
        """Getter for Simple property

        Returns:
            SimpleStruct: the current value
        """
        ...

    async def set_Simple(self, value: SimpleStruct) -> dict:
        """Setter for Simple property

        Args:
            value (SimpleStruct): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        ...


class StructsInterfaceProperties:
    """Manages the state of the properties for StructsInterface

    Args:
        Simple (SimpleStruct): a property for a simple struct
    """

    def __init__(
        self,
        Simple: SimpleStruct,
    ):
        self._properties = {
            "Simple": Simple,
        }

    async def get_Simple(self) -> SimpleStruct:
        """Getter for Simple property

        Returns:
            SimpleStruct: the current value
        """
        return self._properties["Simple"]

    async def set_Simple(self, value: SimpleStruct) -> dict:
        """Setter for Simple property

        Args:
            value (SimpleStruct): the new value

        Returns:
            dict: dictionary of the changed properties, empty if None changed
        """
        if value == self._properties["Simple"]:
            return {}
        self._properties["Simple"] = value
        return {"Simple": value}


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for Structs

    Args:
        wrapper(StructsInterface): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.testservice.structs")
        self.object_path = "/com/yarpc/testservice"
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


class StructsInterface():
    """
    A interface with structures

    Args:
        property_provider (ProvidesStructsInterfaceProperties): provider for interface properties
    """

    def __init__(
        self,
        property_provider: ProvidesStructsInterfaceProperties,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path

        self._SendStruct_handler = None
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

    def on_SendStruct(self, handler) -> None:
        """
        Set handler for SendStruct method

        Args:
            handler (Callable[[SimpleStruct], Awaitable[SimpleStruct]]): the method handler
        """
        self._SendStruct_handler = handler

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
        if self._SendStruct_handler is None:
            raise NotImplementedError()

        return await self._SendStruct_handler(
            simpleStruct,
        )

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
        return await self._properties.get_Simple()

    async def set_Simple(self, value: SimpleStruct):
        """Setter for property Simple

        a property for a simple struct

        Args:
            value (SimpleStruct): the new value
        """
        changed_properties = await self._properties.set_Simple(value)

        self.emit_properties_changed(changed_properties)
