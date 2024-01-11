from python_mocks import (
    BackendMinimalInterfaceMock,
    BackendWithArgsInterfaceMock,
    Connection
)
from unittest.mock import AsyncMock
import asyncio


def _configure_minimal_mock():
    service = BackendMinimalInterfaceMock()
    async def bump_handler():
        await asyncio.sleep(1)
        service.Bumped()
        print("Got Bumped")
    service.mock.Bump = AsyncMock(wraps=bump_handler)
    return service


def _configure_with_args_mock():
    service = BackendWithArgsInterfaceMock()
    async def notify_handler(message):
        await asyncio.sleep(0.5)
        service.Notified(message)
    async def order_handler(item, amount, pricePerItem):
        await asyncio.sleep(1)
        service.OrderReceived(item, amount, pricePerItem)
        return amount * pricePerItem
    service.mock.Notify = AsyncMock(wraps=notify_handler)
    service.mock.Order = AsyncMock(wraps=order_handler)
    return service


def main():
    minimal_service = _configure_minimal_mock()
    with_args_service = _configure_with_args_mock()

    print("Python mock service running")
    asyncio.run(Connection.run(minimal_service, with_args_service))

if __name__ == "__main__":
    main()