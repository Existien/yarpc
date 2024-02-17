from python_mocks import BackendArraysInterfaceMock
from unittest.mock import AsyncMock
from typing import Sequence
import asyncio

def normalize_array(numbers: Sequence[int]) -> Sequence[float]:
    if not numbers:
        return []
    largest = max(numbers)
    if largest == 0:
        return numbers
    normalized = list(map(lambda x: x/largest, numbers))
    return normalized

def get_arrays_mock():
    service = BackendArraysInterfaceMock(
        ArrayProperty=[["Foo", "Bar"], ["Baz"]],
    )

    async def array_method_handler(numbers: Sequence[Sequence[int]]):
        result = []
        for seq in numbers:
            result.append(normalize_array(seq))
        service.ArraySignal(result)
        return result
    service.mock.ArrayMethod = AsyncMock(wraps=array_method_handler)

    return service