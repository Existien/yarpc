from .structs_gen.backend_structs_client import BackendStructsClient
from .structs_gen.structs_interface import StructsInterface, SimpleStruct
import asyncio

class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendStructsClient):
        self._backend = backend

    async def get_Simple(self):
        return await self._backend.get_Simple()

    async def set_Simple(self, value):
        return await self._backend.set_Simple(value)

def get_structs_service_and_backend_client():
    backend_client = BackendStructsClient()
    service = StructsInterface(
        property_provider=ProxyProperties(backend_client)
    )
    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    async def send_struct_handler(arg: SimpleStruct):
        return await backend_client.SendStruct(arg)
    service.on_SendStruct(send_struct_handler)

    def on_struct_received(struct: SimpleStruct, totalCosts: float):
        print(f"Struct received {struct} with total cost of {totalCosts}")
        service.StructReceived(struct, totalCosts)
    backend_client.on_StructReceived(on_struct_received)

    return service, backend_client