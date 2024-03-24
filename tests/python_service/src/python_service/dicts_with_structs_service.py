from .dicts_gen.dicts_with_structs_interface import DictsWithStructsInterface
from .dicts_gen.backend_dicts_with_structs_client import BackendDictsWithStructsClient
from .dicts_gen.simons_dict import StructDict
from typing import Dict
import asyncio


class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendDictsWithStructsClient):
        self._backend = backend

    async def get_DictStructProperty(self):
        return await self._backend.get_DictStructProperty()

    async def set_DictStructProperty(self, value):
        return await self._backend.set_DictStructProperty(value)


def get_dicts_with_struct_service_and_backend_client():
    backend_client = BackendDictsWithStructsClient()
    service = DictsWithStructsInterface(
        property_provider=ProxyProperties(backend_client)
    )

    async def dict_method_handler(array: Dict[str, StructDict]):
        return await backend_client.DictsStructMethod(array)
    service.on_DictsStructMethod(dict_method_handler)

    def on_dict_struct_signal(numbers: Dict[str, StructDict]):
        service.DictStructSignal(numbers)
    backend_client.on_DictStructSignal(on_dict_struct_signal)

    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    return service, backend_client