Feature: Minimal interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           | Bob  |
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
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
            | QmlInstantiation  |      |
        And a running service started with 'qt6_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | Minimal   | Alice |

    Scenario: Interface using signals and methods without args

    # Scenario: Method call without arguments or return value
        When the 'Bump' method is called by 'Alice'
        Then 'Bob' receives a 'Bump' method call

    # Scenario: Emit a signal without arguments
        When a 'Bumped' signal is emitted by 'Bob'
        Then 'Alice' receives a 'Bumped' signal
