Feature: Structs interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface  | name |
            | Minimal    |      |
            | WithArgs   |      |
            | Primitives |      |
            | Structs    | Bob  |
        And a running python service
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | Structs   | Alice |

    Scenario: Method call with a non-nested struct
        Given 'Bob' replies to a 'SendStruct' method call with the following return value
            | value                             | type |
            | SimpleStruct(Item("Bar",3.50),12) | py   |
        When the 'SendStruct' method is called by 'Alice' with the following parameters
            | name         | value                             | type |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) | py   |
        Then 'Alice' receives a return value of
            | value                             | type |
            | SimpleStruct(Item("Bar",3.50),12) | py   |
         And 'Bob' receives a 'SendStruct' method call with the following parameters
            | name         | value                             | type |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) | py   |

    Scenario: Emit a signal with a non-nested struct
        When a 'StructReceived' signal is emitted by 'Bob' with the following parameters
            | name         | value                             | type    |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) | py      |
            | totalCosts   | 99.99                             | float   |
        Then 'Alice' receives a 'StructReceived' signal with the following parameters
            | name         | value                             | type    |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) | py      |
            | totalCosts   | 99.99                             | float   |

    Scenario: Geting and setting read-write properties
        When the 'Simple' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                             | type |
            | SimpleStruct(Item("Foo",0.98),42) | py   |
        When the 'Simple' property is set by 'Alice' to a value of
            | value                             | type |
            | SimpleStruct(Item("Bar",3.50),12) | py   |
        Then 'Alice' receives a property change signal with the following parameters
            | name   | value                             | type |
            | Simple | SimpleStruct(Item("Bar",3.50),12) | py   |
        When the 'Simple' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                             | type |
            | SimpleStruct(Item("Bar",3.50),12) | py   |

    Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                        | type |
            | {"Simple":SimpleStruct(Item("Foo",0.98),42)} | py   |