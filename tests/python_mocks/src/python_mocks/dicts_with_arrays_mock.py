from python_mocks import BackendDictsWithArraysInterfaceMock
from unittest.mock import AsyncMock
from typing import Dict, Dict, List, List

def get_dicts_with_arrays_mock():
    service = BackendDictsWithArraysInterfaceMock(
        DictArrayProperty={
            "A": [{"AA1": 11, "AA2": 12}, {"AB1": 21, "AB2": 22}],
            "B": [{"BA1": 11, "BA2": 12}, {"BB1": 21, "BB2": 22}],
        }
    )

    async def dict_with_arrays_method_handler(numbers: Dict[str, List[Dict[str, int]]]) -> Dict[str, List[Dict[str, int]]]:
        service.DictsArraySignal(numbers)
        return numbers
    service.mock.DictsArrayMethod = AsyncMock(wraps=dict_with_arrays_method_handler)

    return service