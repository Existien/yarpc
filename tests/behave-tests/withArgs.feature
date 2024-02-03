Feature: WithArgs interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface  | name |
            | Minimal    |      |
            | WithArgs   | Bob  |
            | Primitives |      |
            | Structs    |      |
        And a running python service
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | WithArgs  | Alice |

    Scenario: Method call with a single argument, without a return value
        When the 'Notify' method is called by 'Alice' with the following parameters
            | name    | value | type |
            | message | Foo   | str  |
        Then 'Bob' receives a 'Notify' method call with the following parameters
            | name    | value | type |
            | message | Foo   | str  |

    Scenario: Emit a signal with a single parameter
        When a 'Notified' signal is emitted by 'Bob' with the following parameters
            | name    | value | type |
            | message | Foo   | str  |
        Then 'Alice' receives a 'Notified' signal with the following parameters
            | name    | value | type |
            | message | Foo   | str  |

    Scenario: Method call with multiple arguments and a return value
        Given 'Bob' replies to a 'Order' method call with the following return value
            | value | type  |
            | 6.022 | float |
        When the 'Order' method is called by 'Alice' with the following parameters
            | name         | value   | type  |
            | item         | Marbles | str   |
            | amount       | 33      | int   |
            | pricePerItem | 0.33    | float |
        Then 'Alice' receives a return value of
            | value | type  |
            | 6.022 | float |
        And 'Bob' receives a 'Order' method call with the following parameters
            | name         | value   | type  |
            | item         | Marbles | str   |
            | amount       | 33      | int   |
            | pricePerItem | 0.33    | float |

    Scenario: Emit a signal with multiple parameters
        When a 'OrderReceived' signal is emitted by 'Bob' with the following parameters
            | name         | value   | type  |
            | item         | Marbles | str   |
            | amount       | 33      | int   |
            | pricePerItem | 0.33    | float |
        Then 'Alice' receives a 'OrderReceived' signal with the following parameters
            | name         | value   | type  |
            | item         | Marbles | str   |
            | amount       | 33      | int   |
            | pricePerItem | 0.33    | float |

    Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                         | type |
            | {"Speed":10.0,"Distance":200,"Duration":20.0} | json |

    Scenario: Getting read-only properties
        When the 'Duration' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value | type  |
            | 20.0  | float |

    Scenario Outline: Geting and setting read-write properties
        When the '<prop>' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value | type   |
            | <old> | <type> |
        When the '<prop>' property is set by 'Alice' to a value of
            | value | type   |
            | <new> | <type> |
        Then 'Alice' receives a property change signal with the following parameters
            | name   | value | type   |
            | <prop> | <new> | <type> |
        When the '<prop>' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value | type   |
            | <new> | <type> |

        Examples: Properties
            | prop     | old  | new  | type  |
            | Distance | 200  | 50   | int   |
            | Speed    | 10.0 | 5    | float |
