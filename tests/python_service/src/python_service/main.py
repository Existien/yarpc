from .gen.minimal_interface import MinimalInterface
from .gen.with_args_interface import WithArgsInterface
from .gen.backend_minimal_client import BackendMinimalClient
from .gen.backend_with_args_client import BackendWithArgsClient
from .gen.connection import Connection
import asyncio


def _configure_minimal_interface():
    service = MinimalInterface()
    backend_client = BackendMinimalClient()
    async def bump_handler():
        return await backend_client.Bump()
    def on_bumped():
        service.Bumped()
        print("Bump emitted")
    service.on_Bump(bump_handler)
    backend_client.on_Bumped(on_bumped)
    return service, backend_client


def _configure_with_args_interface():
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


async def run():
    minimal_service, minimal_backend_client = _configure_minimal_interface()
    with_args_service, with_args_backend_client = _configure_with_args_interface()

    print("Service running")
    _, pending = await asyncio.wait(
        map(lambda x: asyncio.create_task(x), [
            minimal_backend_client.connect(),
            with_args_backend_client.connect(),
            Connection.run(minimal_service, with_args_service),
        ]),
        return_when=asyncio.FIRST_EXCEPTION
    )
    for task in pending:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

def main():

    asyncio.run(run())

if __name__ == "__main__":
    main()