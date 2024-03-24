from .dicts_gen.dicts_interface import DictsInterface
from .dicts_gen.backend_dicts_client import BackendDictsClient
from typing import Dict, Dict
import asyncio

class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendDictsClient):
        self._backend = backend

    async def get_DictProperty(self):
        return await self._backend.get_DictProperty()

    async def set_DictProperty(self, value):
        return await self._backend.set_DictProperty(value)

def get_dicts_service_and_backend_client():
    backend_client = BackendDictsClient()
    service = DictsInterface(
        property_provider=ProxyProperties(backend_client)
    )

    def on_dict_signal(v):
        service.DictSignal(v)
    backend_client.on_DictSignal(on_dict_signal)

    async def dict_method_handler(keysNValues):
        return await backend_client.DictMethod(keysNValues)
    service.on_DictMethod(dict_method_handler)

    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    return service, backend_client