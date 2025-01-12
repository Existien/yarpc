Feature: QML instantiation interface

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
            | EnumsWithStructs  |      |
            | QmlInstantiation  | Bob  |
        And a running service started with 'qt6_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface       | name   |
            | QmlInstantiation | Alice |

    Scenario: Receive data instantiated in QML
        When the 'PassStructMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                               |
            | QmlStruct("Foo", 3.14, QmlEnum.ONE) |
        And 'Alice' receives a 'PassStructSignal' signal with the following parameters
            | name      | value                               |
            | qmlStruct | QmlStruct("Foo", 3.14, QmlEnum.ONE) |
        And 'Bob' receives a 'PassStructMethod' method call with the following parameters
            | name      | value                               |
            | qmlStruct | QmlStruct("Foo", 3.14, QmlEnum.ONE) |

        When the 'PassArrayInArrayMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value         |
            | [[1,2],[3,4]] |
        And 'Alice' receives a 'PassArrayInArraySignal' signal with the following parameters
            | name        | value         |
            | listOfLists | [[1,2],[3,4]] |
        And 'Bob' receives a 'PassArrayInArrayMethod' method call with the following parameters
            | name        | value         |
            | listOfLists | [[1,2],[3,4]] |

        When the 'PassStructsInArrayMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                     |
            | [QmlStruct("Foo", 3.14, QmlEnum.TWO),QmlStruct("Bar", 1.26, QmlEnum.OWT)] |
        And 'Alice' receives a 'PassStructsInArraySignal' signal with the following parameters
            | name          | value                                                                     |
            | listOfStructs | [QmlStruct("Foo", 3.14, QmlEnum.TWO),QmlStruct("Bar", 1.26, QmlEnum.OWT)] |
        And 'Bob' receives a 'PassStructsInArrayMethod' method call with the following parameters
            | name          | value                                                                     |
            | listOfStructs | [QmlStruct("Foo", 3.14, QmlEnum.TWO),QmlStruct("Bar", 1.26, QmlEnum.OWT)] |

        When the 'PassDictWithStringsMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                |
            | {"A": "b", "C": "d"} |
        And 'Alice' receives a 'PassDictWithStringsSignal' signal with the following parameters
            | name            | value                |
            | dictWithStrings | {"A": "b", "C": "d"} |
        And 'Bob' receives a 'PassDictWithStringsMethod' method call with the following parameters
            | name            | value                |
            | dictWithStrings | {"A": "b", "C": "d"} |

        When the 'PassDictWithNumbersMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value            |
            | {1: "b", 2: "d"} |
        And 'Alice' receives a 'PassDictWithNumbersSignal' signal with the following parameters
            | name            | value            |
            | dictWithNumbers | {1: "b", 2: "d"} |
        And 'Bob' receives a 'PassDictWithNumbersMethod' method call with the following parameters
            | name            | value            |
            | dictWithNumbers | {1: "b", 2: "d"} |

        When the 'PassDictWithStructsMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                              |
            | {"A": QmlStruct("Foo", 1.0, QmlEnum.ONE), "B": QmlStruct("Bar", 2.0, QmlEnum.TWO)} |
        And 'Alice' receives a 'PassDictWithStructsSignal' signal with the following parameters
            | name            | value                                                                              |
            | dictWithStructs | {"A": QmlStruct("Foo", 1.0, QmlEnum.ONE), "B": QmlStruct("Bar", 2.0, QmlEnum.TWO)} |
        And 'Bob' receives a 'PassDictWithStructsMethod' method call with the following parameters
            | name            | value                                                                              |
            | dictWithStructs | {"A": QmlStruct("Foo", 1.0, QmlEnum.ONE), "B": QmlStruct("Bar", 2.0, QmlEnum.TWO)} |

        When the 'PassDictInArrayMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                    |
            | [{"A": "b"}, {"C": "d"}] |
        And 'Alice' receives a 'PassDictInArraySignal' signal with the following parameters
            | name        | value                    |
            | listOfDicts | [{"A": "b"}, {"C": "d"}] |
        And 'Bob' receives a 'PassDictInArrayMethod' method call with the following parameters
            | name        | value                    |
            | listOfDicts | [{"A": "b"}, {"C": "d"}] |

        When the 'PassDictInDictMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                                |
            | {"Ab": {"A": "b"}, "Cd": {"C": "d"}} |
        And 'Alice' receives a 'PassDictInDictSignal' signal with the following parameters
            | name        | value                                |
            | dictOfDicts | {"Ab": {"A": "b"}, "Cd": {"C": "d"}} |
        And 'Bob' receives a 'PassDictInDictMethod' method call with the following parameters
            | name        | value                                |
            | dictOfDicts | {"Ab": {"A": "b"}, "Cd": {"C": "d"}} |

        When the 'PassArrayInDictMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                                |
            | {"Ab": ["A", "b"], "Cd": ["C", "d"]} |
        And 'Alice' receives a 'PassArrayInDictSignal' signal with the following parameters
            | name        | value                                |
            | dictOfLists | {"Ab": ["A", "b"], "Cd": ["C", "d"]} |
        And 'Bob' receives a 'PassArrayInDictMethod' method call with the following parameters
            | name        | value                                |
            | dictOfLists | {"Ab": ["A", "b"], "Cd": ["C", "d"]} |

        When the 'PassDictInArrayInDictMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                                    |
            | {"Ab": [{"A": "b"}], "Cd": [{"C": "d"}]} |
        And 'Alice' receives a 'PassDictInArrayInDictSignal' signal with the following parameters
            | name               | value                                    |
            | dictOfListsOfDicts | {"Ab": [{"A": "b"}], "Cd": [{"C": "d"}]} |
        And 'Bob' receives a 'PassDictInArrayInDictMethod' method call with the following parameters
            | name               | value                                    |
            | dictOfListsOfDicts | {"Ab": [{"A": "b"}], "Cd": [{"C": "d"}]} |

        When the 'PassDictInArrayInArrayMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                        |
            | [[{"A": "b"}], [{"C": "d"}]] |
        And 'Alice' receives a 'PassDictInArrayInArraySignal' signal with the following parameters
            | name               | value                        |
            | listOfListsOfDicts | [[{"A": "b"}], [{"C": "d"}]] |
        And 'Bob' receives a 'PassDictInArrayInArrayMethod' method call with the following parameters
            | name               | value                        |
            | listOfListsOfDicts | [[{"A": "b"}], [{"C": "d"}]] |

        When the 'PassDictWithEnumsMethod' method is called by 'Alice'
        Then 'Alice' receives a return value of
            | value                                                |
            | {QmlEnum.ONE: QmlEnum.ENO, QmlEnum.TWO: QmlEnum.OWT} |
        And 'Alice' receives a 'PassDictWithEnumsSignal' signal with the following parameters
            | name               | value                                                |
            | dictOfEnumsToEnums | {QmlEnum.ONE: QmlEnum.ENO, QmlEnum.TWO: QmlEnum.OWT} |
        And 'Bob' receives a 'PassDictWithEnumsMethod' method call with the following parameters
            | name               | value                                                |
            | dictOfEnumsToEnums | {QmlEnum.ONE: QmlEnum.ENO, QmlEnum.TWO: QmlEnum.OWT} |