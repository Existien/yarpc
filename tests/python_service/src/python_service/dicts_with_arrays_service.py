from .dicts_gen.dicts_with_arrays_interface import DictsWithArraysInterface
from .dicts_gen.backend_dicts_with_arrays_client import BackendDictsWithArraysClient
from typing import Mapping, Sequence
import asyncio


class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendDictsWithArraysClient):
        self._backend = backend

    async def get_DictArrayProperty(self):
        return await self._backend.get_DictArrayProperty()

    async def set_DictArrayProperty(self, value):
        return await self._backend.set_DictArrayProperty(value)


def get_dicts_with_array_service_and_backend_client():
    backend_client = BackendDictsWithArraysClient()
    service = DictsWithArraysInterface(
        property_provider=ProxyProperties(backend_client)
    )

    async def dict_method_handler(array: Mapping[str, Sequence[Mapping[str, int]]]):
        return await backend_client.DictsArrayMethod(array)
    service.on_DictsArrayMethod(dict_method_handler)

    def on_dict_array_signal(numbers: Mapping[str, Sequence[Mapping[str, int]]]):
        service.DictsArraySignal(numbers)
    backend_client.on_DictsArraySignal(on_dict_array_signal)

    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    return service, backend_client