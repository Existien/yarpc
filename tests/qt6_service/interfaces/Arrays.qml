import QtQuick
import gen.arrays

Item {
    Component.onCompleted: {
        ArraysInterface.connect()
    }
    Binding {
        target: ArraysInterface
        property: 'arrayProperty'
        value: client.arrayProperty
    }

    BackendArraysClient {
        id: client
        onArraySignalReceived: function(numbers) {
            ArraysInterface.EmitArraySignal(numbers)
        }
    }

    Connections {
        target: ArraysInterface
        function onArrayMethodCalled(reply) {
            console.log(reply.args().numbers)
            var call = client.ArrayMethod(reply.args().numbers)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(e){reply.sendError(e)})
        }
        function onPropertyArrayPropertySet(value) {
            client.arrayProperty = value
        }
    }
}