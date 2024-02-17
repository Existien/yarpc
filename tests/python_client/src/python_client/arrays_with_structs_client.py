from .arrays_gen.arrays_with_structs_client import ArraysWithStructsClient, StructArray, SimonsArray
import random
import asyncio

async def arrays_with_structs_loop(client: ArraysWithStructsClient):
    random.seed()
    while True:
        sa = [StructArray(numbers = [
            [random.randint(0,100) for _ in range(0,3)] for _ in range(0,3)
        ]) for _ in range(0,2)]
        result = await client.ArrayStructMethod(sa)
        print(f"AwS: {result}")
        previous = await client.get_ArrayStructProperty()
        print(f"Previous prop: {previous}")
        await client.set_ArrayStructProperty(sa)
        print(f"Current Props: {await client.get_all_properties()}")
        await asyncio.sleep(3)

def get_arrays_with_struct_client():
    client = ArraysWithStructsClient()

    def on_array_struct_signal(numbers):
        print(f"ArrayStructSignal: {numbers}")
    client.on_ArrayStructSignal(on_array_struct_signal)

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    return client, arrays_with_structs_loop(client)
