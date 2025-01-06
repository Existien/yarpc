Feature: WithArgs interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           |      |
            | WithArgs          | Bob  |
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
            | WithArgs  | Alice |

    Scenario: Interface using only primitive types

    # Scenario: Method call with a single argument, without a return value
        When the 'Notify' method is called by 'Alice' with the following parameters
            | name    | value |
            | message | "Foo" |
        Then 'Bob' receives a 'Notify' method call with the following parameters
            | name    | value |
            | message | "Foo" |

    # Scenario: Emit a signal with a single parameter
        When a 'Notified' signal is emitted by 'Bob' with the following parameters
            | name    | value |
            | message | "Foo" |
        Then 'Alice' receives a 'Notified' signal with the following parameters
            | name    | value |
            | message | "Foo" |

    # Scenario: Method call with multiple arguments and a return value
        Given 'Bob' replies to a 'Order' method call with the following return value
            | value |
            | 6.022 |
        When the 'Order' method is called by 'Alice' with the following parameters
            | name         | value     |
            | item         | "Marbles" |
            | amount       | 33        |
            | pricePerItem | 0.33      |
        Then 'Alice' receives a return value of
            | value |
            | 6.022 |
        And 'Bob' receives a 'Order' method call with the following parameters
            | name         | value     |
            | item         | "Marbles" |
            | amount       | 33        |
            | pricePerItem | 0.33      |

    # Scenario: Emit a signal with multiple parameters
        When a 'OrderReceived' signal is emitted by 'Bob' with the following parameters
            | name         | value     |
            | item         | "Marbles" |
            | amount       | 33        |
            | pricePerItem | 0.33      |
        Then 'Alice' receives a 'OrderReceived' signal with the following parameters
            | name         | value     |
            | item         | "Marbles" |
            | amount       | 33        |
            | pricePerItem | 0.33      |

    # Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                         |
            | {"Speed":10.0,"Distance":200,"Duration":20.0} |

    # Scenario: Getting read-only properties
        When the 'Duration' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value |
            | 20.0  |

    # Scenario: Geting and setting read-write properties
        When the 'Distance' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value |
            | 200 |
        When the 'Distance' property is set by 'Alice' to a value of
            | value |
            | 50 |
        Then 'Alice' receives a property change signal with the following parameters
            | name   | value |
            | Distance | 50 |
        When the 'Distance' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value |
            | 50 |
        When the 'Speed' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value |
            | 10.0 |
        When the 'Speed' property is set by 'Alice' to a value of
            | value |
            | 5 |
        Then 'Alice' receives a property change signal with the following parameters
            | name   | value |
            | Speed | 5 |
        When the 'Speed' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value |
            | 5 |
