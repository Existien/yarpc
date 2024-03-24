from .arrays_gen.arrays_with_structs_interface import ArraysWithStructsInterface
from .arrays_gen.backend_arrays_with_structs_client import BackendArraysWithStructsClient
from .arrays_gen.simons_array import StructArray
from typing import List
import asyncio


class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendArraysWithStructsClient):
        self._backend = backend

    async def get_ArrayStructProperty(self):
        return await self._backend.get_ArrayStructProperty()

    async def set_ArrayStructProperty(self, value):
        return await self._backend.set_ArrayStructProperty(value)


def get_arrays_with_struct_service_and_backend_client():
    backend_client = BackendArraysWithStructsClient()
    service = ArraysWithStructsInterface(
        property_provider=ProxyProperties(backend_client)
    )

    async def array_method_handler(array: List[StructArray]):
        return await backend_client.ArrayStructMethod(array)
    service.on_ArrayStructMethod(array_method_handler)

    def on_array_struct_signal(numbers: List[StructArray]):
        service.ArrayStructSignal(numbers)
    backend_client.on_ArrayStructSignal(on_array_struct_signal)

    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    return service, backend_client