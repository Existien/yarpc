from .enums_gen.enum_client import EnumClient, Color
import asyncio
import random

async def enums_loop(client: EnumClient):
    random.seed()
    while True:
        color = Color(random.randint(0, 3))
        ret = await client.EnumMethod(color)
        print(f"Color: {color} - Compl.: {ret}")
        await asyncio.sleep(3)
        prev_prop = await client.get_EnumProperty()
        print(f"Previous prop: {prev_prop}")
        await client.set_EnumProperty(ret)
        print(f"Current Props: {await client.get_all_properties()}")

def get_enums_client():
    client = EnumClient()

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    def on_enums_signal(v):
        print(f"EnumSignal received: {v}")
    client.on_EnumSignal(on_enums_signal)

    return client, enums_loop(client)