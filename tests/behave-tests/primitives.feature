Feature: Primitives interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface  | name |
            | Minimal    |      |
            | WithArgs   |      |
            | Primitives | Bob  |
        And a running python service
        And a mocked python client connecting to the following interfaces
            | interface  | name  |
            | Primitives | Alice |

    Scenario Outline: <name> types are transmitted correctly in methods and signals
        Given 'Bob' replies to a '<name>Method' method call with the following return value
            | value   | type   |
            | <value> | <type> |
        When the '<name>Method' method is called by 'Alice' with the following parameters
            | name  | value   | type   |
            | value | <value> | <type> |
        Then 'Bob' receives a '<name>Method' method call with the following parameters
            | name  | value   | type   |
            | value | <value> | <type> |
        When a '<name>Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   | type   |
            | value | <value> | <type> |
        Then 'Alice' receives a '<name>Signal' signal with the following parameters
            | name  | value   | type   |
            | value | <value> | <type> |

        Examples: Valid ranges
            | name   | value                  | type  |
            | Uint8  | 0                      | int   |
            | Uint8  | 255                    | int   |
            | Uint16 | 0                      | int   |
            | Uint16 | 65535                  | int   |
            | Uint32 | 0                      | int   |
            | Uint32 | 4294967295             | int   |
            | Uint64 | 0                      | int   |
            | Uint64 | 18446744073709551615   | int   |
            | Int16  | -128                   | int   |
            | Int16  | 127                    | int   |
            | Int32  | -2147483648            | int   |
            | Int32  | 2147483647             | int   |
            | Int64  | -9223372036854775808   | int   |
            | Int64  | 9223372036854775807    | int   |
            | Bool   | True                   | bool  |
            | Bool   | False                  | bool  |
            | String |                        | str   |
            | String | FooBarBaz              | str   |
            | Double | 3.14159265358979E-1022 | float |
            | Double | 3.14159265358979E1023  | float |
            | Double | 3.14159265358979E0     | float |