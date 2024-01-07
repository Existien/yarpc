from .utils import to_snake_case


class DBusClient:
    def __init__(self, interface):
        self._impl = __DBusClient(interface)
        self.mock = self._impl.mock
        self.interface = self._impl.interface