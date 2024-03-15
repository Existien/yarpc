from .enums_gen.enum_with_dicts_client import EnumWithDictsClient, Color
import asyncio
import random

async def enums_loop(client: EnumWithDictsClient):
    random.seed()
    while True:
        data = {
            Color.RED: Color(random.randint(0, 3)),
            Color.GREEN: Color(random.randint(0, 3)),
            Color.BLUE: Color(random.randint(0, 3)),
            Color.ORANGE: Color(random.randint(0, 3)),
        }
        ret = await client.EnumMethod(data)
        print(f"EnumArray: {data}\nReturnValue: {ret}")
        await asyncio.sleep(3)
        prev_prop = await client.get_EnumProperty()
        print(f"Previous prop: {prev_prop}")
        await client.set_EnumProperty(ret)
        print(f"Current Props: {await client.get_all_properties()}")

def get_enums_with_dicts_client():
    client = EnumWithDictsClient()

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    def on_enums_signal(v):
        print(f"EnumSignal received: {v}")
    client.on_EnumSignal(on_enums_signal)

    return client, enums_loop(client)