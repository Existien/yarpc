Feature: DictsWithArrays interface

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
            | DictsWithArrays   | Bob  |
            | DictKeys          |      |
            | Enums             |      |
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
        And a running service started with 'python_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface       | name  |
            | DictsWithArrays | Alice |

    Scenario: Interface using dicts using arrays using dicts

    # Scenario: Method call
        Given 'Bob' replies to a 'DictsArrayMethod' method call with the following return value
            | value                          |
            | {"x": [{"ab":12}, {"bc": 23}]} |
        When the 'DictsArrayMethod' method is called by 'Alice' with the following parameters
            | name    | value                          |
            | numbers | {"x": [{"ab":12}, {"bc": 23}]} |
        Then 'Alice' receives a return value of
            | value                          |
            | {"x": [{"ab":12}, {"bc": 23}]} |
        Then 'Bob' receives a 'DictsArrayMethod' method call with the following parameters
            | name    | value                          |
            | numbers | {"x": [{"ab":12}, {"bc": 23}]} |

    # Scenario: Signal
        When a 'DictsArraySignal' signal is emitted by 'Bob' with the following parameters
            | name    | value                          |
            | numbers | {"x": [{"ab":12}, {"bc": 23}]} |
        Then 'Alice' receives a 'DictsArraySignal' signal with the following parameters
            | name    | value                          |
            | numbers | {"x": [{"ab":12}, {"bc": 23}]} |

    # Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                                                                |
            | {"DictArrayProperty":{"A":[{"AA1":11,"AA2":12},{"AB1":21,"AB2":22}],"B":[{"BA1":11,"BA2":12},{"BB1":21,"BB2":22}],}} |

    # Scenario: Geting and setting read-write properties
        When the 'DictArrayProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                                          |
            | {"A":[{"AA1":11,"AA2":12},{"AB1":21,"AB2":22}],"B":[{"BA1":11,"BA2":12},{"BB1":21,"BB2":22}],} |
        When the 'DictArrayProperty' property is set by 'Alice' to a value of
            | value                          |
            | {"x": [{"ab":12}, {"bc": 23}]} |
        Then 'Alice' receives a property change signal with the following parameters
            | name               | value                         |
            | DictArrayProperty | {"x": [{"ab":12}, {"bc": 23}]} |
        When the 'DictArrayProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                          |
            | {"x": [{"ab":12}, {"bc": 23}]} |