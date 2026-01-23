import asyncio
from dbus_next.aio import MessageBus
from dbus_next.errors import DBusError

async def wait_for_call(mock):
    while mock.await_count == 0:
        await asyncio.sleep(0.1)

async def wait_for_signal(mock):
    while mock.call_count == 0:
        await asyncio.sleep(0.1)


async def wait_for_dbus(bus_name, object_path, interface_name, timeout_in_s=5):
    bus = await MessageBus().connect()
    interface = None
    time_taken = 0
    while not interface:
        try:
            introspection = await bus.introspect(bus_name, object_path)
            proxy_object = bus.get_proxy_object(bus_name, object_path, introspection)
            interface = proxy_object.get_interface(interface_name)
        except DBusError:
            pass
        if not interface:
            if time_taken > timeout_in_s:
                raise RuntimeError(f"Could not find D-Bus interface with bus name '{bus_name}', object path '{object_path}' and interface '{interface_name}'")
            await asyncio.sleep(0.1)
            time_taken += 0.1