from python_mocks import BackendDictsInterfaceMock
from unittest.mock import AsyncMock
from typing import Mapping, Dict
import asyncio

def get_dicts_mock():
    service = BackendDictsInterfaceMock(
        DictProperty={"Fizz": 3, "Buzz": 5}
    )

    async def dict_method_handler(keysNValues: Mapping[str, int]) -> Dict[str, str]:
        service.DictSignal(keysNValues)
        return {
            k: str(v) for k, v in keysNValues.items()
        }
    service.mock.DictMethod = AsyncMock(wraps=dict_method_handler)
    return service