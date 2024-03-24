from python_mocks import BackendEnumsWithDictsInterfaceMock, Color
from unittest.mock import AsyncMock
from typing import Dict, Dict

def get_enums_with_dicts_mock():
    wheel = {
        Color.RED: Color.GREEN,
        Color.BLUE: Color.ORANGE,
        Color.GREEN: Color.RED,
        Color.ORANGE: Color.BLUE
    }
    service = BackendEnumsWithDictsInterfaceMock(
        EnumProperty=wheel,
    )

    async def enum_method_handler(color: Dict[Color, Color]) -> Dict[Color, Color]:

        service.EnumSignal(color)
        return {
            k: wheel[v] for k, v in color.items()
        }
    service.mock.EnumMethod = AsyncMock(wraps=enum_method_handler)
    return service