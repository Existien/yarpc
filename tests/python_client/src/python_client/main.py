from .gen.minimal_client import MinimalClient
import asyncio

async def runner():
    client = MinimalClient()

    def on_bumped():
        print('Bumped')

    async def bumper():
        while True:
            await asyncio.sleep(2)
            await client.Bump()

    client.on_Bumped(on_bumped)
    print("Client running")
    await asyncio.gather(
        client.connect(),
        bumper(),
    )


def main():
    asyncio.run(runner())

if __name__ == "__main__":
    main()