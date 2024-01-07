from .gen.minimal_interface import MinimalInterface
from .gen.backend_minimal_client import BackendMinimalClient
import asyncio

async def run():
    service = MinimalInterface()
    backend_client = BackendMinimalClient()

    async def bump_handler():
        return await backend_client.Bump()

    def on_bumped():
        service.Bumped()
        print("Bump emitted")

    service.on_Bump(bump_handler)
    backend_client.on_Bumped(on_bumped)

    print("Service running")

    await asyncio.gather(
        service.run(),
        backend_client.run()
    )

def main():

    asyncio.run(run())

if __name__ == "__main__":
    main()