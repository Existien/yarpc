import QtQuick
import gen.enums

Item {
    Component.onCompleted: {
        EnumsWithStructsInterface.connect()
    }
    Binding {
        target: EnumsWithStructsInterface
        property: 'enumProperty'
        value: client.enumProperty
    }

    BackendEnumsWithStructsClient {
        id: client
        onEnumSignalReceived: function(color) {
            EnumsWithStructsInterface.EmitEnumSignal(color)
        }
    }

    Connections {
        target: EnumsWithStructsInterface
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