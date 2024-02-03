from .basic_gen.minimal_client import MinimalClient
import asyncio

async def minimal_loop(client):
    while True:
        await asyncio.sleep(1)
        await client.Bump()

def get_minimal_client():
    client = MinimalClient()
    def on_bumped():
        print('Bumped')
    client.on_Bumped(on_bumped)
    return client, minimal_loop(client)