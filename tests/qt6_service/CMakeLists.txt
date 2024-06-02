cmake_minimum_required(VERSION 3.25)
project(qt6_service LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
find_package(Qt6 REQUIRED COMPONENTS
    Quick
    DBus
)
qt_standard_project_setup()
qt_policy(SET QTP0001 NEW)

qt_add_executable(service
    main.cpp
)

qt_add_qml_module(service
    URI Application
    VERSION 1.0
    QML_FILES
        main.qml
)

target_link_libraries(service PRIVATE
    Qt6::Quick
    Qt6::DBus
    Interfaces
)

add_subdirectory(gen/minimal)
add_subdirectory(gen/with_args)
add_subdirectory(gen/structs)
add_subdirectory(interfaces)