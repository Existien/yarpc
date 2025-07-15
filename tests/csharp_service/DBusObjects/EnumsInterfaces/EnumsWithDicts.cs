namespace csharp_service.DBusObjects.EnumsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendEnumsWithDictsClientPayloads;
using ServicePayload = TestService.Generated.EnumsWithDictsInterfacePayloads;

class EnumsWithDicts
{
    public static async Task Configure(BackendEnumsWithDictsClient client, ComYarpcTestserviceEnums objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.EnumsWithDictsInterface.OnEnumMethod = async (KeyValuePair<Color, Color>[] color) => {
            return await client.EnumMethodAsync(color);
        };
        client.EnumSignal += (ClientPayload.EnumSignal payload) => {
            objectPath.EnumsWithDictsInterface.EmitEnumSignal(new ServicePayload.EnumSignal(payload.color));
        };
        objectPath.EnumsWithDictsInterface.SetEnumProperty = async (KeyValuePair<Color, Color>[] newValue, EnumsWithDictsInterfaceProperties oldProps) => {
            await client.SetEnumPropertyAsync(newValue);
            oldProps.EnumProperty = await client.GetEnumPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.EnumsWithDictsInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "EnumProperty":
                        props.EnumProperty = (KeyValuePair<Color, Color>[]) entry.Value;
                        break;
                }
            }
            objectPath.EnumsWithDictsInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.EnumsWithDictsInterface.Properties = new EnumsWithDictsInterfaceProperties()
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