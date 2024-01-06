# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/primitives.yml
#   Object: Minimal

from dbus_next.aio import MessageBus
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next import Variant, DBusError

import asyncio

class MinimalServiceInterface(ServiceInterface):
    """
    A interface using signals and methods without args
    """

    def __init__(self):
        super().__init__("com.yarpc.testservice.minimal")
        self._Bump_handler = None

    async def run(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        bus = await MessageBus().connect()
        bus.export("/com/yarpc/testservice", self)
        await bus.request_name("com.yarpc.testservice")
        await bus.wait_for_disconnect()

    @signal()
    def Bumped(self) -> None:
        """
        a simple signal without arguments
        """
        return


    def on_Bump(self, handler) -> None:
        """
        Set handler for Bump method

        Args:
            handler (Callable[[], Awaitable[None]]): the method handler
        """
        self._Bump_handler = handler

    @method()
    async def Bump(self) -> None:
        """
        a simple method without args
        """
        if self._Bump_handler is None:
            raise NotImplementedError()

        return await self._Bump_handler()
