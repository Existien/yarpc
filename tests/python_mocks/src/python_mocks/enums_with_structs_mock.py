from python_mocks import BackendEnumsWithStructsInterfaceMock, EnumStruct, Color
from unittest.mock import AsyncMock

def get_enums_with_structs_mock():
    wheel = {
        Color.RED: Color.GREEN,
        Color.BLUE: Color.ORANGE,
        Color.GREEN: Color.RED,
        Color.ORANGE: Color.BLUE
    }
    service = BackendEnumsWithStructsInterfaceMock(
        EnumProperty=EnumStruct(
            color=Color.RED,
            colorArray=[Color.RED, Color.GREEN, Color.BLUE],
            colorDict=wheel,
        )
    )

    async def enum_method_handler(color: EnumStruct) -> EnumStruct:

        service.EnumSignal(color)
        retVal = EnumStruct(
            color=wheel[color.color],
            colorArray=[wheel[x] for x in color.colorArray],
            colorDict=color.colorDict
        )
        return retVal
    service.mock.EnumMethod = AsyncMock(wraps=enum_method_handler)
    return service