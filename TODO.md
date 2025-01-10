- document qt6 restriction in docs!
  - reserved names (by us)
  - PropertiesChanged signal currently only sets properties one at a time
  - int64/uint64 lossy in QML, since its converted to Javascript!
  - don't forget to test enums in instantiation tests!

- split build script off of run script and do build step before tests
