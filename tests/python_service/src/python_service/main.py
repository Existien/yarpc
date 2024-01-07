from .gen.minimal_service import MinimalServiceInterface
from .gen.minimal_client import MinimalClient
import asyncio

async def run():
    service = MinimalServiceInterface()
    client = MinimalClient()

    async def bump_handler():
        return await client.Bump()

    def on_bumped():
        service.Bumped()
        print("Bump emitted")

    service.on_Bump(bump_handler)
    client.on_Bumped(on_bumped)

    print("Service running")

    await asyncio.gather(
        service.run(),
        client.run()
    )

def main():

    asyncio.run(run())

if __name__ == "__main__":
    main()