from python_mocks import (
    BackendStructsInterfaceMock,
    SimpleStruct, Item
)
from unittest.mock import AsyncMock
import asyncio

def get_structs_mock():
    service = BackendStructsInterfaceMock(
        Simple=SimpleStruct(Item("Bob", 0.5), 1)
    )

    async def send_struct_handler(simpleStruct: SimpleStruct) -> SimpleStruct:
        total = simpleStruct.amount * simpleStruct.item.price
        service.StructReceived(simpleStruct, total)
        print(f"Got {simpleStruct} ... add it to the pile")
        simpleStruct.amount += 1
        return simpleStruct
    service.mock.SendStruct = AsyncMock(wraps=send_struct_handler)

    async def on_simple_changed(value: SimpleStruct, props: dict):
        print(f"New Simple: {value}")
        props["Simple"] = value
        return props
    service.on_Simple_changed(on_simple_changed)

    return service
