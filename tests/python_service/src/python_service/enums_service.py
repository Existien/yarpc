from .enums_gen.enums_interface import EnumsInterface
from .enums_gen.backend_enums_client import BackendEnumsClient
from .enums_gen.color import Color

class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendEnumsClient):
        self._backend = backend

    async def get_EnumProperty(self):
        return await self._backend.get_EnumProperty()

    async def set_EnumProperty(self, value):
        return await self._backend.set_EnumProperty(value)

def get_enums_service_and_backend_client():
    backend_client = BackendEnumsClient()
    service = EnumsInterface(
        property_provider=ProxyProperties(backend_client)
    )

    def on_enum_signal(v):
        service.EnumSignal(v)
    backend_client.on_EnumSignal(on_enum_signal)

    async def enum_method_handler(value):
        return await backend_client.EnumMethod(value)
    service.on_EnumMethod(enum_method_handler)

    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    return service, backend_client