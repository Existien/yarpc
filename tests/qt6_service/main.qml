import QtQuick
import QtQuick.Controls
import gen.minimal

Window {
    height: 300
    width: 600
    visible: false

    BackendMinimalClient {
        id: minimalClient
        onBumpedReceived: {
            iface.EmitBumped()
        }
    }

    MinimalInterface {
        id: iface
        Component.onCompleted: connect()

        onBumpCalled: function (reply) {
            var call = minimalClient.Bump()
            call.finished.connect(function(){reply.sendReply()})
            call.error.connect(function(e){reply.sendError(e)})
        }
    }
}
