# Yet another remote procedure call (yarpc)

yarpc generates D-Bus services and clients from specifications written in YAML.

## SDK
- build SDK via the `sdk/build.sh` script
- start the SDK via the `sdk/run.sh` script

## Development
- install the package via `pdm install -p yarpc`
- run unit tests via `yarpc/run_tests.sh`
- generate interfaces via `tests/generate.sh`

## Manual testing
- use `d-feet` to call D-Bus methods
- use `bustle` to monitor D-Bus signals
