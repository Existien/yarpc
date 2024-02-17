from .arrays_gen.arrays_client import ArraysClient
import asyncio
import random

async def arrays_loop(client: ArraysClient):
    random.seed()
    while True:
        values_part1 = [random.randint(0, 100) for _ in range(0, 2)]
        values_part2 = [random.randint(0, 100) for _ in range(0, 3)]
        values = [values_part1, values_part2]
        print(f"           Array: {values}")
        normalized = await client.ArrayMethod(values)
        print(f"Normalized Array: {normalized}")

        change = []
        for v_seq, n_seq in zip(values, normalized):
            seq_change = [f"{v} -> {n}" for v,n in zip(v_seq, n_seq)]
            change.append(seq_change)
        # previous = await client.get_ArrayProperty()
        # print(f"Previous prop: {previous}")
        await client.set_ArrayProperty(change)
        print(f"Current Props: {await client.get_all_properties()}")
        await asyncio.sleep(3)

def get_arrays_client():
    client = ArraysClient()

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    def on_array_signal(values):
        print(f"ArraySignal received: {values}")
    client.on_ArraySignal(on_array_signal)
    return client, arrays_loop(client)