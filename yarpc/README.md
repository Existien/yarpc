# Yet another remote procedure call (yarpc)

yarpc generates D-Bus services and clients from specifications written in YAML.

## Dependencies for generated code

### Python
- dbus-next

## How to install

TBD

## How to use

TBD

## How to add support for a new language

1. Add language support to SDK

   If the new language needs additional libraries,
   compiler, etc, add them to the Dockerfile of the SDK.

2. Add language to yarpc

   TBD

3. Bootstrap test service

   Bootstrap a new service in your target language.

   This service will use the generated code to forward messages
   between a backend D-Bus interface and its own.
   This is used in the behave tests to test the generated
   client and service interfaces.

   It can also serve as an example for how to use the
   generated code for this language.

4. Add step to start test service for behave tests

   In the ``tests/behave-tests/steps/steps.py``,
   add a new step to start your test service.

   Use ``@given("a running python service")`` as a template.

5. Add language folders in ``tests/specs`` and ``tests/behave-tests``

   These will contain the specs used for the generated code and the
   tests for these specs respectively.

6. Implement features

   For each of the specs found in ``tests/specs/python``, do

   1. Copy the spec into your own ``tests/specs/`` language subfolder
      and adjust the ``language`` and ``location`` key

   2. Copy the tests for this spec from ``tests/behave-tests/python`` into your own ``tests/behave-tests`` language subfolder.

      Change the ``Given a running python service`` step in the feature files' ``Backend`` section to your own services' start step.

    3. Implement the templates needed for this spec

       TBD

    4. Update your service with the generated code

       TBD

    5. Run tests

       TBD

7. Update README

   TBD