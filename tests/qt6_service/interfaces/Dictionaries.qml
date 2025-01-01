import QtQuick
import gen.dicts

Item {
    Component.onCompleted: {
        DictsInterface.connect()
    }
    Binding {
        target: DictsInterface
        property: 'dictProperty'
        value: client.dictProperty
    }

    BackendDictsClient {
        id: client
        onDictSignalReceived: function(keysNValues) {
            DictsInterface.EmitDictSignal(keysNValues)
        }
    }

    Connections {
        target: DictsInterface
        function onDictMethodCalled(reply) {
            var call = client.DictMethod(reply.args().keysNValues)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onPropertyDictPropertySet(value) {
            client.dictProperty = value
        }
    }
}