# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/basic_args.yml
#   Object: Minimal
#   Template: service

from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next import Variant, DBusError

import asyncio

class MinimalInterface(ServiceInterface):
    """
    A interface using signals and methods without args
    """

    def __init__(self):
        super().__init__("com.yarpc.testservice.minimal")
        self.object_path = "/com/yarpc/testservice"
        self._Bump_handler = None

    @signal()
    def Bumped(
        self,
    ) -> None:
        """
        a simple signal without arguments
        """


    def on_Bump(self, handler) -> None:
        """
        Set handler for Bump method

        Args:
            handler (Callable[[], Awaitable[None]]): the method handler
        """
        self._Bump_handler = handler

    @method()
    async def Bump(
        self,
    ) -> None:
        """
        a simple method without args
        """
        if self._Bump_handler is None:
            raise NotImplementedError()

        return await self._Bump_handler(
        )
