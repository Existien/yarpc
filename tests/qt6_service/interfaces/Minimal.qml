import QtQuick
import gen.minimal

Item {
    Component.onCompleted: {
        MinimalInterface.connect()
    }

    BackendMinimalClient {
        id: client
        onBumpedReceived: {
            MinimalInterface.EmitBumped()
        }
    }

    Connections {
        target: MinimalInterface
        function onBumpCalled(reply) {
            var call = client.Bump()
            call.finished.connect(function(){reply.sendReply()})
            call.error.connect(function(e){reply.sendError(e)})
        }
    }
}