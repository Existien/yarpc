from python_mocks import BackendPrimitivesInterfaceMock
from unittest.mock import AsyncMock

def get_primitives_mock():
    service = BackendPrimitivesInterfaceMock()
    async def uint8_method_handler(value):
        service.Uint8Signal(value)
    service.mock.Uint8Method = AsyncMock(wraps=uint8_method_handler)
    async def bool_method_handler(value):
        service.BoolSignal(value)
    service.mock.BoolMethod = AsyncMock(wraps=bool_method_handler)
    async def int16_method_handler(value):
        service.Int16Signal(value)
    service.mock.Int16Method = AsyncMock(wraps=int16_method_handler)
    async def uint16_method_handler(value):
        service.Uint16Signal(value)
    service.mock.Uint16Method = AsyncMock(wraps=uint16_method_handler)
    async def int32_method_handler(value):
        service.Int32Signal(value)
    service.mock.Int32Method = AsyncMock(wraps=int32_method_handler)
    async def uint32_method_handler(value):
        service.Uint32Signal(value)
    service.mock.Uint32Method = AsyncMock(wraps=uint32_method_handler)
    async def int64_method_handler(value):
        service.Int64Signal(value)
    service.mock.Int64Method = AsyncMock(wraps=int64_method_handler)
    async def uint64_method_handler(value):
        service.Uint64Signal(value)
    service.mock.Uint64Method = AsyncMock(wraps=uint64_method_handler)
    async def double_method_handler(value):
        service.DoubleSignal(value)
    service.mock.DoubleMethod = AsyncMock(wraps=double_method_handler)
    async def string_method_handler(value):
        service.StringSignal(value)
    service.mock.StringMethod = AsyncMock(wraps=string_method_handler)

    return service