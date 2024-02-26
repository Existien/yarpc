from .dicts_gen.dicts_with_arrays_client import DictsWithArraysClient
import random
import asyncio

async def dicts_with_arrays_loop(client: DictsWithArraysClient):
    random.seed()
    while True:
        sa = {
            "1": [{
                f"{i}{j}": random.randint(0,100) for j in range(0,3)
            } for i in range(0,2)],
            "2": [{
                f"{i}{j}": random.randint(0,100) for j in range(0,3)
            } for i in range(0,2)],
        }
        result = await client.DictsArrayMethod(sa)
        print(f"DwA: {result}")
        previous = await client.get_DictArrayProperty()
        print(f"Previous prop: {previous}")
        await client.set_DictArrayProperty(sa)
        print(f"Current Props: {await client.get_all_properties()}")
        await asyncio.sleep(3)

def get_dicts_with_arrays_client():
    client = DictsWithArraysClient()

    def on_dict_array_signal(numbers):
        print(f"DictArraySignal: {numbers}")
    client.on_DictsArraySignal(on_dict_array_signal)

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    return client, dicts_with_arrays_loop(client)
