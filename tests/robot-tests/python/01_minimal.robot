*** Settings ***
Library  test_library.library
Test Setup  Start Services
Test Teardown  Teardown context

*** Test Cases ***
Interface using signals and methods without args
# Method call without arguments or return value
    Call D-Bus Method                   Alice  Bump
    Should receive D-Bus method call    Bob    Bump
# Emit a signal without arguments
    Emit D-Bus signal                   Bob    Bumped
    Should receive D-Bus signal         Alice  Bumped

*** Keywords ***
Start Services
    Setup context
    Start backend mock with the following interfaces  ${BACKEND_INTERFACES}
    Start service                                     python_service/run.sh
    Connect to the following interfaces               ${MOCK_CLIENTS}

*** Variables ***
&{BACKEND_INTERFACES}   Minimal=Bob
...                     WithArgs=
...                     Primitives=
...                     Structs=
...                     Arrays=
...                     ArraysWithStructs=
...                     Dictionaries=
...                     DictsWithStructs=
...                     DictsWithArrays=
...                     DictKeys=
...                     Enums=
...                     EnumsWithArrays=
...                     EnumsWithDicts=
...                     EnumsWithStructs=
&{MOCK_CLIENTS}         Minimal=Alice