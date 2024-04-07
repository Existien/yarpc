# Yet another remote procedure call (yarpc)

yarpc generates D-Bus services and clients from interface definitions written in YAML.

## SDK
- build SDK via the `sdk/build.sh` script
- start the SDK via the `sdk/run.sh` script

## Development
- install the package via `pdm install -p yarpc`
- run unit tests via `yarpc/run_tests.sh`
- generate interfaces via `tests/generate.sh`
- run behave tests via `tests/run_tests.sh`

## Manual testing
- use `d-feet` to call D-Bus methods
- use `bustle` to monitor D-Bus signals
- `python_service` can be started via `pdm run -p tests/python_service service`
- `python_client` can be started via `pdm run -p tests/python_client client`
- `python_mocks` dummy backend can be started via `pdm run -p tests/python_mocks mock`

## How to add support for a new language

1. Add language support to SDK

   If the new language needs additional libraries,
   compiler, etc, add them to the Dockerfile of the SDK.

2. Bootstrap test service

   Bootstrap a new service in your target language.

   This service will use the generated code to forward messages
   between a backend D-Bus interface and its own.
   This is used in the behave tests to test the generated
   client and service interfaces.

   It can also serve as an example for how to use the
   generated code for this language.

3. Add language to yarpc

   TBD

4. Add step to start test service for behave tests

   In the ``tests/behave-tests/steps/steps.py``,
   add a new step to start your test service.

   Use ``@given("a running python service")`` as a template.

5. Add language folders in ``tests/definitions`` and ``tests/behave-tests``

   These will contain the interface definitions used for the generated code and the
   tests for these definitions respectively.

6. Implement features

   For each of the definitions found in ``tests/definitions/python``, do

   1. Copy the definitions into your own ``tests/definitions/`` language subfolder
      and adjust the ``language`` and ``location`` key

   2. Copy the tests for these definitions from ``tests/behave-tests/python`` into your own ``tests/behave-tests`` language subfolder.

      Change the ``Given a running python service`` step in the feature files' ``Backend`` section to your own services' start step.

    3. Implement the templates needed for this definitions

       TBD

    4. Update your service with the generated code

       TBD

    5. Run tests

       TBD

7. Update README

   TBD
