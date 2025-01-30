Feature: Enums interface

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
            | Enums             | Bob  |
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
        And a running service started with 'rust_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | Enums     | Alice |

    Scenario: Interface using enums

    # Scenario: Emit a signal with a single parameter
        When a 'EnumSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value      |
            | color | Color.BLUE |
        Then 'Alice' receives a 'EnumSignal' signal with the following parameters
            | name  | value      |
            | color | Color.BLUE |

    # Scenario: Method call with multiple arguments and a return value
        Given 'Bob' replies to a 'EnumMethod' method call with the following return value
            | value     |
            | Color.RED |
        When the 'EnumMethod' method is called by 'Alice' with the following parameters
            | name  | value     |
            | color | Color.RED |
        Then 'Alice' receives a return value of
            | value     |
            | Color.RED |
        And 'Bob' receives a 'EnumMethod' method call with the following parameters
            | name  | value     |
            | color | Color.RED |

    # Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                        |
            | {"EnumProperty":Color.GREEN} |

    # Scenario: Geting and setting read-write properties
        When the 'EnumProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value       |
            | Color.GREEN |
        When the 'EnumProperty' property is set by 'Alice' to a value of
            | value     |
            | Color.RED |
        Then 'Alice' receives a property change signal with the following parameters
            | name         | value     |
            | EnumProperty | Color.RED |
        When the 'EnumProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value     |
            | Color.RED |

