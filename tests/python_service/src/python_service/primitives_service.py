from .with_args_gen.primitives_interface import PrimitivesInterface
from .with_args_gen.backend_primitives_client import BackendPrimitivesClient

def get_primitives_service_and_backend_client():
    service = PrimitivesInterface()
    backend_client = BackendPrimitivesClient()
    async def uint8_method_handler(value):
        return await backend_client.Uint8Method(value)
    service.on_Uint8Method(uint8_method_handler)
    async def bool_method_handler(value):
        return await backend_client.BoolMethod(value)
    service.on_BoolMethod(bool_method_handler)
    async def int16_method_handler(value):
        return await backend_client.Int16Method(value)
    service.on_Int16Method(int16_method_handler)
    async def uint16_method_handler(value):
        return await backend_client.Uint16Method(value)
    service.on_Uint16Method(uint16_method_handler)
    async def int32_method_handler(value):
        return await backend_client.Int32Method(value)
    service.on_Int32Method(int32_method_handler)
    async def uint32_method_handler(value):
        return await backend_client.Uint32Method(value)
    service.on_Uint32Method(uint32_method_handler)
    async def int64_method_handler(value):
        return await backend_client.Int64Method(value)
    service.on_Int64Method(int64_method_handler)
    async def uint64_method_handler(value):
        return await backend_client.Uint64Method(value)
    service.on_Uint64Method(uint64_method_handler)
    async def double_method_handler(value):
        return await backend_client.DoubleMethod(value)
    service.on_DoubleMethod(double_method_handler)
    async def string_method_handler(value):
        return await backend_client.StringMethod(value)
    service.on_StringMethod(string_method_handler)

    def on_uint8_signal(value):
        service.Uint8Signal(value)
    backend_client.on_Uint8Signal(on_uint8_signal)
    def on_bool_signal(value):
        service.BoolSignal(value)
    backend_client.on_BoolSignal(on_bool_signal)
    def on_int16_signal(value):
        service.Int16Signal(value)
    backend_client.on_Int16Signal(on_int16_signal)
    def on_uint16_signal(value):
        service.Uint16Signal(value)
    backend_client.on_Uint16Signal(on_uint16_signal)
    def on_int32_signal(value):
        service.Int32Signal(value)
    backend_client.on_Int32Signal(on_int32_signal)
    def on_uint32_signal(value):
        service.Uint32Signal(value)
    backend_client.on_Uint32Signal(on_uint32_signal)
    def on_int64_signal(value):
        service.Int64Signal(value)
    backend_client.on_Int64Signal(on_int64_signal)
    def on_uint64_signal(value):
        service.Uint64Signal(value)
    backend_client.on_Uint64Signal(on_uint64_signal)
    def on_double_signal(value):
        service.DoubleSignal(value)
    backend_client.on_DoubleSignal(on_double_signal)
    def on_string_signal(value):
        service.StringSignal(value)
    backend_client.on_StringSignal(on_string_signal)

    return service, backend_client
