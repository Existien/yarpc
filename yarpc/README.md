# Yet another remote procedure call (yarpc)

yarpc generates D-Bus services and clients from interface definitions written in YAML.

## Dependencies for generated code

### Python
- dbus-next

## How to install

TBD

## How to use

1. Create a directory with interface definitions in yaml
2. Run `yarpc <definitions-dir>` to generate code

All yaml files in the `<definitions-dir>` and its subdirectories
will be merged and processed during generation,
so they can be split and organized as you see fit
(e.g. using separate files for reused elements).

The interface definition is divided into two top-level keys:
- **objects** containing the interface elements
- **outputs** containing the information about the code that should be generated.

See `tests/definitions` for examples
