Qt6
~~~

Dependencies
^^^^^^^^^^^^

- CMake 3.19 or newer
- Qt6.5 (or newer) with QDBus module

Keys
^^^^

language
   ``qt6``

location
    The directory where the code should be generated in.

    Relative paths will be resolved relative to the current working
    directory or the location provided by ``--output-base``.

qmlUri
   The QML URI the generated code will be found under.
   Also determines the namespace.
   The URI ``gen.minimal`` will result in the namespace ``gen::minimal``.

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

How to use the generated service code in QML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting the service:
  Run the ``connect()`` method of the service singleton

  .. code-block:: qml

     Item {
         Component.onCompleted: MyService.connect()
     }

Emitting signals:
  To emit a signal, call the ``Emit<SignalName>`` method, replacing ``<SignalName>`` with the name of the signal

  .. code-block:: qml

     Timer {
         repeat: true
         interval: 1000
         running: true
         onTriggered: MyService.EmitPing()
     }

Method callbacks:
  Connect the ``<MethodName>Called`` signals (with ``<MethodName>`` replaced by the method name)
  to a slot that should handle the callback. The signal passes a reply object that contains
  the method call arguments and functions to send a reply or a D-Bus error

  .. code-block:: qml

     Connections {
         target: MyService
         function onRepeatCalled(reply) {
             if (reply.args().amount < 1) {
                 reply.sendError("com.myservice.InvalidArgument", "Only amounts > 0 are valid")
             } else {
                 var repeated = reply.args().text * reply.args().amount
                 reply.sendReply(repeated)
             }
         }
     }

Properties:
  D-Bus properties are exposed as QML properties of the service singleton.
  Setting them in QML will automatically emit propertiesChanged signals over D-Bus.
  To handle clients setting properties via D-Bus, connect the ``property<PropertyName>Set`` signal
  and set the respective properties in the slot.

  .. code-block:: qml

     Connections {
         target: MyService
         function onPropertyMyPropSet(value) {
             MyService.myProp = value
         }
     }

How to use the generated client code in QML
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting to the service:
  Instantiate the client class. It will automatically (re)-connect to the service interface
  when it is available. The ``connected`` property can be used to react to connection changes.

  .. code-block:: qml

     MyClient {
         id: client
         onConnectedChanged: {
             if (connected) {
                 console.log("Connection established")
             } else {
                 console.log("Connection lost")
             }
         }
     }

Signal callbacks:
  Connect the ``<SignalName>Received`` signal (with ``<SignalName>`` being the signal name)
  to a slot to handle the incoming signal

  .. code-block:: qml

     MyClient {
         id: client
         property int receivedPings: 0
         onPingReceived: {
             receivedPings += 1
             console.log(qsTr("received %1 pings so far").arg(receivedPings))
         }
     }

Calling methods:
  To call a D-Bus method, just call the respective method of the client.
  The method will return a PendingCall object containing a ``finished``
  and an ``error`` signal that will be emitted when the method returns or
  raises an error.

  .. code-block:: qml

     MyClient {
         id: client
     }

     function sendRepeat(text, amount) {
         var call = client.Repeat(text, amount)
         call.finished.connect(function(response) {
             console.log(qsTr("Call finished with %1").arg(response))
         })
         call.error.connect(function(dbusError) {
             console.log(qsTr("Call failed with %1: %2").arg(dbusError.name).arg(dbusError.message))
         })
     }

Properties:
  The D-Bus properties are exposed as QML properties of the client class.
  To get a ``QVariantMap`` containing all properties, use the ``getAllProperties()`` method of the client.


How to use the generated service code in C++
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting the service:
  Run the ``connect()`` method of the service

  .. code-block:: cpp

     auto service = MyService();
     service.connect();

Emitting signals:
  To emit a signal, call the ``Emit<SignalName>`` method, replacing ``<SignalName>`` with the name of the signal

  .. code-block:: cpp

     auto service = MyService();
     service.connect();
     service.EmitPing();

Method callbacks:
  Connect the ``<MethodName>Called`` signals (with ``<MethodName>`` replaced by the method name)
  to a slot that should handle the callback. The signal passes a reply object that contains
  the method call arguments and functions to send a reply or a D-Bus error

  .. code-block:: cpp

     void onRepeatCalled(MyServiceUtils::RepeatPendingReply* reply) {
         if (reply->args().amount < 1) {
             reply->sendError("com.myservice.InvalidArgument", "Only amounts > 0 are valid");
         } else {
             QString repeated = reply->args().text.repeated(reply->args().amount);
             reply->sendReply(repeated)
         }
     }

     auto service = MyService();
     QtObject::connect(&service, &MyService::repeatCalled, onRepeatCalled);
     service.connect();

Properties:
  D-Bus properties are exposed via getter (``get<PropertyName>()``) and setter (``set<PropertyName>``) methods, as well as ``<propertyName>Changed`` signals.
  Calling the setter will automatically emit propertiesChanged signals over D-Bus.
  To handle clients setting properties via D-Bus, connect the ``property<PropertyName>Set`` signal
  and set the respective properties in the slot.

  .. code-block:: cpp

     auto service = MyService();
     QtObject::connect(
         &service, &MyService::propertyMyPropSet,
         [&](double value) {
             service.setMyProp(value);
         }
     );
     service.connect();

How to use the generated client code in C++
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connecting to the service:
  Instantiate the client class. It will automatically (re)-connect to the service interface
  when it is available. The ``connected`` property can be used to react to connection changes.

  .. code-block:: cpp

     auto client = MyClient();
     QtObject::connect(
        &client, &MyClient::connectedChanged,
        [&]() {
            if (client.getConnected()) {
                qDebug() << "Connection established";
            } else {
                qDebug() << "Connection lost";
            }
        }
     );

Signal callbacks:
  Connect the ``<SignalName>Received`` signal (with ``<SignalName>`` being the signal name)
  to a slot to handle the incoming signal

  .. code-block:: cpp

     auto client = MyClient();
     int receivedPings = 0;
     QtObject::connect(
         &client, &MyClient::pingReceived,
         [&](){qDebug() << "received " << ++receivedPings << " pings so far";}
     );

Calling methods:
  To call a D-Bus method, just call the respective method of the client.
  The method will return a PendingCall object containing a ``finished``
  and an ``error`` signal that will be emitted when the method returns or
  raises an error.

  .. code-block:: cpp

     auto client = MyClient();

     auto pendingCall = client.Repeat("Foo", 3);
     QtObject::connect(
        &pendingCall, &MyClientUtils::RepeatPendingCall::finished,
        [](QString response){qDebug() << "Call finished with " << response;}
     );
     QtObject::connect(
        &pendingCall, &MyClientUtils::RepeatPendingCall::error,
        [](DBusError error){qDebug() << "Call failed with " << error.name << " with " << error.message;}
     );

Properties:
  The D-Bus properties are exposed via getter (``get<PropertyName>()``), setter (``set<PropertyName>``) and changed signals (``<propertyName>Changed``) of the client class.
  To get a ``QVariantMap`` containing all properties, use the ``getAllProperties()`` method of the client.

Restrictions
^^^^^^^^^^^^

- The generator creates some auxiliary properties, signals methods and structs for plumbing.
  Most notably the ``connected`` property for interfaces.
  This can lead to naming conflicts, but shouldn't ordinarily happen.
- The PropertiesChanged D-Bus signal is emitted for one property-change
  at a time, event when multiple properties change together
- Handling ``int64`` and ``uint64`` types in QML will lead to issues, since
  they are outside the range of Javascript numbers.