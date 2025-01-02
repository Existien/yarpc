qt_add_qml_module(Interfaces
    STATIC
    PLUGIN_TARGET Interfaces
    URI "interfaces"
    VERSION 1.0
    QML_FILES
        Minimal.qml
        WithArgs.qml
        Primitives.qml
        Structs.qml
        Arrays.qml
        ArraysWithStructs.qml
        Dictionaries.qml
        DictsWithStructs.qml
        DictsWithArrays.qml
        DictKeys.qml
)

target_link_libraries(Interfaces PUBLIC
  Minimal
  WithArgs
  Structs
  Arrays
  Dicts
)