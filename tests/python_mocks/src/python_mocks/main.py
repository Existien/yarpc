from python_mocks import BackendMinimalInterfaceMock, Connection
from unittest.mock import AsyncMock
import asyncio

def main():
    service = BackendMinimalInterfaceMock()
    async def bump_handler():
        await asyncio.sleep(1)
        service.Bumped()
        print("Got Bumped")

    service.mock.Bump = AsyncMock(wraps=bump_handler)
    print("Python mock service running")
    asyncio.run(Connection.run(service))

if __name__ == "__main__":
    main()