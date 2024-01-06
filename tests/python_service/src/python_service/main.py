from .gen.minimal_service import MinimalServiceInterface
import asyncio

def main():
    service = MinimalServiceInterface()

    async def bump_handler():
        print("Got bumped")
        service.Bumped()

    service.on_Bump(bump_handler)

    print("Service running")
    asyncio.run(service.run())

if __name__ == "__main__":
    main()