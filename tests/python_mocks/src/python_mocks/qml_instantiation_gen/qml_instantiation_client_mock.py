# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/qt6/07_qml_instantiation.yml
#   Object: QmlAsService
#   Template: py/client_mock.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
from unittest.mock import Mock
import sys
import asyncio
from .qml_struct import QmlStruct
from .qml_enum import QmlEnum


class QmlInstantiationClientMock():
    """
    Mock client implementation of the QmlAsService D-Bus interface

    The Mock instance can be accessed via the `mock` attribute.
    All received signals will be forwarded to the mock using keyword arguments.
    E.g.
    A received signal `Fooed('bar')`
    might result in the following call of the mock:
    `client.mock.Fooed(msg='bar')`
    """

    def __init__(self):
        self.name = "com.yarpc.testservice.qmlInstantiation"
        self._interface = None
        self._property_interface = None
        self.mock = Mock()
        self._close_event = asyncio.Event()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.testservice",
                "/com/yarpc/testservice/qmlInstantiation",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.testservice",
                "/com/yarpc/testservice/qmlInstantiation",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            self._interface.on_pass_struct_signal(self._PassStructSignal_handler)
            self._interface.on_pass_array_in_array_signal(self._PassArrayInArraySignal_handler)
            self._interface.on_pass_structs_in_array_signal(self._PassStructsInArraySignal_handler)
            self._interface.on_pass_dict_with_strings_signal(self._PassDictWithStringsSignal_handler)
            self._interface.on_pass_dict_with_numbers_signal(self._PassDictWithNumbersSignal_handler)
            self._interface.on_pass_dict_with_structs_signal(self._PassDictWithStructsSignal_handler)
            self._interface.on_pass_dict_in_array_signal(self._PassDictInArraySignal_handler)
            self._interface.on_pass_dict_in_dict_signal(self._PassDictInDictSignal_handler)
            self._interface.on_pass_array_in_dict_signal(self._PassArrayInDictSignal_handler)
            self._interface.on_pass_dict_in_array_in_dict_signal(self._PassDictInArrayInDictSignal_handler)
            self._interface.on_pass_dict_in_array_in_array_signal(self._PassDictInArrayInArraySignal_handler)
            self._interface.on_pass_dict_with_enums_signal(self._PassDictWithEnumsSignal_handler)

            self._property_interface = proxy_object.get_interface(
                "org.freedesktop.DBus.Properties"
            )
            if self._properties_changed_handler:
                self._property_interface.on_properties_changed(self._properties_changed_handler)

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
        if self._PassStructSignal_handler:
            self._interface.off_pass_struct_signal(self._PassStructSignal_handler)
        if self._PassArrayInArraySignal_handler:
            self._interface.off_pass_array_in_array_signal(self._PassArrayInArraySignal_handler)
        if self._PassStructsInArraySignal_handler:
            self._interface.off_pass_structs_in_array_signal(self._PassStructsInArraySignal_handler)
        if self._PassDictWithStringsSignal_handler:
            self._interface.off_pass_dict_with_strings_signal(self._PassDictWithStringsSignal_handler)
        if self._PassDictWithNumbersSignal_handler:
            self._interface.off_pass_dict_with_numbers_signal(self._PassDictWithNumbersSignal_handler)
        if self._PassDictWithStructsSignal_handler:
            self._interface.off_pass_dict_with_structs_signal(self._PassDictWithStructsSignal_handler)
        if self._PassDictInArraySignal_handler:
            self._interface.off_pass_dict_in_array_signal(self._PassDictInArraySignal_handler)
        if self._PassDictInDictSignal_handler:
            self._interface.off_pass_dict_in_dict_signal(self._PassDictInDictSignal_handler)
        if self._PassArrayInDictSignal_handler:
            self._interface.off_pass_array_in_dict_signal(self._PassArrayInDictSignal_handler)
        if self._PassDictInArrayInDictSignal_handler:
            self._interface.off_pass_dict_in_array_in_dict_signal(self._PassDictInArrayInDictSignal_handler)
        if self._PassDictInArrayInArraySignal_handler:
            self._interface.off_pass_dict_in_array_in_array_signal(self._PassDictInArrayInArraySignal_handler)
        if self._PassDictWithEnumsSignal_handler:
            self._interface.off_pass_dict_with_enums_signal(self._PassDictWithEnumsSignal_handler)
        if self._properties_changed_handler:
                self._property_interface.off_properties_changed(self._properties_changed_handler)
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._PassStructSignal_handler = None
        self._PassArrayInArraySignal_handler = None
        self._PassStructsInArraySignal_handler = None
        self._PassDictWithStringsSignal_handler = None
        self._PassDictWithNumbersSignal_handler = None
        self._PassDictWithStructsSignal_handler = None
        self._PassDictInArraySignal_handler = None
        self._PassDictInDictSignal_handler = None
        self._PassArrayInDictSignal_handler = None
        self._PassDictInArrayInDictSignal_handler = None
        self._PassDictInArrayInArraySignal_handler = None
        self._PassDictWithEnumsSignal_handler = None

    def _unpack_prop(self, name, variant):
        prop_map = {
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
        properties = await self._property_interface.call_get_all(self.name)
        return self._unpack_properties(properties)

    def _properties_changed_handler(self, interface: str, properties: dict, _invalidated: list):
        if interface == self.name:
            properties = self._unpack_properties(properties)
            self.mock.on_properties_changed(properties=properties)

    async def PassStructMethod(
        self,
    ) -> QmlStruct:
        """
        pass struct
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_struct_method(
        )
        return QmlStruct.from_dbus(raw_return)

    def _PassStructSignal_handler(
        self,
            qmlStruct: '(sdi)',
    ):
        self.mock.PassStructSignal(
            qmlStruct=QmlStruct.from_dbus(qmlStruct),
        )

    async def PassArrayInArrayMethod(
        self,
    ) -> List[List[int]]:
        """
        pass nested arrays
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_array_in_array_method(
        )
        return [ [ x1 for x1 in x0 ] for x0 in raw_return ]

    def _PassArrayInArraySignal_handler(
        self,
            listOfLists: 'aau',
    ):
        self.mock.PassArrayInArraySignal(
            listOfLists=[ [ x1 for x1 in x0 ] for x0 in listOfLists ],
        )

    async def PassStructsInArrayMethod(
        self,
    ) -> List[QmlStruct]:
        """
        pass structs in array
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_structs_in_array_method(
        )
        return [ QmlStruct.from_dbus(x0) for x0 in raw_return ]

    def _PassStructsInArraySignal_handler(
        self,
            listOfStructs: 'a(sdi)',
    ):
        self.mock.PassStructsInArraySignal(
            listOfStructs=[ QmlStruct.from_dbus(x0) for x0 in listOfStructs ],
        )

    async def PassDictWithStringsMethod(
        self,
    ) -> Dict[str, str]:
        """
        pass a dict with strings as keys
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_with_strings_method(
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    def _PassDictWithStringsSignal_handler(
        self,
            dictWithStrings: 'a{ss}',
    ):
        self.mock.PassDictWithStringsSignal(
            dictWithStrings={ k0: v0 for k0, v0 in dictWithStrings.items() },
        )

    async def PassDictWithNumbersMethod(
        self,
    ) -> Dict[int, str]:
        """
        pass a dict with numbers as keys
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_with_numbers_method(
        )
        return { k0: v0 for k0, v0 in raw_return.items() }

    def _PassDictWithNumbersSignal_handler(
        self,
            dictWithNumbers: 'a{us}',
    ):
        self.mock.PassDictWithNumbersSignal(
            dictWithNumbers={ k0: v0 for k0, v0 in dictWithNumbers.items() },
        )

    async def PassDictWithStructsMethod(
        self,
    ) -> Dict[str, QmlStruct]:
        """
        pass a dict with structs as values
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_with_structs_method(
        )
        return { k0: QmlStruct.from_dbus(v0) for k0, v0 in raw_return.items() }

    def _PassDictWithStructsSignal_handler(
        self,
            dictWithStructs: 'a{s(sdi)}',
    ):
        self.mock.PassDictWithStructsSignal(
            dictWithStructs={ k0: QmlStruct.from_dbus(v0) for k0, v0 in dictWithStructs.items() },
        )

    async def PassDictInArrayMethod(
        self,
    ) -> List[Dict[str, str]]:
        """
        pass dict in array
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_in_array_method(
        )
        return [ { k1: v1 for k1, v1 in x0.items() } for x0 in raw_return ]

    def _PassDictInArraySignal_handler(
        self,
            listOfDicts: 'aa{ss}',
    ):
        self.mock.PassDictInArraySignal(
            listOfDicts=[ { k1: v1 for k1, v1 in x0.items() } for x0 in listOfDicts ],
        )

    async def PassDictInDictMethod(
        self,
    ) -> Dict[str, Dict[str, str]]:
        """
        pass dict in dict
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_in_dict_method(
        )
        return { k0: { k1: v1 for k1, v1 in v0.items() } for k0, v0 in raw_return.items() }

    def _PassDictInDictSignal_handler(
        self,
            dictOfDicts: 'a{sa{ss}}',
    ):
        self.mock.PassDictInDictSignal(
            dictOfDicts={ k0: { k1: v1 for k1, v1 in v0.items() } for k0, v0 in dictOfDicts.items() },
        )

    async def PassArrayInDictMethod(
        self,
    ) -> Dict[str, List[str]]:
        """
        pass array in dict
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_array_in_dict_method(
        )
        return { k0: [ x1 for x1 in v0 ] for k0, v0 in raw_return.items() }

    def _PassArrayInDictSignal_handler(
        self,
            dictOfLists: 'a{sas}',
    ):
        self.mock.PassArrayInDictSignal(
            dictOfLists={ k0: [ x1 for x1 in v0 ] for k0, v0 in dictOfLists.items() },
        )

    async def PassDictInArrayInDictMethod(
        self,
    ) -> Dict[str, List[Dict[str, str]]]:
        """
        pass dict in array in dict
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_in_array_in_dict_method(
        )
        return { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in raw_return.items() }

    def _PassDictInArrayInDictSignal_handler(
        self,
            dictOfListsOfDicts: 'a{saa{ss}}',
    ):
        self.mock.PassDictInArrayInDictSignal(
            dictOfListsOfDicts={ k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in dictOfListsOfDicts.items() },
        )

    async def PassDictInArrayInArrayMethod(
        self,
    ) -> List[List[Dict[str, str]]]:
        """
        pass dict in array in array
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_in_array_in_array_method(
        )
        return [ [ { k2: v2 for k2, v2 in x1.items() } for x1 in x0 ] for x0 in raw_return ]

    def _PassDictInArrayInArraySignal_handler(
        self,
            listOfListsOfDicts: 'aaa{ss}',
    ):
        self.mock.PassDictInArrayInArraySignal(
            listOfListsOfDicts=[ [ { k2: v2 for k2, v2 in x1.items() } for x1 in x0 ] for x0 in listOfListsOfDicts ],
        )

    async def PassDictWithEnumsMethod(
        self,
    ) -> Dict[QmlEnum, QmlEnum]:
        """
        pass dict with enums as keys and values
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_pass_dict_with_enums_method(
        )
        return { QmlEnum(k0): QmlEnum(v0) for k0, v0 in raw_return.items() }

    def _PassDictWithEnumsSignal_handler(
        self,
            dictOfEnumsToEnums: 'a{ii}',
    ):
        self.mock.PassDictWithEnumsSignal(
            dictOfEnumsToEnums={ QmlEnum(k0): QmlEnum(v0) for k0, v0 in dictOfEnumsToEnums.items() },
        )
