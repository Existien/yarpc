from .gen.minimal_interface import MinimalInterface
from .gen.with_args_interface import WithArgsInterface
from .gen.backend_minimal_client import BackendMinimalClient
from .gen.connection import Connection
import asyncio

async def run():
    minimal_service = MinimalInterface()
    with_args_service = WithArgsInterface()
    minimal_backend_client = BackendMinimalClient()

    async def bump_handler():
        return await minimal_backend_client.Bump()

    def on_bumped():
        minimal_service.Bumped()
        print("Bump emitted")

    minimal_service.on_Bump(bump_handler)
    minimal_backend_client.on_Bumped(on_bumped)

    async def on_notify():
        with_args_service.Notified()
        print("Notification emitted")

    async def on_order():
        with_args_service.OrderReceived()
        print("Order received")

    with_args_service.on_Notify(on_notify)
    with_args_service.on_Order(on_order)

    print("Service running")

    _, pending = await asyncio.wait(
        map(lambda x: asyncio.create_task(x), [
            minimal_backend_client.connect(),
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