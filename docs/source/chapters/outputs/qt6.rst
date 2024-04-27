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
