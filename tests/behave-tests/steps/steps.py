from behave import given, when, then
from behave.api.async_step import async_run_until_complete
import subprocess
import os
import asyncio
from python_mocks import MinimalClientMock, BackendMinimalInterfaceMock
from dbus_next.aio import MessageBus
from dbus_next.errors import DBusError


STEP_TIMEOUT = 5


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


@given("a mocked backend service '{name}'")
@async_run_until_complete(timeout=STEP_TIMEOUT)
async def step_impl(context, name):
    service = BackendMinimalInterfaceMock()
    service_task = asyncio.create_task(service.run())
    context.mocks[name] = service
    context.tasks.append(service_task)
    context.cleanup_actions.append(service.stop)
    await wait_for_dbus(
        bus_name="com.yarpc.backend",
        object_path="/com/yarpc/backend",
        interface_name="com.yarpc.backend.minimal"
    )


@given("a mocked python client '{name}'")
@async_run_until_complete(timeout=STEP_TIMEOUT)
async def step_impl(context, name):
    client = MinimalClientMock()
    client_task = asyncio.create_task(client.run())
    context.mocks[name] = client
    context.tasks.append(client_task)
    context.cleanup_actions.append(client.stop)
    await asyncio.sleep(0.1)


@given("a running python service")
@async_run_until_complete(timeout=STEP_TIMEOUT)
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


@when("the '{method}' method is called by '{name}'")
@async_run_until_complete(timeout=STEP_TIMEOUT)
async def step_impl(context, method, name):
    await getattr(context.mocks[name], method)()


@when("a '{signal}' signal is emitted by '{name}'")
@async_run_until_complete(timeout=STEP_TIMEOUT)
async def step_impl(context, signal, name):
    getattr(context.mocks[name], signal)()


@then("'{name}' receives a '{method}' method call")
@async_run_until_complete(timeout=STEP_TIMEOUT)
async def step_impl(context, name, method):
    service = context.mocks[name]
    mock = getattr(service.mock, method)
    while mock.await_count == 0:
        await asyncio.sleep(0.1)
    mock.reset_mock()


@then("'{name}' receives a '{signal}' signal")
@async_run_until_complete(timeout=STEP_TIMEOUT)
async def step_impl(context, name, signal):
    client = context.mocks[name]
    mock = getattr(client.mock, signal)
    while mock.call_count == 0:
        await asyncio.sleep(0.1)
    mock.reset_mock()