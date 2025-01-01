import QtQuick
import gen.dicts

Item {
    Component.onCompleted: {
        DictsWithStructsInterface.connect()
    }
    Binding {
        target: DictsWithStructsInterface
        property: 'dictStructProperty'
        value: client.dictStructProperty
    }

    BackendDictsWithStructsClient {
        id: client
        onDictStructSignalReceived: function(numbers) {
            DictsWithStructsInterface.EmitDictStructSignal(numbers)
        }
    }

    Connections {
        target: DictsWithStructsInterface
        function onDictsStructMethodCalled(reply) {
            var call = client.DictsStructMethod(reply.args().numbers)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onPropertyDictStructPropertySet(value) {
            client.dictStructProperty = value
        }
    }
}