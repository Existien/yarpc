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
- `python_service` can be started via `tests/python_service service/run.sh`
- `python_mocks` dummy backend can be started via `tests/python_mocks/run.sh`