Feature: DictKeys interface

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
            | Enums             |      |
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
        And a running service started with 'qt6_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | DictKeys  | Alice |

    Scenario: Interface using dictionaries with different keys

    # Scenario: Uint8 types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'Uint8Method' method call with the following return value
            | value             |
            | {0: "test"} |
        When the 'Uint8Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Bob' receives a 'Uint8Method' method call with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        When a 'Uint8Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Alice' receives a 'Uint8Signal' signal with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Given 'Bob' replies to a 'Uint8Method' method call with the following return value
            | value             |
            | {255: "test"} |
        When the 'Uint8Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {255: "test"} |
        Then 'Bob' receives a 'Uint8Method' method call with the following parameters
            | name  | value             |
            | value | {255: "test"} |
        When a 'Uint8Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {255: "test"} |
        Then 'Alice' receives a 'Uint8Signal' signal with the following parameters
            | name  | value             |
	    | value | {255: "test"} |

    # Scenario: Uint16 types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'Uint16Method' method call with the following return value
            | value             |
            | {0: "test"} |
        When the 'Uint16Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Bob' receives a 'Uint16Method' method call with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        When a 'Uint16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Alice' receives a 'Uint16Signal' signal with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Given 'Bob' replies to a 'Uint16Method' method call with the following return value
            | value             |
            | {65535: "test"} |
        When the 'Uint16Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {65535: "test"} |
        Then 'Bob' receives a 'Uint16Method' method call with the following parameters
            | name  | value             |
            | value | {65535: "test"} |
        When a 'Uint16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {65535: "test"} |
        Then 'Alice' receives a 'Uint16Signal' signal with the following parameters
            | name  | value             |
	    | value | {65535: "test"} |

    # Scenario: Uint32 types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'Uint32Method' method call with the following return value
            | value             |
            | {0: "test"} |
        When the 'Uint32Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Bob' receives a 'Uint32Method' method call with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        When a 'Uint32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Alice' receives a 'Uint32Signal' signal with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Given 'Bob' replies to a 'Uint32Method' method call with the following return value
            | value             |
            | {4294967295: "test"} |
        When the 'Uint32Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {4294967295: "test"} |
        Then 'Bob' receives a 'Uint32Method' method call with the following parameters
            | name  | value             |
            | value | {4294967295: "test"} |
        When a 'Uint32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {4294967295: "test"} |
        Then 'Alice' receives a 'Uint32Signal' signal with the following parameters
            | name  | value             |
	    | value | {4294967295: "test"} |

    # Scenario: Uint64 types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'Uint64Method' method call with the following return value
            | value             |
            | {0: "test"} |
        When the 'Uint64Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Bob' receives a 'Uint64Method' method call with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        When a 'Uint64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Then 'Alice' receives a 'Uint64Signal' signal with the following parameters
            | name  | value             |
            | value | {0: "test"} |
        Given 'Bob' replies to a 'Uint64Method' method call with the following return value
            | value             |
            | {18446744073709551615: "test"} |
        When the 'Uint64Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {18446744073709551615: "test"} |
        Then 'Bob' receives a 'Uint64Method' method call with the following parameters
            | name  | value             |
            | value | {18446744073709551615: "test"} |
        When a 'Uint64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {18446744073709551615: "test"} |
        Then 'Alice' receives a 'Uint64Signal' signal with the following parameters
            | name  | value             |
	    | value | {18446744073709551615: "test"} |

    # Scenario: Int16 types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'Int16Method' method call with the following return value
            | value             |
            | {-128: "test"} |
        When the 'Int16Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {-128: "test"} |
        Then 'Bob' receives a 'Int16Method' method call with the following parameters
            | name  | value             |
            | value | {-128: "test"} |
        When a 'Int16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {-128: "test"} |
        Then 'Alice' receives a 'Int16Signal' signal with the following parameters
            | name  | value             |
            | value | {-128: "test"} |
        Given 'Bob' replies to a 'Int16Method' method call with the following return value
            | value             |
            | {127: "test"} |
        When the 'Int16Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {127: "test"} |
        Then 'Bob' receives a 'Int16Method' method call with the following parameters
            | name  | value             |
            | value | {127: "test"} |
        When a 'Int16Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {127: "test"} |
        Then 'Alice' receives a 'Int16Signal' signal with the following parameters
            | name  | value             |
            | value | {127: "test"} |

    # Scenario: Int32 types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'Int32Method' method call with the following return value
            | value             |
            | {-2147483648: "test"} |
        When the 'Int32Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {-2147483648: "test"} |
        Then 'Bob' receives a 'Int32Method' method call with the following parameters
            | name  | value             |
            | value | {-2147483648: "test"} |
        When a 'Int32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {-2147483648: "test"} |
        Then 'Alice' receives a 'Int32Signal' signal with the following parameters
            | name  | value             |
            | value | {-2147483648: "test"} |
        Given 'Bob' replies to a 'Int32Method' method call with the following return value
            | value             |
            | {2147483647: "test"} |
        When the 'Int32Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {2147483647: "test"} |
        Then 'Bob' receives a 'Int32Method' method call with the following parameters
            | name  | value             |
            | value | {2147483647: "test"} |
        When a 'Int32Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {2147483647: "test"} |
        Then 'Alice' receives a 'Int32Signal' signal with the following parameters
            | name  | value             |
            | value | {2147483647: "test"} |

    # Scenario: Int64 types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'Int64Method' method call with the following return value
            | value             |
            | {-9223372036854775808: "test"} |
        When the 'Int64Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {-9223372036854775808: "test"} |
        Then 'Bob' receives a 'Int64Method' method call with the following parameters
            | name  | value             |
            | value | {-9223372036854775808: "test"} |
        When a 'Int64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {-9223372036854775808: "test"} |
        Then 'Alice' receives a 'Int64Signal' signal with the following parameters
            | name  | value             |
            | value | {-9223372036854775808: "test"} |
        Given 'Bob' replies to a 'Int64Method' method call with the following return value
            | value             |
            | {9223372036854775807: "test"} |
        When the 'Int64Method' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {9223372036854775807: "test"} |
        Then 'Bob' receives a 'Int64Method' method call with the following parameters
            | name  | value             |
            | value | {9223372036854775807: "test"} |
        When a 'Int64Signal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {9223372036854775807: "test"} |
        Then 'Alice' receives a 'Int64Signal' signal with the following parameters
            | name  | value             |
            | value | {9223372036854775807: "test"} |

    # Scenario: Bool types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'BoolMethod' method call with the following return value
            | value             |
            | {True: "test"} |
        When the 'BoolMethod' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {True: "test"} |
        Then 'Bob' receives a 'BoolMethod' method call with the following parameters
            | name  | value             |
            | value | {True: "test"} |
        When a 'BoolSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {True: "test"} |
        Then 'Alice' receives a 'BoolSignal' signal with the following parameters
            | name  | value             |
            | value | {True: "test"} |
        Given 'Bob' replies to a 'BoolMethod' method call with the following return value
            | value             |
            | {False: "test"} |
        When the 'BoolMethod' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {False: "test"} |
        Then 'Bob' receives a 'BoolMethod' method call with the following parameters
            | name  | value             |
            | value | {False: "test"} |
        When a 'BoolSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {False: "test"} |
        Then 'Alice' receives a 'BoolSignal' signal with the following parameters
            | name  | value             |
	    | value | {False: "test"} |

    # Scenario: String types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'StringMethod' method call with the following return value
            | value             |
            | {"FooBarBaz": "test"} |
        When the 'StringMethod' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {"FooBarBaz": "test"} |
        Then 'Bob' receives a 'StringMethod' method call with the following parameters
            | name  | value             |
            | value | {"FooBarBaz": "test"} |
        When a 'StringSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {"FooBarBaz": "test"} |
        Then 'Alice' receives a 'StringSignal' signal with the following parameters
            | name  | value             |
            | value | {"FooBarBaz": "test"} |
        Given 'Bob' replies to a 'StringMethod' method call with the following return value
            | value             |
            | {"": "test"} |
        When the 'StringMethod' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {"": "test"} |
        Then 'Bob' receives a 'StringMethod' method call with the following parameters
            | name  | value             |
            | value | {"": "test"} |
        When a 'StringSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {"": "test"} |
        Then 'Alice' receives a 'StringSignal' signal with the following parameters
            | name  | value             |
	    | value | {"": "test"} |

    # Scenario: Double types are transmitted correctly as dictionary keys in methods and signals
        Given 'Bob' replies to a 'DoubleMethod' method call with the following return value
            | value             |
            | {3.14159265358979E-1022: "test"} |
        When the 'DoubleMethod' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {3.14159265358979E-1022: "test"} |
        Then 'Bob' receives a 'DoubleMethod' method call with the following parameters
            | name  | value             |
            | value | {3.14159265358979E-1022: "test"} |
        When a 'DoubleSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {3.14159265358979E-1022: "test"} |
        Then 'Alice' receives a 'DoubleSignal' signal with the following parameters
            | name  | value             |
            | value | {3.14159265358979E-1022: "test"} |
        Given 'Bob' replies to a 'DoubleMethod' method call with the following return value
            | value             |
            | {3.14159265358979E1023: "test"} |
        When the 'DoubleMethod' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {3.14159265358979E1023: "test"} |
        Then 'Bob' receives a 'DoubleMethod' method call with the following parameters
            | name  | value             |
            | value | {3.14159265358979E1023: "test"} |
        When a 'DoubleSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {3.14159265358979E1023: "test"} |
        Then 'Alice' receives a 'DoubleSignal' signal with the following parameters
            | name  | value             |
            | value | {3.14159265358979E1023: "test"} |
        Given 'Bob' replies to a 'DoubleMethod' method call with the following return value
            | value             |
            | {3.14159265358979E0: "test"} |
        When the 'DoubleMethod' method is called by 'Alice' with the following parameters
            | name  | value             |
            | value | {3.14159265358979E0: "test"} |
        Then 'Bob' receives a 'DoubleMethod' method call with the following parameters
            | name  | value             |
            | value | {3.14159265358979E0: "test"} |
        When a 'DoubleSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value             |
            | value | {3.14159265358979E0: "test"} |
        Then 'Alice' receives a 'DoubleSignal' signal with the following parameters
            | name  | value             |
            | value | {3.14159265358979E0: "test"} |
