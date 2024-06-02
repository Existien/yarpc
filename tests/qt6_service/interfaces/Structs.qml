import QtQuick
import gen.structs

Item {
    Component.onCompleted: {
        StructsInterface.connect()
    }
    Binding {
        target: StructsInterface
        property: 'simple'
        value: client.simple
    }

    BackendStructsClient {
        id: client
        onStructReceivedReceived: function(simpleStruct, totalCosts) {
            StructsInterface.EmitStructReceived(simpleStruct, totalCosts)
        }
    }

    Connections {
        target: StructsInterface
        function onSendStructCalled(reply) {
            var call = client.SendStruct(reply.args().simpleStruct)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(e){reply.sendError(e)})
        }
        function onPropertySimpleSet(value) {
            client.simple = value
        }
    }
}