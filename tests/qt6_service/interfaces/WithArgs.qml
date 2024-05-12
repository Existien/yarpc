import QtQuick
import gen.with_args

Item {
    Component.onCompleted: {
        WithArgsInterface.connect()
    }
    Binding {
        target: WithArgsInterface
        property: 'speed'
        value: client.speed
    }
    Binding {
        target: WithArgsInterface
        property: 'distance'
        value: client.distance
    }
    Binding {
        target: WithArgsInterface
        property: 'duration'
        value: client.duration
    }

    BackendWithArgsClient {
        id: client
        onNotifiedReceived: function(msg) {
            WithArgsInterface.EmitNotified(msg)
        }
        onOrderReceivedReceived: function(item, amount, price) {
            WithArgsInterface.EmitOrderReceived(item, amount, price)
        }
    }

    Connections {
        target: WithArgsInterface
        function onNotifyCalled(reply) {
            var call = client.Notify(reply.args().message)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(e){reply.sendError(e)})
        }
        function onOrderCalled(reply) {
            var args = reply.args()
            var call = client.Order(
                args.item, args.amount, args.pricePerItem
            )
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(e){reply.sendError(r)})
        }
        function onPropertyDistanceSet(value) {
            client.distance = value
        }
        function onPropertySpeedSet(value) {
            client.speed = value
        }
    }

}
