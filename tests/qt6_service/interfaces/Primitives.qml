import QtQuick
import gen.with_args

Item {
    Component.onCompleted: {
        PrimitivesInterface.connect()
    }

    BackendPrimitivesClient {
        id: client

        onUint8SignalReceived: function(value) { PrimitivesInterface.EmitUint8Signal(value)}
        onBoolSignalReceived: function(value) { PrimitivesInterface.EmitBoolSignal(value)}
        onInt16SignalReceived: function(value) { PrimitivesInterface.EmitInt16Signal(value)}
        onUint16SignalReceived: function(value) { PrimitivesInterface.EmitUint16Signal(value)}
        onInt32SignalReceived: function(value) { PrimitivesInterface.EmitInt32Signal(value)}
        onUint32SignalReceived: function(value) { PrimitivesInterface.EmitUint32Signal(value)}
        onInt64SignalReceived: function(value) { PrimitivesInterface.EmitInt64Signal(value)}
        onUint64SignalReceived: function(value) { PrimitivesInterface.EmitUint64Signal(value)}
        onDoubleSignalReceived: function(value) { PrimitivesInterface.EmitDoubleSignal(value)}
        onStringSignalReceived: function(value) { PrimitivesInterface.EmitStringSignal(value)}
    }

    Connections {
        target: PrimitivesInterface
        function onUint8MethodCalled(reply) {client.Uint8Method(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onBoolMethodCalled(reply) {client.BoolMethod(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onInt16MethodCalled(reply) {client.Int16Method(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onUint16MethodCalled(reply) {client.Uint16Method(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onInt32MethodCalled(reply) {client.Int32Method(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onUint32MethodCalled(reply) {client.Uint32Method(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onInt64MethodCalled(reply) {client.Int64Method(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onUint64MethodCalled(reply) {client.Uint64Method(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onDoubleMethodCalled(reply) {client.DoubleMethod(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
        function onStringMethodCalled(reply) {client.StringMethod(reply.args().value).finished.connect(function(r){reply.sendReply(r)})}
    }

}
