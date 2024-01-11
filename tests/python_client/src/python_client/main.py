from .gen.minimal_client import MinimalClient
from .gen.with_args_client import WithArgsClient
import asyncio


def _configure_minimal_client():
    client = MinimalClient()
    def on_bumped():
        print('Bumped')
    client.on_Bumped(on_bumped)
    return client


def _configure_with_args_client():
    client = WithArgsClient()
    def on_notified(message: str):
        print(f"Notification emitted: {message}")
    def on_order_received(item: str, amount: int, price_per_item: float):
        print(f"Order received: {item} - {amount} x {price_per_item}")
    client.on_Notified(on_notified)
    client.on_OrderReceived(on_order_received)
    return client


async def runner():
    minimal_client = _configure_minimal_client()
    with_args_client = _configure_with_args_client

    async def bumper():
        i=0
        while True:
            await asyncio.sleep(1)
            await minimal_client.Bump()
            await with_args_client.Notify("Just bumped")
            total = await with_args_client.Order("Tingy", i, 3.5)
            print(f"Total: {total}")
            i+=1

    print("Client running")
    await asyncio.gather(
        minimal_client.connect(),
        with_args_client.connect(),
        bumper(),
    )


def main():
    asyncio.run(runner())

if __name__ == "__main__":
    main()