from .structs_gen.structs_client import StructsClient, SimpleStruct, Item
import asyncio

async def structs_loop(client: StructsClient):
    i=0
    while True:
        await asyncio.sleep(3)
        reply = await client.SendStruct(SimpleStruct(
            item=Item(
                name="Trash",
                price=1.5,
            ),
            amount=i,
        ))
        print(f"SendTrash reply: {reply}")
        current = await client.get_Simple()
        await client.set_Simple(SimpleStruct(
            item=Item(
                name=current.item.name,
                price=current.item.price+0.5,
            ),
            amount=current.amount,
        ))
        print(f"Props: {await client.get_all_properties()}")
        i += 1

def get_structs_client():
    client = StructsClient()
    def on_struct_received(struct: SimpleStruct, totalCosts: float):
        print(f"Struct reveived: {struct} which costs {totalCosts}")
    client.on_StructReceived(on_struct_received)
    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)
    return client, structs_loop(client)