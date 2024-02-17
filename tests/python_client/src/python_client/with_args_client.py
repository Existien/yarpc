from .with_args_gen.with_args_client import WithArgsClient
import asyncio

async def with_args_loop(client: WithArgsClient):
    i=0
    while True:
        await asyncio.sleep(1)
        await client.Notify("Just bumped")
        total = await client.Order("Thingy", i, 3.5)
        print(f"Total: {total}")
        i = i+1
        await client.set_Speed(await client.get_Speed() + 0.1)
        print(f"Props: {await client.get_all_properties()}")

def get_with_args_client():
    client = WithArgsClient()
    def on_notified(message: str):
        print(f"Notification emitted: {message}")
    client.on_Notified(on_notified)
    def on_order_received(item: str, amount: int, price_per_item: float):
        print(f"Order received: {item} - {amount} x {price_per_item}")
    client.on_OrderReceived(on_order_received)
    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)
    return client, with_args_loop(client)