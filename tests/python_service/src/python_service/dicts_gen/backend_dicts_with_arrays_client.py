# Generated by YARPC
# Version:  0.1.0+editable
# Definition:
#   File: /workspace/tests/definitions/05.3_dictionaries_with_arrays.yml
#   Object: DictsWithArrays
#   Template: py/client.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
import sys
import asyncio
from .struct_dict import StructDict
from .simons_dict import SimonsDict


class BackendDictsWithArraysClient():
    """
    A interface using dicts using arrays using dicts
    """

    def __init__(self):
        self.name = "com.yarpc.backend.dictsWithArrays"
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._DictsArraySignal_handler = None
        self._close_event = asyncio.Event()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.backend",
                "/com/yarpc/backend",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.backend",
                "/com/yarpc/backend",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            if self._DictsArraySignal_handler:
                self._interface.on_dicts_array_signal(self._DictsArraySignal_wrapper)

            self._property_interface = proxy_object.get_interface(
                "org.freedesktop.DBus.Properties"
            )
            if self._properties_changed_handler:
                self._property_interface.on_properties_changed(self._properties_changed_wrapper)

            self._close_event.clear()
            await asyncio.wait(
                map(
                    lambda x: asyncio.create_task(x),
                    [self._close_event.wait(), bus.wait_for_disconnect()]
                ),
                return_when=asyncio.FIRST_COMPLETED
            )
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)

    def disconnect(self):
        """
        Closes the D-Bus connection of this client
        """
        self._close_event.set()
        if self._DictsArraySignal_handler:
            self._interface.off_dicts_array_signal(self._DictsArraySignal_wrapper)
        if self._properties_changed_handler:
                self._property_interface.off_properties_changed(self._properties_changed_wrapper)
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._DictsArraySignal_handler = None

    def _unpack_prop(self, name, variant):
        prop_map = {
            "DictArrayProperty": lambda value: { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in value.items() },
        }
        if name in prop_map:
            return prop_map[name](variant.value)
        return None

    def _unpack_properties(self, packed_properties):
        return {
            key: self._unpack_prop(key, packed_properties[key])
            for key in packed_properties.keys()
        }

    async def get_all_properties(self) -> dict:
        """Getter for all properties

        Returns:
            dict: a dictionary containing the current state of all properties
        """
        while not self._property_interface:
            await asyncio.sleep(0.1)
        properties = await self._property_interface.call_get_all(self.name)
        return self._unpack_properties(properties)

    def _properties_changed_wrapper(self, interface: str, properties: dict, _invalidated: list):
        if self._properties_changed_handler and interface == self.name:
            properties = self._unpack_properties(properties)
            self._properties_changed_handler(properties)

    def on_properties_changed(self, handler) -> None:
        """
        Set handler for property changes

        The handler takes a dictionary of the changed properties

        Args:
            handler(Callable[[dict], None]): the handler
        """
        self._properties_changed_handler = handler

    async def DictsArrayMethod(
        self,
        numbers: 'Dict[str, List[Dict[str, int]]]',
    ) -> Dict[str, List[Dict[str, int]]]:
        """
        a simple method with one argument

        Args:
            numbers (Dict[str, List[Dict[str, int]]]): some numbers

        Returns:
            Dict[str, List[Dict[str, int]]]: some numbers
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_dicts_array_method(
            { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in numbers.items() },
        )
        return { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in raw_return.items() }

    def _DictsArraySignal_wrapper(
        self,
        numbers: 'a{saa{su}}',
    ):
        self._DictsArraySignal_handler(
            { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in numbers.items() },
        )

    def on_DictsArraySignal(self, handler):
        """
        Set handler for DictsArraySignal signal

        Args:
            handler (Callable[[Dict[str, List[Dict[str, int]]]], None]): the signal handler
        """
        self._DictsArraySignal_handler = handler
        if self._interface:
            self._interface.on_dicts_array_signal(self._DictsArraySignal_wrapper)

    async def get_DictArrayProperty(self) -> Dict[str, List[Dict[str, int]]]:
        """Getter for property 'DictArrayProperty'

        a simple property

        Returns:
            Dict[str, List[Dict[str, int]]]: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_dict_array_property()
        unmarshalled = { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in raw_return.items() }
        return unmarshalled


    async def set_DictArrayProperty(self, value: Dict[str, List[Dict[str, int]]]) -> None:
        """Setter for property 'DictArrayProperty'

        a simple property

        Args:
            value (Dict[str, List[Dict[str, int]]]): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in value.items() }
        return await self._interface.set_dict_array_property(marshalled)
