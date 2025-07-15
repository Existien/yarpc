namespace csharp_service.DBusObjects.EnumsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendEnumsClientPayloads;
using ServicePayload = TestService.Generated.EnumsInterfacePayloads;

class Enums
{
    public static async Task Configure(BackendEnumsClient client, ComYarpcTestserviceEnums objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.EnumsInterface.OnEnumMethod = async (Color color) => {
            return await client.EnumMethodAsync(color);
        };
        client.EnumSignal += (ClientPayload.EnumSignal payload) => {
            objectPath.EnumsInterface.EmitEnumSignal(new ServicePayload.EnumSignal(payload.color));
        };
        objectPath.EnumsInterface.SetEnumProperty = async (Color newValue, EnumsInterfaceProperties oldProps) => {
            await client.SetEnumPropertyAsync(newValue);
            oldProps.EnumProperty = await client.GetEnumPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.EnumsInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "EnumProperty":
                        props.EnumProperty = (Color) entry.Value;
                        break;
                }
            }
            objectPath.EnumsInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.EnumsInterface.Properties = new EnumsInterfaceProperties()
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