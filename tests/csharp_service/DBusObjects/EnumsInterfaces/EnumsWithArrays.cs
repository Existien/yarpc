namespace csharp_service.DBusObjects.EnumsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendEnumsWithArraysClientPayloads;
using ServicePayload = TestService.Generated.EnumsWithArraysInterfacePayloads;

class EnumsWithArrays
{
    public static async Task Configure(BackendEnumsWithArraysClient client, ComYarpcTestserviceEnums objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.EnumsWithArraysInterface.OnEnumMethod = async (Color[] color) => {
            return await client.EnumMethodAsync(color);
        };
        client.EnumSignal += (ClientPayload.EnumSignal payload) => {
            objectPath.EnumsWithArraysInterface.EmitEnumSignal(new ServicePayload.EnumSignal(payload.color));
        };
        objectPath.EnumsWithArraysInterface.SetEnumProperty = async (Color[] newValue, EnumsWithArraysInterfaceProperties oldProps) => {
            await client.SetEnumPropertyAsync(newValue);
            oldProps.EnumProperty = await client.GetEnumPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.EnumsWithArraysInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "EnumProperty":
                        props.EnumProperty = (Color[]) entry.Value;
                        break;
                }
            }
            objectPath.EnumsWithArraysInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.EnumsWithArraysInterface.Properties = new EnumsWithArraysInterfaceProperties()
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