from .dicts_gen.dicts_client import DictsClient
import asyncio
import random

async def dicts_loop(client: DictsClient):
    random.seed()
    names = ["First", "Second", "Third"]
    while True:
        knv = { n: random.randint(0, 100) for n in names }
        ret = await client.DictMethod(knv)
        print(f" Dicts: {ret}")
        await asyncio.sleep(3)
        previous = await client.get_DictProperty()
        print(f"Previous prop: {previous}")
        await client.set_DictProperty(knv)
        print(f"Current Props: {await client.get_all_properties()}")

def get_dicts_client():
    client = DictsClient()

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    def on_dict_signal(v):
        print(f"DictSignal received: {v}")
    client.on_DictSignal(on_dict_signal)

    return client, dicts_loop(client)