- document qt6 restriction in docs!
  - reserved names (by us)
  - PropertiesChanged signal currently only sets properties one at a time
  - int64/uint64 lossy in QML, since its converted to Javascript!

- generate list of types to register/marshall and compare
  - centralize registering / marshalling / unmarshalling / != operator into one header to avoid duplication
