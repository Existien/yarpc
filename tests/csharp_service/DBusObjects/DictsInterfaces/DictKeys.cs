namespace csharp_service.DBusObjects.DictsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendDictKeysClientPayloads;
using ServicePayload = TestService.Generated.DictKeysInterfacePayloads;

class DictKeys
{
    public static async Task Configure(BackendDictKeysClient client, ComYarpcTestserviceDicts objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.DictKeysInterface.OnUint8Method = async (KeyValuePair<byte, string>[] value) => {
            return await client.Uint8MethodAsync(value);
        };
        objectPath.DictKeysInterface.OnBoolMethod = async (KeyValuePair<bool, string>[] value) => {
            return await client.BoolMethodAsync(value);
        };
        objectPath.DictKeysInterface.OnInt16Method = async (KeyValuePair<Int16, string>[] value) => {
            return await client.Int16MethodAsync(value);
        };
        objectPath.DictKeysInterface.OnUint16Method = async (KeyValuePair<UInt16, string>[] value) => {
            return await client.Uint16MethodAsync(value);
        };
        objectPath.DictKeysInterface.OnInt32Method = async (KeyValuePair<Int32, string>[] value) => {
            return await client.Int32MethodAsync(value);
        };
        objectPath.DictKeysInterface.OnUint32Method = async (KeyValuePair<UInt32, string>[] value) => {
            return await client.Uint32MethodAsync(value);
        };
        objectPath.DictKeysInterface.OnInt64Method = async (KeyValuePair<Int64, string>[] value) => {
            return await client.Int64MethodAsync(value);
        };
        objectPath.DictKeysInterface.OnUint64Method = async (KeyValuePair<UInt64, string>[] value) => {
            return await client.Uint64MethodAsync(value);
        };
        objectPath.DictKeysInterface.OnDoubleMethod = async (KeyValuePair<double, string>[] value) => {
            return await client.DoubleMethodAsync(value);
        };
        objectPath.DictKeysInterface.OnStringMethod = async (KeyValuePair<string, string>[] value) => {
            return await client.StringMethodAsync(value);
        };

        client.Uint8Signal += (ClientPayload.Uint8Signal payload) => {
            objectPath.DictKeysInterface.EmitUint8Signal(new ServicePayload.Uint8Signal(payload.value));
        };
        client.BoolSignal += (ClientPayload.BoolSignal payload) => {
            objectPath.DictKeysInterface.EmitBoolSignal(new ServicePayload.BoolSignal(payload.value));
        };
        client.Int16Signal += (ClientPayload.Int16Signal payload) => {
            objectPath.DictKeysInterface.EmitInt16Signal(new ServicePayload.Int16Signal(payload.value));
        };
        client.Uint16Signal += (ClientPayload.Uint16Signal payload) => {
            objectPath.DictKeysInterface.EmitUint16Signal(new ServicePayload.Uint16Signal(payload.value));
        };
        client.Int32Signal += (ClientPayload.Int32Signal payload) => {
            objectPath.DictKeysInterface.EmitInt32Signal(new ServicePayload.Int32Signal(payload.value));
        };
        client.Uint32Signal += (ClientPayload.Uint32Signal payload) => {
            objectPath.DictKeysInterface.EmitUint32Signal(new ServicePayload.Uint32Signal(payload.value));
        };
        client.Int64Signal += (ClientPayload.Int64Signal payload) => {
            objectPath.DictKeysInterface.EmitInt64Signal(new ServicePayload.Int64Signal(payload.value));
        };
        client.Uint64Signal += (ClientPayload.Uint64Signal payload) => {
            objectPath.DictKeysInterface.EmitUint64Signal(new ServicePayload.Uint64Signal(payload.value));
        };
        client.DoubleSignal += (ClientPayload.DoubleSignal payload) => {
            objectPath.DictKeysInterface.EmitDoubleSignal(new ServicePayload.DoubleSignal(payload.value));
        };
        client.StringSignal += (ClientPayload.StringSignal payload) => {
            objectPath.DictKeysInterface.EmitStringSignal(new ServicePayload.StringSignal(payload.value));
        };
    }
}