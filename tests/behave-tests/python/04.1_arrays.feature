Feature: Arrays interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           |      |
            | WithArgs          |      |
            | Primitives        |      |
            | Structs           |      |
            | Arrays            | Bob  |
            | ArraysWithStructs |      |
            | Dictionaries      |      |
            | DictsWithStructs  |      |
            | DictsWithArrays   |      |
            | DictKeys          |      |
            | Enums             |      |
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
        And a running service started with 'python_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | Arrays    | Alice |

    Scenario: Interface using arrays

    # Scenario: Method call
        Given 'Bob' replies to a 'ArrayMethod' method call with the following return value
            | value             |
            | [[4.5,5.5],[6.5]] |
        When the 'ArrayMethod' method is called by 'Alice' with the following parameters
            | name    | value       |
            | numbers | [[1,2],[3]] |
        Then 'Alice' receives a return value of
            | value             |
            | [[4.5,5.5],[6.5]] |
        Then 'Bob' receives a 'ArrayMethod' method call with the following parameters
            | name    | value       |
            | numbers | [[1,2],[3]] |

    # Scenario: Signal
        When a 'ArraySignal' signal is emitted by 'Bob' with the following parameters
            | name    | value             |
            | numbers | [[4.5],[5.5,6.5]] |
        Then 'Alice' receives a 'ArraySignal' signal with the following parameters
            | name    | value             |
            | numbers | [[4.5],[5.5,6.5]] |

    # Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                     |
            | {"ArrayProperty":[["Foo","Bar"],["Baz"]]} |

    # Scenario: Geting and setting read-write properties
        When the 'ArrayProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                   |
            | [["Foo","Bar"],["Baz"]] |
        When the 'ArrayProperty' property is set by 'Alice' to a value of
            | value                          |
            | [["Fizz","Buzz"],["FizzBuzz"]] |
        Then 'Alice' receives a property change signal with the following parameters
            | name          | value                          |
            | ArrayProperty | [["Fizz","Buzz"],["FizzBuzz"]] |
        When the 'ArrayProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                          |
            | [["Fizz","Buzz"],["FizzBuzz"]] |