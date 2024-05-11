Python
~~~~~~

Dependencies
^^^^^^^^^^^^

- dbus-next

Keys
^^^^

language
   ``py``

location
    The directory where the code should be generated in.

    Relative paths will be resolved relative to the current working
    directory or the location provided by ``--output-base``.

busName
   The busName used for D-Bus services.
   Can be omitted when generating only client code.

   Bus names have the reverse form of URLs (e.g. ``com.yarpc.testing``)

services
   A list of D-Bus interfaces for which service code should be generated

   className
      The class name to be used for the generated interface class in PascalCase.

   definition
      The interface object to use

   objectPath
      The D-Bus object path the interface will be available under.

      Object paths follow the same scheme as Bus names, but with slashes instead of periods. (e.g. ``com/yarpc/testing``)

   interfaceName
      The name of the interface published under the objectPath.

      Interface names also have reverse form of URLs (e.g. ``com.yarpc.testing.myCoolInterface``)

clients
   A list of D-Bus interfaces for which client code should be generated

   className
      The class name to be used for the generated interface class in PascalCase.

   definition
      The interface object to use

   busName
      The busName used for the D-Bus service to connect to.

      Bus names have the reverse form of URLs (e.g. ``com.yarpc.testing``)

   objectPath
      The D-Bus object path the interface will be available under.

      Object paths follow the same scheme as Bus names, but with slashes instead of periods. (e.g. ``com/yarpc/testing``)

   interfaceName
      The name of the interface published under the objectPath.

      Interface names also have reverse form of URLs (e.g. ``com.yarpc.testing.myCoolInterface``)

service_mocks
   A list of D-Bus interfaces for which a mock service implementation should be generated.

   Keys are the same as for the ``services``.

   The service mocks will forward any method calls to a ``unittest.mock.AsyncMock`` object.

client_mocks
   A list of D-Bus interfaces for which a mock client implementation should be generated.

   Keys are the same as for the ``clients``.

   The client mocks will forward any incoming signals to a ``unittest.mock.Mock`` object.

How to use the generated service code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting the service:
  Await the ``Connection.run(args)`` coroutine where ``args`` are the service to run
  under the Bus name provided by the ``Connection`` class

  .. code-block:: py

     service = MyService()
     asyncio.run(Connection.run(service))

Emitting signals:
  To emit a signal, just call the method of the same name at the service

  .. code-block:: py

     service = MyService()

     async def pinger():
       while True:
         await asyncio.sleep(1)
         service.Ping()

     asyncio.run(asyncio.gather(
       Connection.run(service),
       pinger(),
     ))

Method callbacks:
   Use the ``on_<MethodName>(coroutine)`` methods to register a
   coroutine with the same signature as the D-Bus method in question.
   To raise D-Bus errors within the callback, raise a ``dbus_next.DBusError``.

   .. code-block:: py

      service = MyService()

      async def handle_repeat(self, text, amount):
        if amount < 1:
          from dbus_next import DBusError
          raise DBusError("com.myservice.InvalidArgument", "Only amounts > 0 are valid")
        return text*amount

      service.on_Repeat(handle_repeat)

Properties:
   To manage properties, pass an object compatible with an ``Provides<ServiceName>Properties`` protocol
   as ``property_provider`` argument

   .. code-block:: py

      class MyProperties:
        def __init__(self):
          self.my_prop = 1

        async def get_MyProp(self):
          return self.my_prop

        async def set_MyProp(self, value):
          self.my_prop = value
          return {"MyProp": self.my_prop}

      service = MyService(property_provider=MyProperties())

How to use the generated client code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting to the service:
  Await the ``connect`` coroutine of the client:

  .. code-block:: py

     client = MyClient()
     asyncio.run(client.connect())

Signal callbacks:
   Use the ``on_<SignalName>(callback)`` methods to register a
   callback with the same signature as the D-Bus signal in question.

   .. code-block:: py

      client = MyClient()
      received_pings = 0

      async def handle_ping():
        received_pings += 1
        print(f"received {received_pings} pings so far")

      client.on_Ping(handle_ping)

Calling methods:
   To call a D-Bus method, just await the coroutine of the same name at the client

  .. code-block:: py

     client = MyClient()

     async def repeater():
       amount = 1
       while True:
         await asyncio.sleep(1)
         print(await client.Repeat("Hi! ", amount))
         amount += 1

     asyncio.run(asyncio.gather(
       client.connect(),
       repeater(),
     ))

Properties:
   To get the current value of a property, use the ``get_<Property>()`` coroutine.

   To set a property, use the ``set_<Property>(value)`` coroutine.

   Use the ``get_all_properties()`` coroutine to get a dictionary with all properties.

   Use ``on_properties_changed(handler: Callable[[dict], None])`` to register a callback that
   handles properties changed signals

How to use the generated service mocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The service mocks behave the same as the generated services, but
come with preset property and method handlers.

Properties
  will be managed by a dictionary. The initial values can
  be set via constructor arguments

  .. code-block:: py

     service_mock = ServiceMock(
       MyProperty=1
     )

  Setter calls will also be forwarded to ``service.mock.on_<Property>_changed`` calls.

  To overwrite the default handler, use the ``service.on_<Property>_changed(handler)`` where
  ``handler`` takes the new value of the property and a dictionary with all current properties
  and returns a dictionary with the new property values.

Medhod calls
  will be forwarded to ``service.mock.<MethodName>`` where ``service.mock`` is an ``unittest.mock.AsyncMock``.
  Custom handlers can be registered by wrapping them in an ``AsyncMock``:

  .. code-block:: py

   service_mock = ServiceMock()

   async def handle_repeat(self, text, amount):
     if amount < 1:
       from dbus_next import DBusError
       raise DBusError("com.myservice.InvalidArgument", "Only amounts > 0 are valid")
     return text*amount

   service.mock.Repeat = AsyncMock(wraps=handle_repeat)

How to use the generated client mocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The client mocks behave the same as the generated clients, but
come with preset signal handlers that forward all incoming signals
to the ``unittest.mock.Mock`` object at ``client.mock``.