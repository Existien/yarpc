from behave import given, when, then
from behave.api.async_step import async_run_until_complete
import subprocess
import os
import asyncio
import json
from python_mocks import (
    Connection,
    MinimalClientMock, BackendMinimalInterfaceMock,
    WithArgsClientMock, BackendWithArgsInterfaceMock,
    PrimitivesClientMock, BackendPrimitivesInterfaceMock,
    StructsClientMock, BackendStructsInterfaceMock, SimpleStruct, Item,
    ArraysClientMock, BackendArraysInterfaceMock,
    ArraysWithStructsClientMock, BackendArraysWithStructsInterfaceMock, StructArray, SimonsArray,
    DictsClientMock, BackendDictsInterfaceMock,
    DictsWithStructsClientMock, BackendDictsWithStructsInterfaceMock, StructDict, SimonsDict,
    DictsWithArraysClientMock, BackendDictsWithArraysInterfaceMock,
    DictKeysClientMock, BackendDictKeysInterfaceMock,
    EnumsClientMock, BackendEnumsInterfaceMock, Color,
    EnumsWithArraysClientMock, BackendEnumsWithArraysInterfaceMock,
    EnumsWithDictsClientMock, BackendEnumsWithDictsInterfaceMock,
    EnumsWithStructsClientMock, BackendEnumsWithStructsInterfaceMock, EnumStruct,
)
from dbus_next.aio import MessageBus
from dbus_next.errors import DBusError


@given("a running python service")
@async_run_until_complete
async def step_impl(context):
    process = subprocess.Popen(
        args=["pdm", "run", "-p", "python_service", "service"],
        cwd="/workspace/tests",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    context.processes.append(process)
    await wait_for_dbus(
        bus_name="com.yarpc.testservice",
        object_path="/com/yarpc/testservice",
        interface_name="com.yarpc.testservice.minimal"
    )


async def wait_for_dbus(bus_name, object_path, interface_name):
    bus = await MessageBus().connect()
    interface = None
    while not interface:
        await asyncio.sleep(0.1)
        try:
            introspection = await bus.introspect(bus_name, object_path)
            proxy_object = bus.get_proxy_object(bus_name, object_path, introspection)
            interface = proxy_object.get_interface(interface_name)
        except DBusError:
            pass


def table_to_args(table):
    args = []
    for row in table:
        args.append(eval(row['value']))
    return args


def table_to_kwargs(table):
    kwargs = {}
    for row in table:
        kwargs[row['name']] = eval(row['value'])
    return kwargs


@given("a mocked backend service with the following interfaces")
@async_run_until_complete
async def step_impl(context):
    async def start_interface(interface, name):
        service = None
        match interface:
            case 'Minimal':
                service = BackendMinimalInterfaceMock()
            case 'WithArgs':
                service = BackendWithArgsInterfaceMock(
                    Speed=10.0,
                    Distance=200,
                    Duration=200/10.0,
                )
            case 'Primitives':
                service = BackendPrimitivesInterfaceMock()
            case 'Structs':
                service = BackendStructsInterfaceMock(
                    Simple=SimpleStruct(
                        Item(
                            name="Foo",
                            price=0.98,
                        ),
                        amount=42,
                    )
                )
            case 'Arrays':
                service=BackendArraysInterfaceMock(
                    ArrayProperty=[["Foo", "Bar"], ["Baz"]]
                )
            case 'ArraysWithStructs':
                service=BackendArraysWithStructsInterfaceMock(
                    ArrayStructProperty=[StructArray(numbers=[[1],[2]]),StructArray(numbers=[[3,4]])]
                )
            case 'Dictionaries':
                service=BackendDictsInterfaceMock(
                    DictProperty={"Fizz":3, "Buzz": 5}
                )
            case 'DictsWithStructs':
                service=BackendDictsWithStructsInterfaceMock(
                    DictStructProperty={
                        "first": StructDict(numbers={
                            "1": {"Fizz": 3, "Buzz": 5},
                            "2": {"One": 1, "Two": 2},
                        }),
                        "second": StructDict(numbers={
                            "Legs": {"Fish": 0, "Dog": 4, "Ant": 6},
                            "Wings": {"Fish": 0, "Dog": 0, "Ant": 2},
                        }),
                    }
                )
            case 'DictsWithArrays':
                service=BackendDictsWithArraysInterfaceMock(
                    DictArrayProperty={
                        "A": [{"AA1": 11, "AA2": 12}, {"AB1": 21, "AB2": 22}],
                        "B": [{"BA1": 11, "BA2": 12}, {"BB1": 21, "BB2": 22}],
                    }
                )
            case 'DictKeys':
                service=BackendDictKeysInterfaceMock()
            case 'Enums':
                service=BackendEnumsInterfaceMock(
                    EnumProperty=Color.GREEN
                )
            case 'EnumsWithArrays':
                service=BackendEnumsWithArraysInterfaceMock(
                    EnumProperty=[Color.RED, Color.GREEN, Color.BLUE]
                )
            case 'EnumsWithDicts':
                service=BackendEnumsWithDictsInterfaceMock(
                    EnumProperty={
                        Color.RED: Color.GREEN,
                        Color.GREEN: Color.RED,
                        Color.BLUE: Color.ORANGE,
                    }
                )
            case 'EnumsWithStructs':
                service=BackendEnumsWithStructsInterfaceMock(
                    EnumProperty=EnumStruct(
                        color=Color.GREEN,
                        colorArray=[Color.RED, Color.GREEN, Color.BLUE],
                        colorDict={
                            Color.RED: Color.GREEN,
                            Color.GREEN: Color.RED,
                            Color.BLUE: Color.ORANGE,
                        }
                    )
                )
            case _:
                assert False, f"Unknown interface '{interface}'"
        assert service is not None, f"Could not find service '{interface}'"
        service_task = asyncio.create_task(Connection.run(service))
        if name:
            context.mocks[name] = service
        context.tasks.append(service_task)
        context.cleanup_actions.append(Connection.close)
        await wait_for_dbus(
            bus_name="com.yarpc.backend",
            object_path="/com/yarpc/backend",
            interface_name=service.name
        )
    for row in context.table:
        await start_interface(row['interface'], row['name'])



@given("a mocked python client connecting to the following interfaces")
@async_run_until_complete
async def step_impl(context):
    async def connect_to_interface(interface, name):
        client = None
        match interface:
            case 'Minimal':
                client = MinimalClientMock()
            case 'WithArgs':
                client = WithArgsClientMock()
            case 'Primitives':
                client = PrimitivesClientMock()
            case 'Structs':
                client = StructsClientMock()
            case 'Arrays':
                client = ArraysClientMock()
            case 'ArraysWithStructs':
                client = ArraysWithStructsClientMock()
            case 'Dictionaries':
                client = DictsClientMock()
            case 'DictsWithStructs':
                client = DictsWithStructsClientMock()
            case 'DictsWithArrays':
                client = DictsWithArraysClientMock()
            case 'DictKeys':
                client = DictKeysClientMock()
            case 'Enums':
                client = EnumsClientMock()
            case 'EnumsWithArrays':
                client = EnumsWithArraysClientMock()
            case 'EnumsWithDicts':
                client = EnumsWithDictsClientMock()
            case 'EnumsWithStructs':
                client = EnumsWithStructsClientMock()
            case _:
                assert False, f"Unknown interface '{interface}'"
        client_task = asyncio.create_task(client.connect())
        context.mocks[name] = client
        context.tasks.append(client_task)
        await asyncio.sleep(0.1)
    for row in context.table:
        await connect_to_interface(row['interface'], row['name'])


@given("'{name}' replies to a '{method}' method call with the following return value")
@async_run_until_complete
async def step_impl(context, name, method):
    return_value = table_to_args(context.table)[0]
    assert name in context.mocks.keys(), f"Service {name} not found"
    service = context.mocks[name]
    mock = getattr(service.mock, method)
    mock.return_value = return_value


@when("the '{method}' method is called by '{name}'")
@async_run_until_complete
async def step_impl(context, method, name):
    assert name in context.mocks.keys(), f"Client {name} not found"
    return_value = await getattr(context.mocks[name], method)()
    context.last_return_values[name] = return_value


@then("'{name}' receives a return value of")
@async_run_until_complete
async def step_impl(context, name):
    expected = table_to_args(context.table)[0]
    actual = context.last_return_values[name]
    assert expected == actual, f"Expected return value {expected}, but got {actual}"
    context.last_return_values[name]= None


@when("a '{signal}' signal is emitted by '{name}'")
@async_run_until_complete
async def step_impl(context, signal, name):
    assert name in context.mocks.keys(), f"Service {name} not found"
    getattr(context.mocks[name], signal)()


@then("'{name}' receives a '{method}' method call")
@async_run_until_complete
async def step_impl(context, name, method):
    assert name in context.mocks.keys(), f"Service {name} not found"
    service = context.mocks[name]
    mock = getattr(service.mock, method)
    while mock.await_count == 0:
        await asyncio.sleep(0.1)
    mock.reset_mock()


@then("'{name}' receives a '{signal}' signal")
@async_run_until_complete
async def step_impl(context, name, signal):
    assert name in context.mocks.keys(), f"Client {name} not found"
    client = context.mocks[name]
    mock = getattr(client.mock, signal)
    while mock.call_count == 0:
        await asyncio.sleep(0.1)
    mock.reset_mock()


@when("the '{method}' method is called by '{name}' with the following parameters")
@async_run_until_complete
async def step_impl(context, method, name):
    kwargs = table_to_kwargs(context.table)
    assert name in context.mocks.keys(), f"Client {name} not found"
    return_value = await getattr(context.mocks[name], method)(**kwargs)
    context.last_return_values[name] = return_value


@then("'{name}' receives a '{method}' method call with the following parameters")
@async_run_until_complete
async def step_impl(context, name, method):
    assert name in context.mocks.keys(), f"Service {name} not found"
    service = context.mocks[name]
    mock = getattr(service.mock, method)
    while mock.await_count == 0:
        await asyncio.sleep(0.1)
    kwargs = table_to_kwargs(context.table)
    mock.assert_awaited_with(**kwargs)
    mock.reset_mock()


@when("a '{signal}' signal is emitted by '{name}' with the following parameters")
@async_run_until_complete
async def step_impl(context, signal, name):
    kwargs = table_to_kwargs(context.table)
    assert name in context.mocks.keys(), f"Service {name} not found"
    getattr(context.mocks[name], signal)(**kwargs)


@then("'{name}' receives a '{signal}' signal with the following parameters")
@async_run_until_complete
async def step_impl(context, name, signal):
    kwargs = table_to_kwargs(context.table)
    assert name in context.mocks.keys(), f"Client {name} not found"
    client = context.mocks[name]
    mock = getattr(client.mock, signal)
    while mock.call_count == 0:
        await asyncio.sleep(0.1)
    mock.called_once_with(**kwargs)
    mock.reset_mock()


@when("all properties are queried from '{name}'")
@async_run_until_complete
async def step_impl(context, name):
    assert name in context.mocks.keys(), f"Client {name} not found"
    client = context.mocks[name]
    return_value = await client.get_all_properties()
    context.last_return_values[name] = return_value


@when("the '{prop}' property is queried from '{name}'")
@async_run_until_complete
async def step_impl(context, name, prop):
    assert name in context.mocks.keys(), f"Client {name} not found"
    client = context.mocks[name]
    return_value = await getattr(client, f"get_{prop}")()
    context.last_return_values[name] = return_value


@when("the '{prop}' property is set by '{name}' to a value of")
@async_run_until_complete
async def step_impl(context, name, prop):
    value = table_to_args(context.table)[0]
    assert name in context.mocks.keys(), f"Client {name} not found"
    client = context.mocks[name]
    await getattr(client, f"set_{prop}")(value)


@then("'{name}' receives a property change signal with the following parameters")
@async_run_until_complete
async def step_impl(context, name):
    kwargs = table_to_kwargs(context.table)
    assert name in context.mocks.keys(), f"Client {name} not found"
    client = context.mocks[name]
    mock = client.mock.on_properties_changed
    while mock.call_count == 0:
        await asyncio.sleep(0.1)
    mock.called_once_with(kwargs)
    mock.reset_mock()