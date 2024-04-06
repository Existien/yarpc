.. _interfaces:

Interfaces
~~~~~~~~~~

Interfaces define a set of methods, signals and properties.
:ref:`outputs` then assign these interfaces to the D-Bus addresses they
should be generated for.

Keys
++++

name
   The name of the interface in PascalCase.
kind
   ``interface``
docs
   The documentation of the interface
members
   A list of methods, signals and properties

Methods
^^^^^^^

name
   The name of the method in PascalCase.
kind
   ``method``
docs
   The documentation of the method
args *(optional)*
   A list of arguments


   name
      The name of the argument in camelCase.
   type
      The type of the variable. One of

      - :ref:`builtin-types`
      - :ref:`enums`
      - :ref:`structs`
   docs
      The documentation of the argument

returns *(optional)*
   The return value


   type
      The type of the return value. One of

      - :ref:`builtin-types`
      - :ref:`enums`
      - :ref:`structs`
   docs
      The documentation of the return value

Signals
^^^^^^^

name
   The name of the signal in PascalCase.
kind
   ``signal``
docs
   The documentation of the signal
args *(optional)*
   A list of arguments


   name
      The name of the argument in camelCase.
   type
      The type of the variable. One of

      - :ref:`builtin-types`
      - :ref:`enums`
      - :ref:`structs`
   docs
      The documentation of the argument

Properties
^^^^^^^^^^

name
   The name of the property in PascalCase.
kind
   ``property``
type
   The type of the property. One of

   - :ref:`builtin-types`
   - :ref:`enums`
   - :ref:`structs`
docs
   The documentation of the property
readonly *(optional)*
   Whether the property is readonly (for clients connected via the D-Bus interface)

Example
^^^^^^^

.. code:: yaml

   objects:
   - name: Journey
     kind: interface
     docs: Interface to define routes and track the journey progression
     members:
     - name: ArrivedAtDestination
       docs: Emitted when the destination is reached
       kind: signal
       args:
       - name: distanceTravelled
         type: uint32
         docs: distance in m
     - name: SetRoute
       kind: method
       docs: configures the route to take
       members:
       - name: origin
         type: string
         docs: the start of the journey
       - name: destination
         type: string
         docs: the destination of the journey
       returns:
         type: bool
         docs: Whether the route is valid
     - name: Start
       kind: method
       docs: Starts the journey
     - name: Speed
       kind: property
       type: double
       docs: the speed in m/s
     - name: Distance
       kind: property
       type: uint32
       docs: the distance to travel in m
       readonly: true
     - name: Duration
       kind: property
       type: double
       readonly: true
       docs: the time until the distance is covered at the current speed