# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/qt6/07_qml_instantiation.yml
#   Object: QmlAsClient
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
from .qml_struct import QmlStruct


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for QmlAsClient

    Args:
        wrapper(QmlInstantiationInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.qmlInstantiation")
        self.object_path = "/com/yarpc/backend/qmlInstantiation"
        self._wrapper = wrapper

    @method()
    async def PassStructMethod(
        self,
        qmlStruct: '(sd)',
    ) -> None:
        await self._wrapper.PassStructMethod(
            QmlStruct.from_dbus(qmlStruct),
        )
        return None

    @method()
    async def PassArrayInArrayMethod(
        self,
        listOfLists: 'aau',
    ) -> None:
        await self._wrapper.PassArrayInArrayMethod(
            [ [ x1 for x1 in x0 ] for x0 in listOfLists ],
        )
        return None

    @method()
    async def PassStructsInArrayMethod(
        self,
        listOfStructs: 'a(sd)',
    ) -> None:
        await self._wrapper.PassStructsInArrayMethod(
            [ QmlStruct.from_dbus(x0) for x0 in listOfStructs ],
        )
        return None

    @method()
    async def PassDictWithStringsMethod(
        self,
        dictWithStrings: 'a{ss}',
    ) -> None:
        await self._wrapper.PassDictWithStringsMethod(
            { k0: v0 for k0, v0 in dictWithStrings.items() },
        )
        return None

    @method()
    async def PassDictWithNumbersMethod(
        self,
        dictWithNumbers: 'a{us}',
    ) -> None:
        await self._wrapper.PassDictWithNumbersMethod(
            { k0: v0 for k0, v0 in dictWithNumbers.items() },
        )
        return None

    @method()
    async def PassDictWithStructsMethod(
        self,
        dictWithStructs: 'a{s(sd)}',
    ) -> None:
        await self._wrapper.PassDictWithStructsMethod(
            { k0: QmlStruct.from_dbus(v0) for k0, v0 in dictWithStructs.items() },
        )
        return None

    @method()
    async def PassDictInArrayMethod(
        self,
        listOfDicts: 'aa{ss}',
    ) -> None:
        await self._wrapper.PassDictInArrayMethod(
            [ { k1: v1 for k1, v1 in x0.items() } for x0 in listOfDicts ],
        )
        return None

    @method()
    async def PassDictInDictMethod(
        self,
        dictOfDicts: 'a{sa{ss}}',
    ) -> None:
        await self._wrapper.PassDictInDictMethod(
            { k0: { k1: v1 for k1, v1 in v0.items() } for k0, v0 in dictOfDicts.items() },
        )
        return None

    @method()
    async def PassArrayInDictMethod(
        self,
        dictOfLists: 'a{sas}',
    ) -> None:
        await self._wrapper.PassArrayInDictMethod(
            { k0: [ x1 for x1 in v0 ] for k0, v0 in dictOfLists.items() },
        )
        return None

    @method()
    async def PassDictInArrayInDictMethod(
        self,
        dictOfListsOfDicts: 'a{saa{ss}}',
    ) -> None:
        await self._wrapper.PassDictInArrayInDictMethod(
            { k0: [ { k2: v2 for k2, v2 in x1.items() } for x1 in v0 ] for k0, v0 in dictOfListsOfDicts.items() },
        )
        return None

    @method()
    async def PassDictInArrayInArrayMethod(
        self,
        listOfListsOfDicts: 'aaa{ss}',
    ) -> None:
        await self._wrapper.PassDictInArrayInArrayMethod(
            [ [ { k2: v2 for k2, v2 in x1.items() } for x1 in x0 ] for x0 in listOfListsOfDicts ],
        )
        return None


class QmlInstantiationInterfaceMock():
    """
    Mock service implementation of the QmlAsClient D-Bus interface.

    The AsyncMock instance can be accessed via the `mock` attribute.
    All method calls will be forwarded to the mock using keyword arguments.
    E.g.
    `await service.Foo('bar')`
    might result in the following await of the mock:
    `await service.mock.Foo(msg='bar')`
    """

    def __init__(
        self,
    ):
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.PassStructMethod.return_value = None
        self.mock.PassArrayInArrayMethod.return_value = None
        self.mock.PassStructsInArrayMethod.return_value = None
        self.mock.PassDictWithStringsMethod.return_value = None
        self.mock.PassDictWithNumbersMethod.return_value = None
        self.mock.PassDictWithStructsMethod.return_value = None
        self.mock.PassDictInArrayMethod.return_value = None
        self.mock.PassDictInDictMethod.return_value = None
        self.mock.PassArrayInDictMethod.return_value = None
        self.mock.PassDictInArrayInDictMethod.return_value = None
        self.mock.PassDictInArrayInArrayMethod.return_value = None

        self._properties = {}

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

    async def PassStructMethod(
        self,
        qmlStruct: QmlStruct,
    ) -> None:
        """
        pass struct

        Args:
            qmlStruct (QmlStruct): the struct
        """
        return await self._await_mock_method("PassStructMethod", locals())

    async def PassArrayInArrayMethod(
        self,
        listOfLists: List[List[int]],
    ) -> None:
        """
        pass nested arrays

        Args:
            listOfLists (List[List[int]]): the nested array
        """
        return await self._await_mock_method("PassArrayInArrayMethod", locals())

    async def PassStructsInArrayMethod(
        self,
        listOfStructs: List[QmlStruct],
    ) -> None:
        """
        pass structs in array

        Args:
            listOfStructs (List[QmlStruct]): list of structs
        """
        return await self._await_mock_method("PassStructsInArrayMethod", locals())

    async def PassDictWithStringsMethod(
        self,
        dictWithStrings: Dict[str, str],
    ) -> None:
        """
        pass a dict with strings as keys

        Args:
            dictWithStrings (Dict[str, str]): dict with string as keys
        """
        return await self._await_mock_method("PassDictWithStringsMethod", locals())

    async def PassDictWithNumbersMethod(
        self,
        dictWithNumbers: Dict[int, str],
    ) -> None:
        """
        pass a dict with numbers as keys

        Args:
            dictWithNumbers (Dict[int, str]): dict with numbers as keys
        """
        return await self._await_mock_method("PassDictWithNumbersMethod", locals())

    async def PassDictWithStructsMethod(
        self,
        dictWithStructs: Dict[str, QmlStruct],
    ) -> None:
        """
        pass a dict with structs as values

        Args:
            dictWithStructs (Dict[str, QmlStruct]): dict with structs as values
        """
        return await self._await_mock_method("PassDictWithStructsMethod", locals())

    async def PassDictInArrayMethod(
        self,
        listOfDicts: List[Dict[str, str]],
    ) -> None:
        """
        pass dict in array

        Args:
            listOfDicts (List[Dict[str, str]]): list of dicts
        """
        return await self._await_mock_method("PassDictInArrayMethod", locals())

    async def PassDictInDictMethod(
        self,
        dictOfDicts: Dict[str, Dict[str, str]],
    ) -> None:
        """
        pass dict in dict

        Args:
            dictOfDicts (Dict[str, Dict[str, str]]): dict of dicts
        """
        return await self._await_mock_method("PassDictInDictMethod", locals())

    async def PassArrayInDictMethod(
        self,
        dictOfLists: Dict[str, List[str]],
    ) -> None:
        """
        pass array in dict

        Args:
            dictOfLists (Dict[str, List[str]]): dict of lists
        """
        return await self._await_mock_method("PassArrayInDictMethod", locals())

    async def PassDictInArrayInDictMethod(
        self,
        dictOfListsOfDicts: Dict[str, List[Dict[str, str]]],
    ) -> None:
        """
        pass dict in array in dict

        Args:
            dictOfListsOfDicts (Dict[str, List[Dict[str, str]]]): dict of lists of dicts
        """
        return await self._await_mock_method("PassDictInArrayInDictMethod", locals())

    async def PassDictInArrayInArrayMethod(
        self,
        listOfListsOfDicts: List[List[Dict[str, str]]],
    ) -> None:
        """
        pass dict in array in array

        Args:
            listOfListsOfDicts (List[List[Dict[str, str]]]): list of lists of dicts
        """
        return await self._await_mock_method("PassDictInArrayInArrayMethod", locals())
