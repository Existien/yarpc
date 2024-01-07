# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/primitives.yml
#   Object: Minimal

from dbus_next.aio import MessageBus
from dbus_next import Variant, DBusError

import asyncio


class MinimalClient():
    """
    A interface using signals and methods without args
    """

    def __init__(self):
        self._bus = None
        self._interface = None
        self._Bumped_handler = None

    async def run(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        self._bus = await MessageBus().connect()
        introspection = await self._bus.introspect(
            "com.yarpc.testservice",
            "/com/yarpc/testservice",
        )
        proxy_object = self._bus.get_proxy_object(
            "com.yarpc.testservice",
            "/com/yarpc/testservice",
            introspection
        )
        self._interface = proxy_object.get_interface(
            "com.yarpc.testservice.minimal"
        )

        if self._Bumped_handler:
            self._interface.on_bumped(self._Bumped_handler)
        await self._bus.wait_for_disconnect()

    def stop(self):
        """
        Closes the D-Bus connection
        """
        if self._bus:
            self._bus.disconnect()

    def on_Bumped(self, handler):
        """
        Set handler for Bumped signal

        Args:
            handler (Callable[[], None)
        """
        self._Bumped_handler = handler
        if self._interface:
            self._interface.on_bumped(self._Bumped_handler)

    async def Bump(self) -> None:
        """
        a simple method without args
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        return await self._interface.call_bump()
