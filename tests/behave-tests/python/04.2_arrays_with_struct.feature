Feature: Arrays interface

    Background:
        Given a mocked backend service with the following interfaces
            | interface         | name |
            | Minimal           |      |
            | WithArgs          |      |
            | Primitives        |      |
            | Structs           |      |
            | Arrays            |      |
            | ArraysWithStructs | Bob  |
            | Dictionaries      |      |
            | DictsWithStructs  |      |
            | DictsWithArrays   |      |
            | DictKeys          |      |
        And a running python service
        And a mocked python client connecting to the following interfaces
            | interface         | name  |
            | ArraysWithStructs | Alice |

    Scenario: Method call
        Given 'Bob' replies to a 'ArrayStructMethod' method call with the following return value
            | value                                                           |
            | [SimonsArray([StructArray([[1],[2]]), StructArray([[3],[4]])])] |
        When the 'ArrayStructMethod' method is called by 'Alice' with the following parameters
            | name    | value                            |
            | numbers | [StructArray([[11,12],[21,22]])] |
        Then 'Alice' receives a return value of
            | value                                                           |
            | [SimonsArray([StructArray([[1],[2]]), StructArray([[3],[4]])])] |
        Then 'Bob' receives a 'ArrayStructMethod' method call with the following parameters
            | name    | value                            |
            | numbers | [StructArray([[11,12],[21,22]])] |

    Scenario: Signal
        When a 'ArrayStructSignal' signal is emitted by 'Bob' with the following parameters
            | name    | value                            |
            | numbers | [StructArray([[11,12],[21,22]])] |
        Then 'Alice' receives a 'ArrayStructSignal' signal with the following parameters
            | name    | value                            |
            | numbers | [StructArray([[11,12],[21,22]])] |

    Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                 |
            | {"ArrayStructProperty":[StructArray([[1],[2]]),StructArray([[3,4]])]} |

    Scenario: Geting and setting read-write properties
        When the 'ArrayStructProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                         |
            | [StructArray([[1],[2]]),StructArray([[3,4]])] |
        When the 'ArrayStructProperty' property is set by 'Alice' to a value of
            | value                                             |
            | [StructArray([[11,12]]),StructArray([[21],[22]])] |
        Then 'Alice' receives a property change signal with the following parameters
            | name                | value                                             |
            | ArrayStructProperty | [StructArray([[11,12]]),StructArray([[21],[22]])] |
        When the 'ArrayStructProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                             |
            | [StructArray([[11,12]]),StructArray([[21],[22]])] |