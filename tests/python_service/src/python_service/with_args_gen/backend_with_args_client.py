# Generated by YARPC
# Version:  0.1.0
# Definition:
#   File: /workspace/tests/definitions/02.1_with_args.yml
#   Object: WithArgs
#   Template: py/client.j2

from typing import List, Dict
from .connection import Connection
from dbus_next import Variant, DBusError
import sys
import asyncio


class BackendWithArgsClient():
    """
    A interface using only primitive types

    And some elaborate docstring

    """

    def __init__(self):
        self.name = "com.yarpc.backend.withArgs"
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._Notified_handler = None
        self._OrderReceived_handler = None
        self._close_event = asyncio.Event()

    async def connect(self):
        """
        Initializes the D-Bus connection and waits until it is closed
        """
        try:
            bus = await Connection.bus()
            introspection = await bus.introspect(
                "com.yarpc.backend",
                "/com/yarpc/backend/withArgs",
            )
            proxy_object = bus.get_proxy_object(
                "com.yarpc.backend",
                "/com/yarpc/backend/withArgs",
                introspection
            )
            self._interface = proxy_object.get_interface(
                self.name
            )

            if self._Notified_handler:
                self._interface.on_notified(self._Notified_wrapper)
            if self._OrderReceived_handler:
                self._interface.on_order_received(self._OrderReceived_wrapper)

            self._property_interface = proxy_object.get_interface(
                "org.freedesktop.DBus.Properties"
            )
            if self._properties_changed_handler:
                self._property_interface.on_properties_changed(self._properties_changed_wrapper)

            self._close_event.clear()
            await asyncio.wait(
                map(
                    lambda x: asyncio.create_task(x),
                    [self._close_event.wait(), bus.wait_for_disconnect()]
                ),
                return_when=asyncio.FIRST_COMPLETED
            )
        except Exception as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)

    def disconnect(self):
        """
        Closes the D-Bus connection of this client
        """
        self._close_event.set()
        if self._Notified_handler:
            self._interface.off_notified(self._Notified_wrapper)
        if self._OrderReceived_handler:
            self._interface.off_order_received(self._OrderReceived_wrapper)
        if self._properties_changed_handler:
                self._property_interface.off_properties_changed(self._properties_changed_wrapper)
        self._interface = None
        self._property_interface = None
        self._properties_changed_handler = None
        self._Notified_handler = None
        self._OrderReceived_handler = None

    def _unpack_prop(self, name, variant):
        prop_map = {
            "Speed": lambda value: value,
            "Distance": lambda value: value,
            "Duration": lambda value: value,
        }
        if name in prop_map:
            return prop_map[name](variant.value)
        return None

    def _unpack_properties(self, packed_properties):
        return {
            key: self._unpack_prop(key, packed_properties[key])
            for key in packed_properties.keys()
        }

    async def get_all_properties(self) -> dict:
        """Getter for all properties

        Returns:
            dict: a dictionary containing the current state of all properties
        """
        while not self._property_interface:
            await asyncio.sleep(0.1)
        properties = await self._property_interface.call_get_all(self.name)
        return self._unpack_properties(properties)

    def _properties_changed_wrapper(self, interface: str, properties: dict, _invalidated: list):
        if self._properties_changed_handler and interface == self.name:
            properties = self._unpack_properties(properties)
            self._properties_changed_handler(properties)

    def on_properties_changed(self, handler) -> None:
        """
        Set handler for property changes

        The handler takes a dictionary of the changed properties

        Args:
            handler(Callable[[dict], None]): the handler
        """
        self._properties_changed_handler = handler

    def _Notified_wrapper(
        self,
        message: 's',
    ):
        self._Notified_handler(
            message,
        )

    def on_Notified(self, handler):
        """
        Set handler for Notified signal

        Args:
            handler (Callable[[str], None]): the signal handler
        """
        self._Notified_handler = handler
        if self._interface:
            self._interface.on_notified(self._Notified_wrapper)

    def _OrderReceived_wrapper(
        self,
        item: 's',
        amount: 'u',
        pricePerItem: 'd',
    ):
        self._OrderReceived_handler(
            item,
            amount,
            pricePerItem,
        )

    def on_OrderReceived(self, handler):
        """
        Set handler for OrderReceived signal

        Args:
            handler (Callable[[str, int, float], None]): the signal handler
        """
        self._OrderReceived_handler = handler
        if self._interface:
            self._interface.on_order_received(self._OrderReceived_wrapper)

    async def Notify(
        self,
        message: 'str',
    ) -> None:
        """
        a simple method with one argument

        Args:
            message (str): The message
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_notify(
            message,
        )
        return None

    async def Order(
        self,
        item: 'str',
        amount: 'int',
        pricePerItem: 'float',
    ) -> float:
        """
        a simple method
        with args and return value


        Args:
            item (str): The
                item

            amount (int): a amount ordered
            pricePerItem (float): the price per item

        Returns:
            float: the
                total price

        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.call_order(
            item,
            amount,
            pricePerItem,
        )
        return raw_return

    async def get_Speed(self) -> float:
        """Getter for property 'Speed'

        the speed
        in m/s


        Returns:
            float: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_speed()
        unmarshalled = raw_return
        return unmarshalled


    async def set_Speed(self, value: float) -> None:
        """Setter for property 'Speed'

        the speed
        in m/s


        Args:
            value (float): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = value
        return await self._interface.set_speed(marshalled)

    async def get_Distance(self) -> int:
        """Getter for property 'Distance'

        the distance to travel in m

        Returns:
            int: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_distance()
        unmarshalled = raw_return
        return unmarshalled


    async def set_Distance(self, value: int) -> None:
        """Setter for property 'Distance'

        the distance to travel in m

        Args:
            value (int): the new value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        marshalled = value
        return await self._interface.set_distance(marshalled)

    async def get_Duration(self) -> float:
        """Getter for property 'Duration'

        the time until the distance is covered at the current speed

        Returns:
            float: the current value
        """
        while not self._interface:
            await asyncio.sleep(0.1)
        raw_return = await self._interface.get_duration()
        unmarshalled = raw_return
        return unmarshalled

