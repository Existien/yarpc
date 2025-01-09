import QtQuick
import gen.enums

Item {
    Component.onCompleted: {
        EnumsWithArraysInterface.connect()
    }
    Binding {
        target: EnumsWithArraysInterface
        property: 'enumProperty'
        value: client.enumProperty
    }

    BackendEnumsWithArraysClient {
        id: client
        onEnumSignalReceived: function(color) {
            EnumsWithArraysInterface.EmitEnumSignal(color)
        }
    }

    Connections {
        target: EnumsWithArraysInterface
        function onEnumMethodCalled(reply) {
            var call = client.EnumMethod(reply.args().color)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(e){reply.sendError(e)})
        }
        function onPropertyEnumPropertySet(value) {
            client.enumProperty = value
        }
    }
}