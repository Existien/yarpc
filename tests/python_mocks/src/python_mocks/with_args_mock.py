from python_mocks import BackendWithArgsInterfaceMock
from unittest.mock import AsyncMock
import asyncio

def get_with_args_mock():
    service = BackendWithArgsInterfaceMock(
        Distance=100,
        Speed=10.0,
        Duration=10.0,
    )
    async def notify_handler(message):
        await asyncio.sleep(0.5)
        service.Notified(message)
    async def order_handler(item, amount, pricePerItem):
        await asyncio.sleep(1)
        service.OrderReceived(item, amount, pricePerItem)
        return amount * pricePerItem
    service.mock.Notify = AsyncMock(wraps=notify_handler)
    service.mock.Order = AsyncMock(wraps=order_handler)

    async def on_duration_changed(_value: float, _props: dict):
        print("This should not be called ever!")
    service.on_Duration_changed(on_duration_changed)
    async def on_speed_changed(value: float, props: dict):
        props["Speed"] = value
        props["Duration"] = props["Distance"] / props["Speed"]
        print(f"New Speed: {value} m/s")
        return props
    service.on_Speed_changed(on_speed_changed)
    async def on_distance_changed(value: float, props: dict):
        props["Distance"] = value
        props["Duration"] = props["Distance"] / props["Speed"]
        print(f"New Distance: {value} m")
        return props
    service.on_Distance_changed(on_distance_changed)

    return service
