Feature: EnumsWithArrays interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           |      |
            | WithArgs          |      |
            | Primitives        |      |
            | Structs           |      |
            | Arrays            |      |
            | ArraysWithStructs |      |
            | Dictionaries      |      |
            | DictsWithStructs  |      |
            | DictsWithArrays   |      |
            | DictKeys          |      |
            | Enums             |      |
            | EnumsWithArrays   | Bob  |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
            | QmlInstantiation  |      |
        And a running service started with 'qt6_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface       | name  |
            | EnumsWithArrays | Alice |

    Scenario: Interface using enums in arrays

    # Scenario: Emit a signal with a single parameter
        When a 'EnumSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value                      |
            | color | [Color.BLUE, Color.ORANGE] |
        Then 'Alice' receives a 'EnumSignal' signal with the following parameters
            | name  | value                      |
            | color | [Color.BLUE, Color.ORANGE] |

    # Scenario: Method call with multiple arguments and a return value
        Given 'Bob' replies to a 'EnumMethod' method call with the following return value
            | value                    |
            | [Color.RED, Color.GREEN] |
        When the 'EnumMethod' method is called by 'Alice' with the following parameters
            | name  | value                      |
            | color | [Color.BLUE, Color.ORANGE] |
        Then 'Alice' receives a return value of
            | value                    |
            | [Color.RED, Color.GREEN] |
        And 'Bob' receives a 'EnumMethod' method call with the following parameters
            | name  | value                      |
            | color | [Color.BLUE, Color.ORANGE] |

    # Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                 |
            | {"EnumProperty":[Color.RED, Color.GREEN, Color.BLUE]} |

    # Scenario: Geting and setting read-write properties
        When the 'EnumProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                |
            | [Color.RED, Color.GREEN, Color.BLUE] |
        When the 'EnumProperty' property is set by 'Alice' to a value of
            | value                      |
            | [Color.BLUE, Color.ORANGE] |
        Then 'Alice' receives a property change signal with the following parameters
            | name         | value                      |
            | EnumProperty | [Color.BLUE, Color.ORANGE] |
        When the 'EnumProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                      |
            | [Color.BLUE, Color.ORANGE] |

