from .dicts_gen.dicts_with_structs_client import DictsWithStructsClient, SimonsDict, StructDict
import random
import asyncio

async def dicts_with_structs_loop(client: DictsWithStructsClient):
    random.seed()
    while True:
        sd = {
            "1": StructDict(numbers = {
                f"{i}x": { f"{j}y": random.randint(0,100) for j in range(0,3)}
                for i in range(0,2)
            }),
            "2": StructDict(numbers = {
                f"{i}x": { f"{j}y": random.randint(0,100) for j in range(0,3)}
                for i in range(0,2)
            }),
        }
        result = await client.DictsStructMethod(sd)
        print(f"DwS: {result}")
        previous = await client.get_DictStructProperty()
        print(f"Previous prop: {previous}")
        await client.set_DictStructProperty(sd)
        print(f"Current Props: {await client.get_all_properties()}")
        await asyncio.sleep(3)

def get_dicts_with_struct_client():
    client = DictsWithStructsClient()

    def on_dict_struct_signal(numbers):
        print(f"DictStructSignal: {numbers}")
    client.on_DictStructSignal(on_dict_struct_signal)

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    return client, dicts_with_structs_loop(client)
