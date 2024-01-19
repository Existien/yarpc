from python_mocks import BackendWithArgsInterfaceMock
from unittest.mock import AsyncMock
import asyncio

def get_with_args_mock():
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
