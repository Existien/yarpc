from .arrays_gen.arrays_interface import ArraysInterface
from .arrays_gen.backend_arrays_client import BackendArraysClient
from typing import Sequence
import asyncio

class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendArraysClient):
        self._backend = backend

    async def get_ArrayProperty(self):
        return await self._backend.get_ArrayProperty()

    async def set_ArrayProperty(self, value):
        return await self._backend.set_ArrayProperty(value)


def get_arrays_service_and_backend_client():
    backend_client = BackendArraysClient()
    service = ArraysInterface(
        property_provider=ProxyProperties(backend_client)
    )

    async def array_method_handler(array: Sequence[Sequence[int]]):
        return await backend_client.ArrayMethod(array)
    service.on_ArrayMethod(array_method_handler)

    def on_array_signal(values: list):
        service.ArraySignal(values)
    backend_client.on_ArraySignal(on_array_signal)

    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    return service, backend_client