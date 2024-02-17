from python_mocks import BackendArraysWithStructsInterfaceMock, ArraysWithStructsClientMock, SimonsArray, StructArray
from unittest.mock import AsyncMock
from typing import Sequence

__previous: Sequence[SimonsArray] = []

def get_arrays_with_structs_mock():
    service = BackendArraysWithStructsInterfaceMock(
        ArrayStructProperty=[StructArray(numbers=[[1], [2,3]]), StructArray(numbers=[[4,5],[6]])]
    )

    async def array_with_struct_method_handler(numbers: Sequence[StructArray]):
        service.ArrayStructSignal(numbers)
        __previous.append(SimonsArray(numbers=numbers))
        return __previous
    service.mock.ArrayStructMethod = AsyncMock(wraps=array_with_struct_method_handler)

    return service