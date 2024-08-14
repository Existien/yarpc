import QtQuick
import gen.arrays

Item {
    Component.onCompleted: {
        ArraysWithStructsInterface.connect()
    }
    Binding {
        target: ArraysWithStructsInterface
        property: 'arrayStructProperty'
        value: client.arrayStructProperty
    }

    BackendArraysWithStructsClient {
        id: client
        onArrayStructSignalReceived: function(numbers) {
            ArraysWithStructsInterface.EmitArrayStructSignal(numbers)
        }
    }

    Connections {
        target: ArraysWithStructsInterface
        function onArrayStructMethodCalled(reply) {
            console.log(reply.args().numbers)
            var call = client.ArrayStructMethod(reply.args().numbers)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(e){reply.sendError(e)})
        }
        function onPropertyArrayStructPropertySet(value) {
            client.arrayStructProperty = value
        }
    }
}