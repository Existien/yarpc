# Generated by YARPC
# Version:  0.1.0+editable
# Spec:
#   File: /workspace/tests/specs/basic_args.yml
#   Object: WithArgs
#   Template: client_mock

from .connection import Connection
from dbus_next import Variant, DBusError
from unittest.mock import Mock
import sys
import asyncio


class WithArgsClientMock():
    """
    Mock client implementation of the WithArgs D-Bus interface

    The Mock instance can be accessed via the `mock` attribute.
    All received signals will be forwarded to the mock using keyword arguments.
    E.g.
    A received signal `Fooed('bar')`
    might result in the following call of the mock:
    `client.mock.Fooed(msg='bar')`
    """

    def __init__(self):
        self._interface = None
        self.mock = Mock()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.testservice",
                "/com/yarpc/testservice",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.testservice",
                "/com/yarpc/testservice",
                introspection
            )
            self._interface = proxy_object.get_interface(
                "com.yarpc.testservice.withArgs"
            )

            self._interface.on_notified(self._Notified_handler)
            self._interface.on_order_received(self._OrderReceived_handler)
            await bus.wait_for_disconnect()
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)

    def _Notified_handler(
        self,
            message: str,
    ):
        self.mock.Notified(
            message,
        )

    def _OrderReceived_handler(
        self,
            item: str,
            amount: int,
            pricePerItem: float,
    ):
        self.mock.OrderReceived(
            item,
            amount,
            pricePerItem,
        )

    async def Notify(
        self,
        message: str,
    ) -> None:
        """
        a simple method with one argument

        Args:
            message (str): The message
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        return await self._interface.call_notify(
            message,
        )

    async def Order(
        self,
        item: str,
        amount: int,
        pricePerItem: float,
    ) -> float:
        """
        a simple method with args and return value

        Args:
            item (str): The item
            amount (int): a amount ordered
            pricePerItem (float): the price per item
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        return await self._interface.call_order(
            item,
            amount,
            pricePerItem,
        )
