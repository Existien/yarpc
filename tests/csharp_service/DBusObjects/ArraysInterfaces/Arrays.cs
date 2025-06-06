namespace csharp_service.DBusObjects.ArraysInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendArraysClientPayloads;
using ServicePayload = TestService.Generated.ArraysInterfacePayloads;

class Arrays
{
    public static async Task Configure(BackendArraysClient client, ComYarpcTestserviceArrays objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.ArraysInterface.OnArrayMethod = async (UInt32[][] numbers) => {
            return await client.ArrayMethodAsync(numbers);
        };
        client.ArraySignal += (ClientPayload.ArraySignal payload) => {
            objectPath.ArraysInterface.EmitArraySignal(new ServicePayload.ArraySignal(payload.numbers));
        };

        objectPath.ArraysInterface.SetArrayProperty = async (string[][] newValue, ArraysInterfaceProperties oldProps) => {
            await client.SetArrayPropertyAsync(newValue);
            oldProps.ArrayProperty = await client.GetArrayPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.ArraysInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "ArrayProperty":
                        props.ArrayProperty = (string[][])entry.Value;
                        break;
                }
            }
            objectPath.ArraysInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.ArraysInterface.Properties = new ArraysInterfaceProperties()
                {
                    ArrayProperty = clientProps.ArrayProperty,
                };
                arePropertiesSet=true;
            }
            catch (Exception e)
            {
                await Task.Delay(1000, stoppingToken);
                logger.LogWarning($"{e.Message}");
            }
        }
    }
}