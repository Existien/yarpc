from python_mocks import (
    BackendMinimalInterfaceMock,
    BackendWithArgsInterfaceMock,
    BackendPrimitivesInterfaceMock,
    BackendStructsInterfaceMock, SimpleStruct, Item,
    BackendArraysInterfaceMock,
    BackendArraysWithStructsInterfaceMock, StructArray,
    BackendDictsInterfaceMock,
    BackendDictsWithStructsInterfaceMock, StructDict,
    BackendDictsWithArraysInterfaceMock,
    BackendDictKeysInterfaceMock,
    BackendEnumsInterfaceMock, Color,
    BackendEnumsWithArraysInterfaceMock,
    BackendEnumsWithDictsInterfaceMock,
    BackendEnumsWithStructsInterfaceMock, EnumStruct,
    QmlInstantiationInterfaceMock,
)

def get_service_mock(interface):
    match interface:
        case 'Minimal':
            return BackendMinimalInterfaceMock()
        case 'WithArgs':
            return BackendWithArgsInterfaceMock(
                Speed=10.0,
                Distance=200,
                Duration=200/10.0,
            )
        case 'Primitives':
            return BackendPrimitivesInterfaceMock()
        case 'Structs':
            return BackendStructsInterfaceMock(
                Simple=SimpleStruct(
                    Item(
                        name="Foo",
                        price=0.98,
                    ),
                    amount=42,
                )
            )
        case 'Arrays':
            return BackendArraysInterfaceMock(
                ArrayProperty=[["Foo", "Bar"], ["Baz"]]
            )
        case 'ArraysWithStructs':
            return BackendArraysWithStructsInterfaceMock(
                ArrayStructProperty=[StructArray(numbers=[[1],[2]]),StructArray(numbers=[[3,4]])]
            )
        case 'Dictionaries':
            return BackendDictsInterfaceMock(
                DictProperty={"Fizz":3, "Buzz": 5}
            )
        case 'DictsWithStructs':
            return BackendDictsWithStructsInterfaceMock(
                DictStructProperty={
                    "first": StructDict(numbers={
                        "1": {"Fizz": 3, "Buzz": 5},
                        "2": {"One": 1, "Two": 2},
                    }),
                    "second": StructDict(numbers={
                        "Legs": {"Fish": 0, "Dog": 4, "Ant": 6},
                        "Wings": {"Fish": 0, "Dog": 0, "Ant": 2},
                    }),
                }
            )
        case 'DictsWithArrays':
            return BackendDictsWithArraysInterfaceMock(
                DictArrayProperty={
                    "A": [{"AA1": 11, "AA2": 12}, {"AB1": 21, "AB2": 22}],
                    "B": [{"BA1": 11, "BA2": 12}, {"BB1": 21, "BB2": 22}],
                }
            )
        case 'DictKeys':
            return BackendDictKeysInterfaceMock()
        case 'Enums':
            return BackendEnumsInterfaceMock(
                EnumProperty=Color.GREEN
            )
        case 'EnumsWithArrays':
            return BackendEnumsWithArraysInterfaceMock(
                EnumProperty=[Color.RED, Color.GREEN, Color.BLUE]
            )
        case 'EnumsWithDicts':
            return BackendEnumsWithDictsInterfaceMock(
                EnumProperty={
                    Color.RED: Color.GREEN,
                    Color.GREEN: Color.RED,
                    Color.BLUE: Color.ORANGE,
                }
            )
        case 'EnumsWithStructs':
            return BackendEnumsWithStructsInterfaceMock(
                EnumProperty=EnumStruct(
                    color=Color.GREEN,
                    colorArray=[Color.RED, Color.GREEN, Color.BLUE],
                    colorDict={
                        Color.RED: Color.GREEN,
                        Color.GREEN: Color.RED,
                        Color.BLUE: Color.ORANGE,
                    }
                )
            )
        case 'QmlInstantiation':
            return QmlInstantiationInterfaceMock()
        case _:
            assert False, f"Unknown interface '{interface}'"