from .gen.with_args_client import WithArgsClient
import asyncio

async def with_args_loop(client: WithArgsClient):
    i=0
    while True:
        await asyncio.sleep(1)
        await client.Notify("Just bumped")
        total = await client.Order("Tingy", i, 3.5)
        print(f"Total: {total}")
        i+=1

def get_with_args_client():
    client = WithArgsClient()
    def on_notified(message: str):
        print(f"Notification emitted: {message}")
    def on_order_received(item: str, amount: int, price_per_item: float):
        print(f"Order received: {item} - {amount} x {price_per_item}")
    client.on_Notified(on_notified)
    client.on_OrderReceived(on_order_received)
    return client, with_args_loop(client)