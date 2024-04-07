# Generated by YARPC
# Version:  0.1.0+editable
# Definition:
#   File: /workspace/tests/definitions/04.1_arrays.yml
#   Object: Arrays
#   Template: py/bus.j2

from dbus_next.aio import MessageBus
import asyncio
import sys


class Connection:
    """
    Singleton that manages the D-Bus connection
    """
    _bus = None

    @classmethod
    async def bus(cls) -> MessageBus:
        """
        Connects to D-Bus, if not already done and returns the Bus.

        Returns:
            MessageBus: the connected bus
        """
        if not cls._bus:
            cls._bus = await MessageBus().connect()
        return cls._bus

    @classmethod
    def close(cls):
        """
        Closes the D-Bus connection
        """
        if cls._bus:
            cls._bus.disconnect()
            cls._bus = None

    @classmethod
    async def run(cls, *interfaces):
        """
        Starts connection, providing the passed interfaces

        Args:
            interfaces: interfaces to service
        """
        try:
            bus = await cls.bus()
            for interface in interfaces:
                bus.export(interface.object_path, interface.interface)
            await bus.request_name("com.yarpc.testservice")
            await bus.wait_for_disconnect()
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)

