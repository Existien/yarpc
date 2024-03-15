from .enums_gen.enum_with_structs_client import EnumWithStructsClient, Color, EnumStruct
import asyncio
import random

async def enums_loop(client: EnumWithStructsClient):
    random.seed()
    while True:
        struct = EnumStruct(
            color=Color(random.randint(0, 3)),
            colorArray=[Color(random.randint(0, 3)) for _ in range(0,3)],
            colorDict={
                Color.RED: Color(random.randint(0, 3)),
                Color.GREEN: Color(random.randint(0, 3)),
                Color.BLUE: Color(random.randint(0, 3)),
                Color.ORANGE: Color(random.randint(0, 3)),
            }
        )
        ret = await client.EnumMethod(struct)
        print(f"EnumStruct: {struct}\nReturnValue: {ret}")
        await asyncio.sleep(3)
        prev_prop = await client.get_EnumProperty()
        print(f"Previous prop: {prev_prop}")
        await client.set_EnumProperty(ret)
        print(f"Current Props: {await client.get_all_properties()}")

def get_enums_with_structs_client():
    client = EnumWithStructsClient()

    def on_properties_changed(props):
        print(f"Changed properties: {props}")
    client.on_properties_changed(on_properties_changed)

    def on_enums_signal(v):
        print(f"EnumSignal received: {v}")
    client.on_EnumSignal(on_enums_signal)

    return client, enums_loop(client)