from .gen.with_args_interface import WithArgsInterface
from .gen.backend_with_args_client import BackendWithArgsClient

def get_with_args_service_and_backend_client():
    service = WithArgsInterface()
    backend_client = BackendWithArgsClient()
    async def notify_handler(message: str):
        return await backend_client.Notify(message)
    async def order_handler(item: str, amount, price_per_item):
        return await backend_client.Order(item, amount, price_per_item)
    def on_notified(message: str):
        service.Notified(message)
        print(f"Notification emitted: {message}")
    def on_order_received(item: str, amount: int, price_per_item: float):
        service.OrderReceived(item, amount, price_per_item)
        print(f"Order received: {item} - {amount} x {price_per_item}")
    service.on_Notify(notify_handler)
    service.on_Order(order_handler)
    backend_client.on_Notified(on_notified)
    backend_client.on_OrderReceived(on_order_received)
    return service, backend_client