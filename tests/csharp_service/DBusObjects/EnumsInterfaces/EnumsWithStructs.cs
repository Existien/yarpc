namespace csharp_service.DBusObjects.EnumsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendEnumsWithStructsClientPayloads;
using ServicePayload = TestService.Generated.EnumsWithStructsInterfacePayloads;

class EnumsWithStructs
{
    public static async Task Configure(BackendEnumsWithStructsClient client, ComYarpcTestserviceEnums objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.EnumsWithStructsInterface.OnEnumMethod = async (EnumStruct color) => {
            return await client.EnumMethodAsync(color);
        };
        client.EnumSignal += (ClientPayload.EnumSignal payload) => {
            objectPath.EnumsWithStructsInterface.EmitEnumSignal(new ServicePayload.EnumSignal(payload.color));
        };
        objectPath.EnumsWithStructsInterface.SetEnumProperty = async (EnumStruct newValue, EnumsWithStructsInterfaceProperties oldProps) => {
            await client.SetEnumPropertyAsync(newValue);
            oldProps.EnumProperty = await client.GetEnumPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.EnumsWithStructsInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "EnumProperty":
                        props.EnumProperty = (EnumStruct) entry.Value;
                        break;
                }
            }
            objectPath.EnumsWithStructsInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.EnumsWithStructsInterface.Properties = new EnumsWithStructsInterfaceProperties()
                {
                    EnumProperty = clientProps.EnumProperty,
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