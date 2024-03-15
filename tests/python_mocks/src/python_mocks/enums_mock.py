from python_mocks import BackendEnumsInterfaceMock, Color
from unittest.mock import AsyncMock

def get_enums_mock():
    service = BackendEnumsInterfaceMock(
        EnumProperty=Color.ORANGE
    )

    async def enum_method_handler(color: Color) -> Color:
        wheel = {
            Color.RED: Color.GREEN,
            Color.BLUE: Color.ORANGE,
            Color.GREEN: Color.RED,
            Color.ORANGE: Color.BLUE
        }
        service.EnumSignal(color)
        return wheel[color]
    service.mock.EnumMethod = AsyncMock(wraps=enum_method_handler)
    return service