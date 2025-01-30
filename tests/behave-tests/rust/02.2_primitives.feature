Feature: Primitives interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           |      |
            | WithArgs          |      |
            | Primitives        | Bob  |
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
        And a running service started with 'rust_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface  | name  |
            | Primitives | Alice |

    Scenario: Interface using all builtin primitive types

    # Scenario: Uint8 types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'Uint8Method' method call with the following return value
            | value   |
            | 0 |
        When the 'Uint8Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Bob' receives a 'Uint8Method' method call with the following parameters
            | name  | value   |
            | value | 0 |
        When a 'Uint8Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Alice' receives a 'Uint8Signal' signal with the following parameters
            | name  | value   |
            | value | 0 |
        Given 'Bob' replies to a 'Uint8Method' method call with the following return value
            | value   |
            | 255 |
        When the 'Uint8Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 255 |
        Then 'Bob' receives a 'Uint8Method' method call with the following parameters
            | name  | value   |
            | value | 255 |
        When a 'Uint8Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 255 |
        Then 'Alice' receives a 'Uint8Signal' signal with the following parameters
            | name  | value   |
            | value | 255 |

    # Scenario: Uint16 types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'Uint16Method' method call with the following return value
            | value   |
            | 0 |
        When the 'Uint16Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Bob' receives a 'Uint16Method' method call with the following parameters
            | name  | value   |
            | value | 0 |
        When a 'Uint16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Alice' receives a 'Uint16Signal' signal with the following parameters
            | name  | value   |
            | value | 0 |
        Given 'Bob' replies to a 'Uint16Method' method call with the following return value
            | value   |
            | 65535 |
        When the 'Uint16Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 65535 |
        Then 'Bob' receives a 'Uint16Method' method call with the following parameters
            | name  | value   |
            | value | 65535 |
        When a 'Uint16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 65535 |
        Then 'Alice' receives a 'Uint16Signal' signal with the following parameters
            | name  | value   |
            | value | 65535 |

    # Scenario: Uint32 types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'Uint32Method' method call with the following return value
            | value   |
            | 0 |
        When the 'Uint32Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Bob' receives a 'Uint32Method' method call with the following parameters
            | name  | value   |
            | value | 0 |
        When a 'Uint32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Alice' receives a 'Uint32Signal' signal with the following parameters
            | name  | value   |
            | value | 0 |
        Given 'Bob' replies to a 'Uint32Method' method call with the following return value
            | value   |
            | 4294967295 |
        When the 'Uint32Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 4294967295 |
        Then 'Bob' receives a 'Uint32Method' method call with the following parameters
            | name  | value   |
            | value | 4294967295 |
        When a 'Uint32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 4294967295 |
        Then 'Alice' receives a 'Uint32Signal' signal with the following parameters
            | name  | value   |
            | value | 4294967295 |

    # Scenario: Uint64 types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'Uint64Method' method call with the following return value
            | value   |
            | 0 |
        When the 'Uint64Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Bob' receives a 'Uint64Method' method call with the following parameters
            | name  | value   |
            | value | 0 |
        When a 'Uint64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 0 |
        Then 'Alice' receives a 'Uint64Signal' signal with the following parameters
            | name  | value   |
            | value | 0 |
        Given 'Bob' replies to a 'Uint64Method' method call with the following return value
            | value   |
            | 18446744073709551615 |
        When the 'Uint64Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 18446744073709551615 |
        Then 'Bob' receives a 'Uint64Method' method call with the following parameters
            | name  | value   |
            | value | 18446744073709551615 |
        When a 'Uint64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 18446744073709551615 |
        Then 'Alice' receives a 'Uint64Signal' signal with the following parameters
            | name  | value   |
            | value | 18446744073709551615 |


    # Scenario: Int16 types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'Int16Method' method call with the following return value
            | value   |
            | -128 |
        When the 'Int16Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | -128 |
        Then 'Bob' receives a 'Int16Method' method call with the following parameters
            | name  | value   |
            | value | -128 |
        When a 'Int16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | -128 |
        Then 'Alice' receives a 'Int16Signal' signal with the following parameters
            | name  | value   |
            | value | -128 |
        Given 'Bob' replies to a 'Int16Method' method call with the following return value
            | value   |
            | 127 |
        When the 'Int16Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 127 |
        Then 'Bob' receives a 'Int16Method' method call with the following parameters
            | name  | value   |
            | value | 127 |
        When a 'Int16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 127 |
        Then 'Alice' receives a 'Int16Signal' signal with the following parameters
            | name  | value   |
            | value | 127 |

    # Scenario: Int32 types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'Int32Method' method call with the following return value
            | value   |
            | -2147483648 |
        When the 'Int32Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | -2147483648 |
        Then 'Bob' receives a 'Int32Method' method call with the following parameters
            | name  | value   |
            | value | -2147483648 |
        When a 'Int32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | -2147483648 |
        Then 'Alice' receives a 'Int32Signal' signal with the following parameters
            | name  | value   |
            | value | -2147483648 |
        Given 'Bob' replies to a 'Int32Method' method call with the following return value
            | value   |
            | 2147483647 |
        When the 'Int32Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 2147483647 |
        Then 'Bob' receives a 'Int32Method' method call with the following parameters
            | name  | value   |
            | value | 2147483647 |
        When a 'Int32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 2147483647 |
        Then 'Alice' receives a 'Int32Signal' signal with the following parameters
            | name  | value   |
            | value | 2147483647 |

    # Scenario: Int64 types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'Int64Method' method call with the following return value
            | value   |
            | -9223372036854775808 |
        When the 'Int64Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | -9223372036854775808 |
        Then 'Bob' receives a 'Int64Method' method call with the following parameters
            | name  | value   |
            | value | -9223372036854775808 |
        When a 'Int64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | -9223372036854775808 |
        Then 'Alice' receives a 'Int64Signal' signal with the following parameters
            | name  | value   |
            | value | -9223372036854775808 |
        Given 'Bob' replies to a 'Int64Method' method call with the following return value
            | value   |
            | 9223372036854775807 |
        When the 'Int64Method' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 9223372036854775807 |
        Then 'Bob' receives a 'Int64Method' method call with the following parameters
            | name  | value   |
            | value | 9223372036854775807 |
        When a 'Int64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 9223372036854775807 |
        Then 'Alice' receives a 'Int64Signal' signal with the following parameters
            | name  | value   |
	    | value | 9223372036854775807 |

    # Scenario: Bool types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'BoolMethod' method call with the following return value
            | value   |
            | True |
        When the 'BoolMethod' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | True |
        Then 'Bob' receives a 'BoolMethod' method call with the following parameters
            | name  | value   |
            | value | True |
        When a 'BoolSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | True |
        Then 'Alice' receives a 'BoolSignal' signal with the following parameters
            | name  | value   |
            | value | True |
        Given 'Bob' replies to a 'BoolMethod' method call with the following return value
            | value   |
            | False |
        When the 'BoolMethod' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | False |
        Then 'Bob' receives a 'BoolMethod' method call with the following parameters
            | name  | value   |
            | value | False |
        When a 'BoolSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | False |
        Then 'Alice' receives a 'BoolSignal' signal with the following parameters
            | name  | value   |
	    | value | False |

    # Scenario: String types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'StringMethod' method call with the following return value
            | value   |
            | "FooBarBaz" |
        When the 'StringMethod' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | "FooBarBaz" |
        Then 'Bob' receives a 'StringMethod' method call with the following parameters
            | name  | value   |
            | value | "FooBarBaz" |
        When a 'StringSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | "FooBarBaz" |
        Then 'Alice' receives a 'StringSignal' signal with the following parameters
            | name  | value   |
            | value | "FooBarBaz" |
        Given 'Bob' replies to a 'StringMethod' method call with the following return value
            | value   |
            | "" |
        When the 'StringMethod' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | "" |
        Then 'Bob' receives a 'StringMethod' method call with the following parameters
            | name  | value   |
            | value | "" |
        When a 'StringSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | "" |
        Then 'Alice' receives a 'StringSignal' signal with the following parameters
            | name  | value   |
	    | value | "" |

    # Scenario: Double types are transmitted correctly in methods and signals
        Given 'Bob' replies to a 'DoubleMethod' method call with the following return value
            | value   |
            | 3.14159265358979E-1022 |
        When the 'DoubleMethod' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 3.14159265358979E-1022 |
        Then 'Bob' receives a 'DoubleMethod' method call with the following parameters
            | name  | value   |
            | value | 3.14159265358979E-1022 |
        When a 'DoubleSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 3.14159265358979E-1022 |
        Then 'Alice' receives a 'DoubleSignal' signal with the following parameters
            | name  | value   |
            | value | 3.14159265358979E-1022 |
        Given 'Bob' replies to a 'DoubleMethod' method call with the following return value
            | value   |
            | 3.14159265358979E1023 |
        When the 'DoubleMethod' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 3.14159265358979E1023 |
        Then 'Bob' receives a 'DoubleMethod' method call with the following parameters
            | name  | value   |
            | value | 3.14159265358979E1023 |
        When a 'DoubleSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 3.14159265358979E1023 |
        Then 'Alice' receives a 'DoubleSignal' signal with the following parameters
            | name  | value   |
            | value | 3.14159265358979E1023 |
        Given 'Bob' replies to a 'DoubleMethod' method call with the following return value
            | value   |
            | 3.14159265358979E0 |
        When the 'DoubleMethod' method is called by 'Alice' with the following parameters
            | name  | value   |
            | value | 3.14159265358979E0 |
        Then 'Bob' receives a 'DoubleMethod' method call with the following parameters
            | name  | value   |
            | value | 3.14159265358979E0 |
        When a 'DoubleSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value   |
            | value | 3.14159265358979E0 |
        Then 'Alice' receives a 'DoubleSignal' signal with the following parameters
            | name  | value   |
            | value | 3.14159265358979E0 |
