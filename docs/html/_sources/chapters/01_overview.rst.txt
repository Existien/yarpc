Overview
========

Yarpc is a code generator for D-Bus services and clients.
The interfaces are defined using YAML files.

Features
--------

- Un-(marshalling) of structs
- Enum support
- Reusable definitions

Why not use the `XML introspection data format`_?
-------------------------------------------------

Many languages already come with tooling to generate D-Bus client or service code
from the XML introspection data.

The XML format does have some disadvantages

- it does not support enums, just uints with some documentation
- XML is not the most human-readable format, which can be important
  when the definitions serve as a single source of truth
- it does not support named structs. Depending on the tooling used,
  there may be annotations to define the corresponding types for a certain language,
  but this usually doesn't include unmarshalling or the generation of those types.
  This feature may also not be available in tooling for all languages.

Usage
-----

Assuming we have two python apps ``calc_service`` and ``calc_client``
for which we want to generate some interface code:

1. Create a folder with interface definitions

   .. code-block:: yaml
      :caption: foo/example.yaml

      objects:
      - name: Example
        kind: interface
        docs: Minimum example interface
        members:
        - name: CalculateAverage
          kind: method
          docs: calculates the average value of the provided numbers
          args:
          - name: numbers
            type: array<double>
            docs: the numbers to calculate the average for
          returns:
            type: double
            docs: the arithmetic average or 0, if the list is empty
        - name: Ping
          kind: signal
          docs: emitted every second
      outputs:
      - name: ExampleService
        language: py
        location: calc_service/src/calc_service/gen
        busName: com.example.calcservice
        services:
        - className: CalcService
          definition: Example
          objectPath: /com/example/calcservice
          interfaceName: com.example.calcservice.calculations
      - name: ExampleClient
        language: py
        location: calc_client/src/calc_client/gen
        clients:
        - className: CalcClient
          definition: Example
          busName: com.example.calcservice
          objectPath: /com/example/calcservice
          interfaceName: com.example.calcservice.calculations

   More examples can be found under `tests/definitions`_ of this repo

2. Run Yarpc via ``yarpc foo`` to generate the code
3. Use the generated code

   .. code-block:: python
      :caption: calc_service/src/calc_service/main.py

      import asyncio
      from calc_service.gen.connection import Connection
      from calc_service.gen.calc_service import CalcService


      async def main():
          service = CalcService()

          async def calculate_average(values: list) -> float:
              return sum(values)/len(values) if values else 0
          service.on_CalculateAverage(calculate_average)

          async def do_ping():
              while True:
                  await asyncio.sleep(1)
                  service.Ping()

          await asyncio.gather(
              Connection.run(service),
              do_ping()
          )


      if __name__ == "__main__":
          asyncio.run(main())

   .. code-block:: python
      :caption: calc_client/src/calc_client/main.py

      import asyncio
      import random
      from calc_client.gen.calc_client import CalcClient


      async def main():
          client = CalcClient()

          def on_ping():
              print("Ping")
          client.on_Ping(on_ping)

          async def do_stuff():
              for _ in range(3):
                  await asyncio.sleep(1)
                  random_numbers = [random.random()*100 for _ in range(5)]
                  result = await client.CalculateAverage(random_numbers)
                  print(f"Numbers: {random_numbers}\nAvg: {result}")

              client.disconnect()
              await asyncio.sleep(2)

          await asyncio.gather(
              client.connect(),
              do_stuff(),
          )


      if __name__ == "__main__":
          asyncio.run(main())


Yarpc can also be used to check the consistency of the generated code with the definitions
via ``yarpc foo --check``. This can be useful for CI jobs to ensure running yarpc after changing
definitions is not forgotten.

.. _XML introspection data format: https://dbus.freedesktop.org/doc/dbus-specification.html#introspection-format
.. _tests/definitions:  https://github.com/Existien/yarpc/tree/main/tests/definitions
