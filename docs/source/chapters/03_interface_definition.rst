Interface definition
====================

The interfaces are defined in yaml files containing the top-level keys ``objects`` and ``outputs``,
each containing a list of objects and outputs, respectively.

These lists can be split over multiple files and subdirectories to structure them.

Objects
-------

Objects define

- interfaces containing a set of methods, signals and properties
- structs
- enums

.. toctree::
   :maxdepth: 2
   :glob:

   objects/*

.. _outputs:

Outputs
-------

Outputs define

- where code should be generated
- for which language
- for which objects it should generate client or service code
- which D-Bus address belongs to which object

The keys of output objects are language dependent:

.. toctree::
   :maxdepth: 2
   :glob:

   outputs/*