*** Settings ***
Library  test_library.library
Test Setup  Start Services
Test Teardown  Teardown context

*** Test Cases ***
# Interface using only primitive types
Method call with a single argument, without a return value
    Call D-Bus Method                   Alice   Notify          {'message': 'Foo'}
    Should receive D-Bus method call    Bob     Notify          {'message': 'Foo'}
Emit a signal with a single parameter
    Emit D-Bus signal                   Bob     Notified        {'message': 'Foo'}
    Should receive D-Bus signal         Alice   Notified        {'message': 'Foo'}
Method call with multiple arguments and a return value
    Set D-Bus method return value       Bob     Order           ${ORDER_RET_VAL}
    ${r}  ${e}  Call D-Bus method       Alice   Order           ${ORDER}
    Should receive D-Bus method call    Bob     Order           ${ORDER}
    Should be equal                     ${r}    ${ORDER_RET_VAL}
Method call that raises an error
    Set D-Bus method error              Bob     Order           ${ORDER_ERROR}
    ${r}  ${e}  Call D-Bus method       Alice   Order           ${ORDER}
    Should be equal                     ${e}    ${ORDER_ERROR}
Emit a signal with multiple parameters
    Emit D-Bus signal                   Bob     OrderReceived   ${ORDER}
    Should receive D-Bus signal         Alice   OrderReceived   ${ORDER}
Get all properties
    ${r}  Get properties                Alice
    Should be equal                     ${r}    ${PROPERTIES}
Getting read-only properties
    ${r}    Get property                Alice   Duration
    Should be equal                     ${r}    ${DURATION}
Geting and setting read-write properties
    ${r}    Get property                Alice   Distance
    Should be equal                     ${r}    ${DISTANCE}
    Set property                        Alice   Distance    ${DISTANCE_NEW}
    Should receive property change      Alice   ${DISTANCE_CHANGE}
    ${r}    Get property                Alice   Distance
    Should be equal                     ${r}    ${DISTANCE_NEW}
    ${r}    Get property                Alice   Speed
    Should be equal                     ${r}    ${SPEED}
    Set property                        Alice   Speed    ${SPEED_NEW}
    Should receive property change      Alice   ${SPEED_CHANGE}
    ${r}    Get property                Alice   Speed
    Should be equal                     ${r}    ${SPEED_NEW}

*** Keywords ***
Start Services
    Setup context
    Start backend mock with the following interfaces  ${BACKEND_INTERFACES}
    Start service                                     python_service/run.sh
    Connect to the following interfaces               ${MOCK_CLIENTS}

*** Variables ***
${ORDER: dict}              {'item': 'Marbles', 'amount': 33, 'pricePerItem': 0.33}
${ORDER_RET_VAL: float}     6.022
${ORDER_ERROR: dict}        {'type': 'com.yarpc.backend.withArgs.error', 'text': 'out of marbles'}
${DISTANCE: int}            200
${DURATION: float}          20.0
${SPEED: float}             10.0
${PROPERTIES: dict}         {'Distance': ${DISTANCE}, 'Duration': ${DURATION}, 'Speed': ${SPEED}}
${DISTANCE_NEW: int}        200
${DURATION_NEW: float}      20.0
${SPEED_NEW: float}         10.0
${DISTANCE_CHANGE: dict}    {'Distance': ${DISTANCE_NEW}}
${SPEED_CHANGE: dict}       {'Speed': ${SPEED_NEW}}
&{BACKEND_INTERFACES}   Minimal=
...                     WithArgs=Bob
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
&{MOCK_CLIENTS}         WithArgs=Alice