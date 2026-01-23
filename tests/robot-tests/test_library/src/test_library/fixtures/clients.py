from python_mocks import (
    MinimalClientMock,
    WithArgsClientMock,
    PrimitivesClientMock,
    StructsClientMock,
    ArraysClientMock,
    ArraysWithStructsClientMock,
    DictsClientMock,
    DictsWithStructsClientMock,
    DictsWithArraysClientMock,
    DictKeysClientMock,
    EnumsClientMock,
    EnumsWithArraysClientMock,
    EnumsWithDictsClientMock,
    EnumsWithStructsClientMock,
    QmlInstantiationClientMock,
)

def get_mock_client(interface):
    match interface:
        case 'Minimal':
            return MinimalClientMock()
        case 'WithArgs':
            return WithArgsClientMock()
        case 'Primitives':
            return PrimitivesClientMock()
        case 'Structs':
            return StructsClientMock()
        case 'Arrays':
            return ArraysClientMock()
        case 'ArraysWithStructs':
            return ArraysWithStructsClientMock()
        case 'Dictionaries':
            return DictsClientMock()
        case 'DictsWithStructs':
            return DictsWithStructsClientMock()
        case 'DictsWithArrays':
            return DictsWithArraysClientMock()
        case 'DictKeys':
            return DictKeysClientMock()
        case 'Enums':
            return EnumsClientMock()
        case 'EnumsWithArrays':
            return EnumsWithArraysClientMock()
        case 'EnumsWithDicts':
            return EnumsWithDictsClientMock()
        case 'EnumsWithStructs':
            return EnumsWithStructsClientMock()
        case 'QmlInstantiation':
            return QmlInstantiationClientMock()
        case _:
            assert False, f"Unknown interface '{interface}'"