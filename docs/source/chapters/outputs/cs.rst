C#
~~~

Dependencies
^^^^^^^^^^^^

- Tmds.DBus

Keys
^^^^

language
   ``cs``

location
    The directory where the code should be generated in.

    Relative paths will be resolved relative to the current working
    directory or the location provided by ``--output-base``.

namespace
   The namespace the generated code will be found under.

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

How to use the generated service code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting the service:

  - Create a ``Connection`` instance and onnect to the D-Bus using the ``Connection.ConnectAsync`` method if not already done
  - Create the object path instance that contains the service interface
  - Set method callbacks for the interfaces in the object path (see *Method callbacks* section)
  - Register the object path with the connection using the ``Connection.RegisterObjectPathAsync`` method

  .. code-block:: cs
  
     var connection = new Connection();
     var connectionTask = connection.ConnectAsync(stoppingToken);
     var objectPath = new MyObjectPath();
     // Set method callbacks here
     await connection.RegisterObjectPathAsync(objectPath);

Emitting signals:
  To emit a signal, just call the ``Emit<SignalName>`` method of the interface.
  The interfaces are members of the object path.

  .. code-block:: cs

     objectPath.PingerInterface.EmitPing();

Method callbacks:
  Set the respective ``On<MethodName>`` member of the interface.
  The interfaces are members of the object path.

  .. code-block:: cs

     objectPath.PingerInterface.OnEcho = async (string message) => {
         await Task.Delay(1000, stoppingToken);
         return message;
     };

Properties:
  D-Bus properties are internally exposed via the ``Properties`` member of the interface.
  The default property setters can be overwritten by setting the ``Set<PropertyName>`` member of the interface.
  When changing properties, don't change the members, but swap the whole ``Properties`` member.
  It's setter will automatically determine property changes and emit the respective ``PropertiesChanged`` signal.

  .. code-block:: cs

     objectPath.RunnerInterface.SetDistance = (double newValue, RunnerInterfaceProperties oldProps) => {
         oldProps.Distance = newValue;
         oldProps.Duration = oldProps.Speed / newValue;
         return Task.FromResult(oldProps);
     };


How to use the generated client code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting to the service:

  - Create a ``Connection`` instance and onnect to the D-Bus using the ``Connection.ConnectAsync`` method if not already done
  - Create the client instance
  - Register the client with the connection using the ``Connection.RegisterClient`` method

  .. code-block:: cs
  
     var connection = new Connection();
     var connectionTask = connection.ConnectAsync(stoppingToken);
     var myClient = new MyClient();
     await connection.RegisterClient(myClient);

Signal callbacks:

  Signals are forwarded to an event of the same name.
  The signal payload is wrapped in a struct due to technical limitations (and to preserve names).

  .. code-block:: cs

     client.MySignal += (DemoCode.Generated.MyClientPayloads.MySignal payload) => {
         // Do something smart with it
     };

Calling methods:

  Methods can be called using the ``<MethodName>Async()`` members of the client.
  
  .. code-block:: cs

     await client.PingAsync();

Properties:
  To get the current value of a property, use the ``Get<PropertyName>Async()`` method.

  To set a property, use the ``Set<PropertyName>Async()`` method.

  Use the ``OnPropertiesChanged`` event to register handlers for property changes.
  The property changes are communicated as a ``KeyValuePair<string, object>[]`` that contains
  all changed properties.

Restrictions
^^^^^^^^^^^^

- The generated service code can only (dis-)connect whole object paths.
  I.e. it is not possible to (dis-)connect just one interface at an object path
- Dictionaries are handled as KeyValuePair arrays