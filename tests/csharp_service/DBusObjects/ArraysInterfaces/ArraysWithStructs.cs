namespace csharp_service.DBusObjects.ArraysInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendArraysWithStructsClientPayloads;
using ServicePayload = TestService.Generated.ArraysWithStructsInterfacePayloads;

class ArraysWithStructs
{
    public static async Task Configure(BackendArraysWithStructsClient client, ComYarpcTestserviceArrays objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.ArraysWithStructsInterface.OnArrayStructMethod = async (StructArray[] numbers) => {
            return await client.ArrayStructMethodAsync(numbers);
        };
        client.ArrayStructSignal += (ClientPayload.ArrayStructSignal payload) => {
            objectPath.ArraysWithStructsInterface.EmitArrayStructSignal(new ServicePayload.ArrayStructSignal(payload.numbers));
        };

        objectPath.ArraysWithStructsInterface.SetArrayStructProperty = async (StructArray[] newValue, ArraysWithStructsInterfaceProperties oldProps) => {
            await client.SetArrayStructPropertyAsync(newValue);
            oldProps.ArrayStructProperty = await client.GetArrayStructPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.ArraysWithStructsInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "ArrayStructProperty":
                        props.ArrayStructProperty = (StructArray[])entry.Value;
                        break;
                }
            }
            objectPath.ArraysWithStructsInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.ArraysWithStructsInterface.Properties = new ArraysWithStructsInterfaceProperties()
                {
                    ArrayStructProperty = clientProps.ArrayStructProperty,
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