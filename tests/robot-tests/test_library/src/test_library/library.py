import subprocess
from robot.api.deco import library, keyword
from robot.api import logger
import asyncio
from dbus_next.errors import DBusError
from python_mocks import Connection
from test_library.fixtures.clients import get_mock_client
from test_library.fixtures.interfaces import get_service_mock
from test_library.helpers.process import shutdown_process
from test_library.helpers.dbus import wait_for_call, wait_for_signal, wait_for_dbus
from test_library.context import Context


@library
class DBusLibrary:
    def __init__(self):
        self.context = None

    def get_mock(self, name):
        assert name in self.context.mocks.keys(), f"Mock {name} not found"
        return self.context.mocks[name]

    def run(self, coro):
        return self.context.loop.run_until_complete(coro)

    @keyword
    def setup_context(self):
        self.context = Context()

    @keyword
    def teardown_context(self):
        first_error = None

        # Run cleanup actions
        self.context.cleanup_actions.reverse()
        for cleanup_action in self.context.cleanup_actions:
            try:
                cleanup_action()
            except Exception as e:
                logger.error(f"Error during cleanup: {type(e).__name__}: {e}")
                if first_error is None:
                    first_error = e

        # Cancel remaining tasks
        for task in self.context.tasks:
            if not task.done():
                task.cancel()
                try:
                    self.run(task)
                except asyncio.CancelledError:
                    pass

        # Re-raise first error
        if first_error:
            raise first_error

    @keyword
    def start_backend_mock_with_the_following_interfaces(self, args):
        async def start_interface(interface, name):
            service = get_service_mock(interface)
            service_task = asyncio.create_task(Connection.run(service))
            if name:
                self.context.mocks[name] = service
            self.context.tasks.append(service_task)
            self.context.cleanup_actions.append(Connection.close)
            await wait_for_dbus(
                bus_name="com.yarpc.backend",
                object_path=service.object_path,
                interface_name=service.name,
            )
        for interface, name in args.items():
            self.run(start_interface(interface, name))

    @keyword
    def start_service(self, args):
        start_args = args.split(' ')
        process = subprocess.Popen(
            args=start_args,
            cwd="/workspace/tests",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.context.cleanup_actions.append(lambda: shutdown_process(process))
        self.run(wait_for_dbus(
            bus_name="com.yarpc.testservice",
            object_path="/com/yarpc/testservice/minimal",
            interface_name="com.yarpc.testservice.minimal"
        ))

    @keyword
    def connect_to_the_following_interfaces(self, args):
        async def connect_to_interface(interface, name):
            client = get_mock_client(interface)
            client_task = asyncio.create_task(client.connect())
            self.context.mocks[name] = client
            self.context.cleanup_actions.append(client.disconnect)
            self.context.tasks.append(client_task)
            await asyncio.sleep(0.1)
        for interface, name in args.items():
            self.run(connect_to_interface(interface, name))

    @keyword('Call D-Bus method')
    def call_method(self, client_name, method, kwargs={}):
        client = self.get_mock(client_name)
        return_value = None
        error = None
        try:
            return_value = self.run(getattr(client, method)(**kwargs))
        except DBusError as e:
            error = {'type': e.type, 'text': e.text}
        return (return_value, error)

    @keyword('Should receive D-Bus method call')
    def should_receive_call(self, interface_name, method, kwargs={}):
        interface = self.get_mock(interface_name)
        mock = getattr(interface.mock, method)
        self.run(wait_for_call(mock))
        mock.assert_awaited_once_with(**kwargs)
        mock.reset_mock()

    @keyword('Emit D-Bus signal')
    def emit_signal(self, interface_name, signal, kwargs={}):
        interface = self.get_mock(interface_name)
        getattr(interface, signal)(**kwargs)

    @keyword('Should receive D-Bus signal')
    def should_receive_signal(self, client_name, signal, kwargs={}):
        client = self.get_mock(client_name)
        mock = getattr(client.mock, signal)
        self.run(wait_for_signal(mock))
        mock.assert_called_once_with(**kwargs)
        mock.reset_mock()

    @keyword('Set D-Bus method return value')
    def set_return_value(self, interface_name, method, return_value):
        interface = self.get_mock(interface_name)
        mock = getattr(interface.mock, method)
        mock.return_value = return_value

    @keyword('Set D-Bus method error')
    def set_error(self, interface_name, method, error):
        interface = self.get_mock(interface_name)
        mock = getattr(interface.mock, method)
        mock.side_effect = DBusError(error['type'], error['text'])

    @keyword('Get properties')
    def get_properties(self, client_name):
        client = self.get_mock(client_name)
        return self.run(client.get_all_properties())

    @keyword('Get property')
    def get_property(self, client_name, property):
        client = self.get_mock(client_name)
        return self.run(getattr(client, f"get_{property}")())

    @keyword('Set property')
    def set_property(self, client_name, property, value):
        client = self.get_mock(client_name)
        self.run(getattr(client, f"set_{property}")(value))

    @keyword('Should receive property change')
    def should_receive_property_change(self, client_name, content):
        client = self.get_mock(client_name)
        mock = client.mock.on_properties_changed
        self.run(wait_for_signal(mock))
        logger.warn(mock.call_args_list)
        mock.assert_called_with(properties=content)
        mock.reset_mock()