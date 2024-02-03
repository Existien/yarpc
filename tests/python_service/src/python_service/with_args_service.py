from .basic_gen.with_args_interface import WithArgsInterface
from .basic_gen.backend_with_args_client import BackendWithArgsClient
import asyncio

class ProxyProperties:
    """Forwards all calls to backend interface"""
    def __init__(self, backend: BackendWithArgsClient):
        self._backend = backend

    async def get_Speed(self):
        return await self._backend.get_Speed()

    async def set_Speed(self, value):
        return await self._backend.set_Speed(value)

    async def get_Duration(self):
        return await self._backend.get_Duration()

    async def set_Duration(self, value):
        return await self._backend.set_Duration(value)

    async def get_Distance(self):
        return await self._backend.get_Distance()

    async def set_Distance(self, value):
        return await self._backend.set_Distance(value)


def get_with_args_service_and_backend_client():
    backend_client = BackendWithArgsClient()
    service = WithArgsInterface(
        property_provider=ProxyProperties(backend_client)
    )
    def on_properties_changed(properties):
        """Publish changed backend properties"""
        service.emit_properties_changed(properties)
    backend_client.on_properties_changed(on_properties_changed)

    async def notify_handler(message: str):
        return await backend_client.Notify(message)
    service.on_Notify(notify_handler)
    async def order_handler(item: str, amount, price_per_item):
        return await backend_client.Order(item, amount, price_per_item)
    service.on_Order(order_handler)

    def on_notified(message: str):
        service.Notified(message)
        print(f"Notification emitted: {message}")
    backend_client.on_Notified(on_notified)
    def on_order_received(item: str, amount: int, price_per_item: float):
        service.OrderReceived(item, amount, price_per_item)
        print(f"Order received: {item} - {amount} x {price_per_item}")
    backend_client.on_OrderReceived(on_order_received)

    return service, backend_client