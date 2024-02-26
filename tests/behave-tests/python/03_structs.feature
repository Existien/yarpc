Feature: Structs interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           |      |
            | WithArgs          |      |
            | Primitives        |      |
            | Structs           | Bob  |
            | Arrays            |      |
            | ArraysWithStructs |      |
            | Dictionaries      |      |
            | DictsWithStructs  |      |
            | DictsWithArrays   |      |
            | DictKeys          |      |
        And a running python service
        And a mocked python client connecting to the following interfaces
            | interface | name  |
            | Structs   | Alice |

    Scenario: Method call with a non-nested struct
        Given 'Bob' replies to a 'SendStruct' method call with the following return value
            | value                             |
            | SimpleStruct(Item("Bar",3.50),12) |
        When the 'SendStruct' method is called by 'Alice' with the following parameters
            | name         | value                             |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) |
        Then 'Alice' receives a return value of
            | value                             |
            | SimpleStruct(Item("Bar",3.50),12) |
         And 'Bob' receives a 'SendStruct' method call with the following parameters
            | name         | value                             |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) |

    Scenario: Emit a signal with a non-nested struct
        When a 'StructReceived' signal is emitted by 'Bob' with the following parameters
            | name         | value                             |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) |
            | totalCosts   | 99.99                             |
        Then 'Alice' receives a 'StructReceived' signal with the following parameters
            | name         | value                             |
            | simpleStruct | SimpleStruct(Item("Foo",0.98),42) |
            | totalCosts   | 99.99                             |

    Scenario: Geting and setting read-write properties
        When the 'Simple' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                             |
            | SimpleStruct(Item("Foo",0.98),42) |
        When the 'Simple' property is set by 'Alice' to a value of
            | value                             |
            | SimpleStruct(Item("Bar",3.50),12) |
        Then 'Alice' receives a property change signal with the following parameters
            | name   | value                             |
            | Simple | SimpleStruct(Item("Bar",3.50),12) |
        When the 'Simple' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                             |
            | SimpleStruct(Item("Bar",3.50),12) |

    Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                        |
            | {"Simple":SimpleStruct(Item("Foo",0.98),42)} |