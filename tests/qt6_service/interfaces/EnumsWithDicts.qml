import QtQuick
import gen.enums

Item {
    Component.onCompleted: {
        EnumsWithDictsInterface.connect()
    }
    Binding {
        target: EnumsWithDictsInterface
        property: 'enumProperty'
        value: client.enumProperty
    }

    BackendEnumsWithDictsClient {
        id: client
        onEnumSignalReceived: function(color) {
            EnumsWithDictsInterface.EmitEnumSignal(color)
        }
    }

    Connections {
        target: EnumsWithDictsInterface
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