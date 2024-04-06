.. _enums:

Enums
~~~~~

Since enumerations are not specified by D-Bus,
they are internally converted to ``int32``.

Keys
^^^^

name
   The name of the enum in PascalCase.
kind
   ``enum``
docs
   The documentation
members
   A list of key - value pairs for the enum values

Example
^^^^^^^

.. code:: yaml

   objects:
   - name: Color
     kind: enum
     docs: Some colors
     members:
     - RED: 0
     - GREEN: 2
     - BLUE: 4
