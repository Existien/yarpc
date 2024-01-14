from behave import given, when, then
from behave.api.async_step import async_run_until_complete
import subprocess
import os
import asyncio
from python_mocks import (
    Connection,
    MinimalClientMock, BackendMinimalInterfaceMock,
    WithArgsClientMock, BackendWithArgsInterfaceMock,
    PrimitivesClientMock, BackendPrimitivesInterfaceMock,
)
from dbus_next.aio import MessageBus
from dbus_next.errors import DBusError


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


def cast(value: str, type: str):
    match type:
        case 'bool':
            match value:
                case 'True':
                    return True
                case 'False':
                    return False
                case _:
                    raise ValueError("Invalid boolean. Use 'True' or 'False'")
        case _:
            return __builtins__[type](value)


def table_to_args(table):
    args = []
    for row in table:
        args.append(cast(row['value'], row['type']))
    return args


def table_to_kwargs(table):
    kwargs = {}
    for row in table:
        kwargs[row['name']] = cast(row['value'], row['type'])
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
                service = BackendWithArgsInterfaceMock()
            case 'Primitives':
                service = BackendPrimitivesInterfaceMock()
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
            case _:
                assert False, f"Unknown interface '{interface}'"
        client_task = asyncio.create_task(client.connect())
        context.mocks[name] = client
        context.tasks.append(client_task)
        await asyncio.sleep(0.1)
    for row in context.table:
        await connect_to_interface(row['interface'], row['name'])


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