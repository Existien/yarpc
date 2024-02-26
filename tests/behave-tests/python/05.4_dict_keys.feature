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
            | Dictionaries      |      |
            | DictsWithStructs  |      |
            | DictsWithArrays   |      |
            | DictKeys          | Bob  |
        And a running python service
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | DictKeys  | Alice |

    Scenario Outline: <name> types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a '<name>Method' method call with the following return value
            | value             |
            | {<value>: "test"} |
        When the '<name>Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {<value>: "test"} |
        Then 'Bob' receives a '<name>Method' method call with the following parameters
            | name  | value             |
            | value | {<value>: "test"} |
        When a '<name>Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {<value>: "test"} |
        Then 'Alice' receives a '<name>Signal' signal with the following parameters
            | name  | value             |
            | value | {<value>: "test"} |

        Examples: Valid ranges
            | name   | value                  |
            | Uint8  | 0                      |
            | Uint8  | 255                    |
            | Uint16 | 0                      |
            | Uint16 | 65535                  |
            | Uint32 | 0                      |
            | Uint32 | 4294967295             |
            | Uint64 | 0                      |
            | Uint64 | 18446744073709551615   |
            | Int16  | -128                   |
            | Int16  | 127                    |
            | Int32  | -2147483648            |
            | Int32  | 2147483647             |
            | Int64  | -9223372036854775808   |
            | Int64  | 9223372036854775807    |
            | Bool   | True                   |
            | Bool   | False                  |
            | String | ""                     |
            | String | "FooBarBaz"            |
            | Double | 3.14159265358979E-1022 |
            | Double | 3.14159265358979E1023  |
            | Double | 3.14159265358979E0     |