import QtQuick
import gen.enums

Item {
    Component.onCompleted: {
        EnumsInterface.connect()
    }
    Binding {
        target: EnumsInterface
        property: 'enumProperty'
        value: client.enumProperty
    }

    BackendEnumsClient {
        id: client
        onEnumSignalReceived: function(color) {
            EnumsInterface.EmitEnumSignal(color)
        }
    }

    Connections {
        target: EnumsInterface
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