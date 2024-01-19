from python_mocks import BackendMinimalInterfaceMock
from unittest.mock import AsyncMock
import asyncio

def get_minimal_mock():
    service = BackendMinimalInterfaceMock()
    async def bump_handler():
        await asyncio.sleep(1)
        service.Bumped()
        print("Got Bumped")
    service.mock.Bump = AsyncMock(wraps=bump_handler)
    return service