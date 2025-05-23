namespace csharp_service.DBusObjects.WithArgsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendPrimitivesClientPayloads;
using ServicePayload = TestService.Generated.PrimitivesInterfacePayloads;

class Primitives
{
    public static void Configure(BackendPrimitivesClient client, ComYarpcTestserviceWithArgs objectPath)
    {
        objectPath.PrimitivesInterface.OnUint8Method = async (byte value) => {
            return await client.Uint8MethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnBoolMethod = async (bool value) => {
            return await client.BoolMethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnInt16Method = async (Int16 value) => {
            return await client.Int16MethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnUint16Method = async (UInt16 value) => {
            return await client.Uint16MethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnInt32Method = async (Int32 value) => {
            return await client.Int32MethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnUint32Method = async (UInt32 value) => {
            return await client.Uint32MethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnInt64Method = async (Int64 value) => {
            return await client.Int64MethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnUint64Method = async (UInt64 value) => {
            return await client.Uint64MethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnDoubleMethod = async (double value) => {
            return await client.DoubleMethodAsync(value);
        };
        objectPath.PrimitivesInterface.OnStringMethod = async (string value) => {
            return await client.StringMethodAsync(value);
        };

        client.Uint8Signal += (ClientPayload.Uint8Signal payload) => {
            objectPath.PrimitivesInterface.EmitUint8Signal(new ServicePayload.Uint8Signal(payload.value));
        };
        client.BoolSignal += (ClientPayload.BoolSignal payload) => {
            objectPath.PrimitivesInterface.EmitBoolSignal(new ServicePayload.BoolSignal(payload.value));
        };
        client.Int16Signal += (ClientPayload.Int16Signal payload) => {
            objectPath.PrimitivesInterface.EmitInt16Signal(new ServicePayload.Int16Signal(payload.value));
        };
        client.Uint16Signal += (ClientPayload.Uint16Signal payload) => {
            objectPath.PrimitivesInterface.EmitUint16Signal(new ServicePayload.Uint16Signal(payload.value));
        };
        client.Int32Signal += (ClientPayload.Int32Signal payload) => {
            objectPath.PrimitivesInterface.EmitInt32Signal(new ServicePayload.Int32Signal(payload.value));
        };
        client.Uint32Signal += (ClientPayload.Uint32Signal payload) => {
            objectPath.PrimitivesInterface.EmitUint32Signal(new ServicePayload.Uint32Signal(payload.value));
        };
        client.Int64Signal += (ClientPayload.Int64Signal payload) => {
            objectPath.PrimitivesInterface.EmitInt64Signal(new ServicePayload.Int64Signal(payload.value));
        };
        client.Uint64Signal += (ClientPayload.Uint64Signal payload) => {
            objectPath.PrimitivesInterface.EmitUint64Signal(new ServicePayload.Uint64Signal(payload.value));
        };
        client.DoubleSignal += (ClientPayload.DoubleSignal payload) => {
            objectPath.PrimitivesInterface.EmitDoubleSignal(new ServicePayload.DoubleSignal(payload.value));
        };
        client.StringSignal += (ClientPayload.StringSignal payload) => {
            objectPath.PrimitivesInterface.EmitStringSignal(new ServicePayload.StringSignal(payload.value));
        };
    }
}