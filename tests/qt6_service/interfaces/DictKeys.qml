import QtQuick
import gen.dicts

Item {
    Component.onCompleted: {
        DictKeysInterface.connect()
    }
    // Binding {
    //     target: DictKeysInterface
    //     property: 'dictProperty'
    //     value: client.dictProperty
    // }

    BackendDictKeysClient {
        id: client
        onUint8SignalReceived: function(value) {
            DictKeysInterface.EmitUint8Signal(value)
        }
        onBoolSignalReceived: function(value) {
            DictKeysInterface.EmitBoolSignal(value)
        }
        onInt16SignalReceived: function(value) {
            DictKeysInterface.EmitInt16Signal(value)
        }
        onUint16SignalReceived: function(value) {
            DictKeysInterface.EmitUint16Signal(value)
        }
        onInt32SignalReceived: function(value) {
            DictKeysInterface.EmitInt32Signal(value)
        }
        onUint32SignalReceived: function(value) {
            DictKeysInterface.EmitUint32Signal(value)
        }
        onInt64SignalReceived: function(value) {
            DictKeysInterface.EmitInt64Signal(value)
        }
        onUint64SignalReceived: function(value) {
            DictKeysInterface.EmitUint64Signal(value)
        }
        onDoubleSignalReceived: function(value) {
            DictKeysInterface.EmitDoubleSignal(value)
        }
        onStringSignalReceived: function(value) {
            DictKeysInterface.EmitStringSignal(value)
        }
    }

    Connections {
        target: DictKeysInterface
        function onUint8MethodCalled(reply) {
            var call = client.Uint8Method(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onBoolMethodCalled(reply) {
            var call = client.BoolMethod(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onInt16MethodCalled(reply) {
            var call = client.Int16Method(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onUint16MethodCalled(reply) {
            var call = client.Uint16Method(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onInt32MethodCalled(reply) {
            var call = client.Int32Method(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onUint32MethodCalled(reply) {
            var call = client.Uint32Method(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onInt64MethodCalled(reply) {
            var call = client.Int64Method(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onUint64MethodCalled(reply) {
            var call = client.Uint64Method(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onDoubleMethodCalled(reply) {
            var call = client.DoubleMethod(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
        function onStringMethodCalled(reply) {
            var call = client.StringMethod(reply.args().value)
            call.finished.connect(function(r){reply.sendReply(r)})
            call.error.connect(function(r){reply.sendError(e)})
        }
    }
}