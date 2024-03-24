from python_mocks import BackendEnumsWithArraysInterfaceMock, Color
from unittest.mock import AsyncMock
from typing import List, List

def get_enums_with_arrays_mock():
    wheel = {
        Color.RED: Color.GREEN,
        Color.BLUE: Color.ORANGE,
        Color.GREEN: Color.RED,
        Color.ORANGE: Color.BLUE
    }
    service = BackendEnumsWithArraysInterfaceMock(
        EnumProperty=[Color.RED, Color.GREEN, Color.BLUE],
    )

    async def enum_method_handler(color: List[Color]) -> List[Color]:

        service.EnumSignal(color)
        return [wheel[c] for c in color]
    service.mock.EnumMethod = AsyncMock(wraps=enum_method_handler)
    return service