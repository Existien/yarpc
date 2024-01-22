# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/basic_args.yml
#   Object: Minimal
#   Template: service_mock

from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
from copy import deepcopy
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

    def __init__(
        self,
    ):
        super().__init__("com.yarpc.backend.minimal")
        self.mock = AsyncMock()
        self.object_path = "/com/yarpc/backend"

        self.mock.Bump.return_value = None

        self._properties = {}

    async def _await_mock_method(self, method, local_variables):
        kwargs = dict(filter(lambda kv: kv[0] != 'self', local_variables.items()))
        return await getattr(self.mock, method)(**kwargs)

    @signal()
    def Bumped(
        self,
    ) -> None:
        """
        a simple signal without arguments
        """

    @method()
    async def Bump(
        self,
    ) -> None:
        """
        a simple method without args
        """
        return await self._await_mock_method("Bump", locals())