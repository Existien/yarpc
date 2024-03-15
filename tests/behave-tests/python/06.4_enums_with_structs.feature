Feature: WithArgs interface

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
            | DictKeys          |      |
            | Enums             |      |
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  | Bob  |
        And a running python service
        And a mocked python client connecting to the following interfaces
            | interface        | name  |
            | EnumsWithStructs | Alice |

    Scenario: Emit a signal with a single parameter
        When a 'EnumSignal' signal is emitted by 'Bob' with the following parameters
            | name  | value                                                                                                   |
            | color | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |
        Then 'Alice' receives a 'EnumSignal' signal with the following parameters
            | name  | value                                                                                                   |
            | color | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |

    Scenario: Method call with multiple arguments and a return value
        Given 'Bob' replies to a 'EnumMethod' method call with the following return value
            | value                                                                                                   |
            | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |
        When the 'EnumMethod' method is called by 'Alice' with the following parameters
            | name  | value                                                                                                   |
            | color | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |
        Then 'Alice' receives a return value of
            | value                                                                                                   |
            | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |
        And 'Bob' receives a 'EnumMethod' method call with the following parameters
            | name  | value                                                                                                   |
            | color | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |

    Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                                                                                                                             |
            | {"EnumProperty":EnumStruct(color=Color.GREEN,colorArray=[Color.RED, Color.GREEN, Color.BLUE],colorDict={Color.RED: Color.GREEN,Color.GREEN: Color.RED,Color.BLUE: Color.ORANGE})} |

    Scenario: Geting and setting read-write properties
        When the 'EnumProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                                                                                                            |
            | EnumStruct(color=Color.GREEN,colorArray=[Color.RED, Color.GREEN, Color.BLUE],colorDict={Color.RED: Color.GREEN,Color.GREEN: Color.RED,Color.BLUE: Color.ORANGE}) |
        When the 'EnumProperty' property is set by 'Alice' to a value of
            | value                                                                                                   |
            | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |
        Then 'Alice' receives a property change signal with the following parameters
            | name         | value                                                                                                   |
            | EnumProperty | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |
        When the 'EnumProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                                                   |
            | EnumStruct(color=Color.ORANGE,colorArray=[Color.RED, Color.GREEN],colorDict={Color.BLUE: Color.ORANGE}) |

