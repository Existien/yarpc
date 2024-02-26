from python_mocks import BackendDictsWithStructsInterfaceMock, SimonsDict, StructDict
from unittest.mock import AsyncMock
from typing import Mapping, Dict

__count = 0
__previous: Dict[str, SimonsDict] = {}

def get_dicts_with_structs_mock():
    service = BackendDictsWithStructsInterfaceMock(
        DictStructProperty={
            "first": StructDict(
                numbers={
                    "1": {"Fizz": 3, "Buzz": 5},
                    "2": {"One": 1, "Two": 2},
                },
            ),
            "second": StructDict(
                numbers={
                    "Legs": {"Fish": 0, "Dog": 4, "Ant": 6},
                    "Wings": {"Fish": 0, "Dog": 0, "Ant": 2},
                }
            ),
        },
    )

    async def dict_with_struct_method_handler(numbers: Mapping[str, StructDict]):
        global __count
        global __previous
        service.DictStructSignal(numbers)
        __previous[f"{__count}"] = SimonsDict(numbers=numbers)
        __count += 1
        return __previous
    service.mock.DictsStructMethod = AsyncMock(wraps=dict_with_struct_method_handler)

    return service