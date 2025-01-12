import QtQuick
import gen.qml_instantiation

Item {
    Component.onCompleted: {
        QmlAsServiceInterface.connect()
    }

    QmlAsClient {
        id: client
    }

    Connections {
        target: QmlAsServiceInterface
        function onPassStructMethodCalled(reply) {
            var obj = QmlStructFactory.create("Foo", 3.14, QmlEnum.ONE)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassStructSignal(obj)
            client.PassStructMethod(obj)
        }
        function onPassArrayInArrayMethodCalled(reply)
        {
            var obj = [[1,2],[3,4]]
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassArrayInArraySignal(obj)
            client.PassArrayInArrayMethod(obj)
        }
        function onPassStructsInArrayMethodCalled(reply) {
            var obj = [
                QmlStructFactory.create("Foo", 3.14, QmlEnum.TWO),
                QmlStructFactory.create("Bar", 1.26, QmlEnum.OWT)
            ]
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassStructsInArraySignal(obj)
            client.PassStructsInArrayMethod(obj)
        }
        function onPassDictWithStringsMethodCalled(reply) {
            var jsobj = {"A": "b", "C": "d"}
            var obj = Conversions.jsToMapOfStringToString(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictWithStringsSignal(obj)
            client.PassDictWithStringsMethod(obj)
        }
        function onPassDictWithNumbersMethodCalled(reply) {
            var jsobj = {1: "b", 2: "d"}
            var obj = Conversions.jsToMapOfUint32ToString(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictWithNumbersSignal(obj)
            client.PassDictWithNumbersMethod(obj)
        }
        function onPassDictWithStructsMethodCalled(reply) {
            var jsobj = {
                "A": QmlStructFactory.create("Foo", 1.0, QmlEnum.ONE),
                "B": QmlStructFactory.create("Bar", 2.0, QmlEnum.TWO)
            }
            var obj = Conversions.jsToMapOfStringToQmlStruct(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictWithStructsSignal(obj)
            client.PassDictWithStructsMethod(obj)
        }
        function onPassDictInArrayMethodCalled(reply) {
            var jsobj = [
                {"A": "b"},
                {"C": "d"}
            ]
            var obj = Conversions.jsToListOfMapOfStringToString(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictInArraySignal(obj)
            client.PassDictInArrayMethod(obj)
        }
        function onPassDictInDictMethodCalled(reply) {
            var jsobj = {
                "Ab": {"A": "b"},
                "Cd": {"C": "d"}
            }
            var obj = Conversions.jsToMapOfStringToMapOfStringToString(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictInDictSignal(obj)
            client.PassDictInDictMethod(obj)
        }
        function onPassArrayInDictMethodCalled(reply) {
            var jsobj = {
                "Ab": ["A", "b"],
                "Cd": ["C", "d"]
            }
            var obj = Conversions.jsToMapOfStringToListOfString(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassArrayInDictSignal(obj)
            client.PassArrayInDictMethod(obj)
        }
        function onPassDictInArrayInDictMethodCalled(reply) {
            var jsobj = {
                "Ab": [{"A": "b"}],
                "Cd": [{"C": "d"}]
            }
            var obj = Conversions.jsToMapOfStringToListOfMapOfStringToString(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictInArrayInDictSignal(obj)
            client.PassDictInArrayInDictMethod(obj)
        }
        function onPassDictInArrayInArrayMethodCalled(reply) {
            var jsobj = [
                [{"A": "b"}],
                [{"C": "d"}]
            ]
            var obj = Conversions.jsToListOfListOfMapOfStringToString(jsobj)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictInArrayInArraySignal(obj)
            client.PassDictInArrayInArrayMethod(obj)
        }
        function onPassDictWithEnumsMethodCalled(reply) {
            var jsob = {
                [QmlEnum.ONE]: QmlEnum.ENO,
                [QmlEnum.TWO]: QmlEnum.OWT
            }
            var obj = Conversions.jsToMapOfQmlEnumToQmlEnum(jsob)
            reply.sendReply(obj)
            QmlAsServiceInterface.EmitPassDictWithEnumsSignal(obj)
            client.PassDictWithEnumsMethod(obj)
        }
    }
}