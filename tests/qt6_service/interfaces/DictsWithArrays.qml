import QtQuick
import gen.dicts

Item {
    Component.onCompleted: {
        DictsWithArraysInterface.connect()
    }
    Binding {
        target: DictsWithArraysInterface
        property: 'dictArrayProperty'
        value: client.dictArrayProperty
    }

    BackendDictsWithArraysClient {
        id: client
        onDictsArraySignalReceived: function(numbers) {
            DictsWithArraysInterface.EmitDictsArraySignal(numbers)
        }
    }

    Connections {
        target: DictsWithArraysInterface
        function onDictsArrayMethodCalled(reply) {
            var call = client.DictsArrayMethod(reply.args().numbers)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onPropertyDictArrayPropertySet(value) {
            client.dictArrayProperty = value
        }
    }
}