- document qt6 restriction in docs!
  - reserved names (by us)
  - PropertiesChanged signal currently only sets properties one at a time
  - int64/uint64 lossy in QML, since its converted to Javascript!

- fix JS Object -> QVariantMap conversion or provide tools to generate method/signal types in QML (try to create dict reply)
  - check if arrays are also affected
