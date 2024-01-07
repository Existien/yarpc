# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/primitives.yml
#   Object: Minimal
#   Template: service_mock

from dbus_next.aio import MessageBus
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
import asyncio

class BackendMinimalInterfaceMock(ServiceInterface):
    """
    Mock service implementation of the Minimal D-Bus interface.

    The AsyncMock instance can be accessed via the `mock` attribute.
    All method calls will be forwarded to the mock using keyword arguments.
    E.g.
    `await service.Foo('bar')`
    might result in the following await of the mock:
    `await service.mock.Foo(msg='bar')`
    """

    def __init__(self):
        super().__init__("com.yarpc.backend.minimal")
        self._bus = None
        self.mock = AsyncMock()

        self.mock.Bump.return_value = None

    async def run(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        self._bus = await MessageBus().connect()
        self._bus.export("/com/yarpc/backend", self)
        await self._bus.request_name("com.yarpc.backend")
        await self._bus.wait_for_disconnect()

    def stop(self):
        """
        Closes the D-Bus connection
        """
        if self._bus:
            self._bus.disconnect()

    async def _await_mock_method(self, method, local_variables):
        kwargs = dict(filter(lambda kv: kv[0] != 'self', local_variables.items()))
        return await getattr(self.mock, method)(**kwargs)

    @signal()
    def Bumped(self) -> None:
        """
        a simple signal without arguments
        """
        return

    @method()
    async def Bump(self) -> None:
        """
        a simple method without args
        """
        return await self._await_mock_method("Bump", locals())
