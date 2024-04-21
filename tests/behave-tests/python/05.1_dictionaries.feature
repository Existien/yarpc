Feature: Dictionary interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           |      |
            | WithArgs          |      |
            | Primitives        |      |
            | Structs           |      |
            | Arrays            |      |
            | ArraysWithStructs |      |
            | Dictionaries      | Bob  |
            | DictsWithStructs  |      |
            | DictsWithArrays   |      |
            | DictKeys          |      |
            | Enums             |      |
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
        And a running service started with 'python_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface    | name  |
            | Dictionaries | Alice |

    Scenario: Interface using dictionaries

    # Scenario: Method call
        Given 'Bob' replies to a 'DictMethod' method call with the following return value
            | value             |
            | {"1":"a","2":"b"} |
        When the 'DictMethod' method is called by 'Alice' with the following parameters
            | name        | value         |
            | keysNValues | {"a":1,"b":2} |
        Then 'Alice' receives a return value of
            | value             |
            | {"1":"a","2":"b"} |
        Then 'Bob' receives a 'DictMethod' method call with the following parameters
            | name        | value         |
            | keysNValues | {"a":1,"b":2} |

    # Scenario: Signal
        When a 'DictSignal' signal is emitted by 'Bob' with the following parameters
            | name        | value         |
            | keysNValues | {"a":1,"b":2} |
        Then 'Alice' receives a 'DictSignal' signal with the following parameters
            | name        | value         |
            | keysNValues | {"a":1,"b":2} |

    # Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                |
            | {"DictProperty":{"Fizz":3,"Buzz":5}} |

    # Scenario: Geting and setting read-write properties
        When the 'DictProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value               |
            | {"Fizz":3,"Buzz":5} |
        When the 'DictProperty' property is set by 'Alice' to a value of
            | value         |
            | {"a":2,"b":4} |
        Then 'Alice' receives a property change signal with the following parameters
            | name         | value         |
            | DictProperty | {"a":2,"b":4} |
        When the 'DictProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value         |
            | {"a":2,"b":4} |