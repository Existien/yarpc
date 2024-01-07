from python_mocks import MinimalServiceInterfaceMock
from unittest.mock import AsyncMock
import asyncio

def main():
    service = MinimalServiceInterfaceMock()
    async def bump_handler():
        await asyncio.sleep(1)
        service.Bumped()
        print("Got Bumped")

    service.mock.Bump = AsyncMock(wraps=bump_handler)
    print("Python mock service running")
    asyncio.run(service.run())

if __name__ == "__main__":
    main()