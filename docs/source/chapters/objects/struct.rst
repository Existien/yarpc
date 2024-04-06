.. _structs:

Structs
~~~~~~~

Keys
^^^^

name
   The name of the struct in PascalCase.
kind
   ``struct``
docs
   The documentation of the struct
members
   A list of member variables


   name
      The name of the member variable in camelCase.
   type
      The type of the variable. One of

      - :ref:`builtin-types`
      - :ref:`enums`
      - :ref:`structs`
   docs
      The documentation of the member variable

Example
^^^^^^^

.. code:: yaml

   objects:
   - name: Item
     kind: struct
     docs: An item
     members:
     - name: name
       type: string
       docs: the name of the item
     - name: color
       type: Color
       docs: the color of the item
   - name: Box
     kind: struct
     docs: A container with items
     members:
     - name: content
       type: array<Item>
       docs: the items in the container