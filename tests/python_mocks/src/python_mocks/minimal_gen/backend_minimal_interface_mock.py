# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/01_minimal.yml
#   Object: Minimal
#   Template: py/service_mock.j2

from typing import Sequence
from dbus_next.service import (
    ServiceInterface, method, dbus_property, signal
)
from dbus_next.constants import PropertyAccess
from dbus_next import Variant, DBusError
from unittest.mock import AsyncMock
from copy import deepcopy


class _Interface(ServiceInterface):
    """
    D-Bus interface implementation for Minimal

    Args:
        wrapper(BackendMinimalInterfaceMock): Wrapper responsible for (un-)marhsalling D-Bus types
    """

    def __init__(self, wrapper):
        super().__init__("com.yarpc.backend.minimal")
        self.object_path = "/com/yarpc/backend"
        self._wrapper = wrapper

    @signal()
    def Bumped(
        self,
    ) -> None:
        return None

    @method()
    async def Bump(
        self,
    ) -> None:
        await self._wrapper.Bump(
        )
        return None


class BackendMinimalInterfaceMock():
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
        self.interface = _Interface(self)
        self.name = self.interface.name
        self.object_path = self.interface.object_path
        self.mock = AsyncMock()

        self.mock.Bump.return_value = None

        self._properties = {}

    async def _await_mock_method(self, method, local_variables):
        kwargs = dict(filter(lambda kv: kv[0] != 'self', local_variables.items()))
        return await getattr(self.mock, method)(**kwargs)

    def emit_properties_changed(self, changed_properties: dict) -> None:
        """Informs clients about changed properties

        Args:
            changed_properties (dict): A dictionary containing all changed properties with their new values
        """
        if not changed_properties: return

        def marshal(data):
            if isinstance(data, dict):
                for key in data.keys():
                    data[key] = marshal(data[key])
                return data
            elif isinstance(data, list):
                for i in range(0, len(data)):
                    data[i] = marshal(data[i])
                return data
            elif hasattr(data, 'to_dbus'):
                return data.to_dbus()
            else:
                return data
        marshalled = marshal(deepcopy(changed_properties))
        self.interface.emit_properties_changed(marshalled)

    def Bumped(
        self,
    ) -> None:
        """
        a simple signal without arguments
        """
        self.interface.Bumped(
        )

    async def Bump(
        self,
    ) -> None:
        """
        a simple method without args
        """
        return await self._await_mock_method("Bump", locals())
