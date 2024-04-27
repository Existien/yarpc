Feature: DictsWithStructs interface

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
            | DictsWithStructs  | Bob  |
            | DictsWithArrays   |      |
            | DictKeys          |      |
            | Enums             |      |
            | EnumsWithArrays   |      |
            | EnumsWithDicts    |      |
            | EnumsWithStructs  |      |
        And a running service started with '{{ cookiecutter.language_folder }}_service/run.sh'
        And a mocked python client connecting to the following interfaces
            | interface        | name  |
            | DictsWithStructs | Alice |

    Scenario: Interface using dicts using structs using dicts

    # Scenario: Method call
        Given 'Bob' replies to a 'DictsStructMethod' method call with the following return value
            | value                                                |
            | {"x": SimonsDict({"1":StructDict({"a":{"ab":12}})})} |
        When the 'DictsStructMethod' method is called by 'Alice' with the following parameters
            | name    | value                             |
            | numbers | {"1":StructDict({"a":{"ab":12}})} |
        Then 'Alice' receives a return value of
            | value                                                |
            | {"x": SimonsDict({"1":StructDict({"a":{"ab":12}})})} |
        Then 'Bob' receives a 'DictsStructMethod' method call with the following parameters
            | name    | value                             |
            | numbers | {"1":StructDict({"a":{"ab":12}})} |

    # Scenario: Signal
        When a 'DictStructSignal' signal is emitted by 'Bob' with the following parameters
            | name    | value                             |
            | numbers | {"1":StructDict({"a":{"ab":12}})} |
        Then 'Alice' receives a 'DictStructSignal' signal with the following parameters
            | name    | value                             |
            | numbers | {"1":StructDict({"a":{"ab":12}})} |

    # Scenario: Get all properties
        When all properties are queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                                                                                                                                       |
            | {"DictStructProperty":{"first":StructDict({"1":{"Fizz":3,"Buzz":5},"2":{"One":1,"Two":2},}),"second":StructDict({"Legs":{"Fish":0,"Dog":4,"Ant":6},"Wings":{"Fish":0,"Dog":0,"Ant":2},}),}} |

    # Scenario: Geting and setting read-write properties
        When the 'DictStructProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                                                                                                                                                                |
            | {"first":StructDict({"1":{"Fizz":3,"Buzz":5},"2":{"One":1,"Two":2},}),"second":StructDict({"Legs":{"Fish":0,"Dog":4,"Ant":6},"Wings":{"Fish":0,"Dog":0,"Ant":2},}),} |
        When the 'DictStructProperty' property is set by 'Alice' to a value of
            | value                             |
            | {"1":StructDict({"a":{"ab":12}})} |
        Then 'Alice' receives a property change signal with the following parameters
            | name               | value                             |
            | DictStructProperty | {"1":StructDict({"a":{"ab":12}})} |
        When the 'DictStructProperty' property is queried from 'Alice'
        Then 'Alice' receives a return value of
            | value                             |
            | {"1":StructDict({"a":{"ab":12}})} |