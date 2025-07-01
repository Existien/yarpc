namespace csharp_service.DBusObjects.DictsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendDictsClientPayloads;
using ServicePayload = TestService.Generated.DictsInterfacePayloads;

class Dicts
{
    public static async Task Configure(BackendDictsClient client, ComYarpcTestserviceDicts objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.DictsInterface.OnDictMethod = async (KeyValuePair<string, UInt32>[] keysNValues) => {
            return await client.DictMethodAsync(keysNValues);
        };
        client.DictSignal += (ClientPayload.DictSignal payload) => {
            objectPath.DictsInterface.EmitDictSignal(new ServicePayload.DictSignal(payload.keysNValues));
        };

        objectPath.DictsInterface.SetDictProperty = async (KeyValuePair<string, UInt32>[] newValue, DictsInterfaceProperties oldProps) => {
            await client.SetDictPropertyAsync(newValue);
            oldProps.DictProperty = await client.GetDictPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.DictsInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "DictProperty":
                        props.DictProperty = (KeyValuePair<string, UInt32>[]) entry.Value;
                        break;
                }
            }
            objectPath.DictsInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.DictsInterface.Properties = new DictsInterfaceProperties()
                {
                    DictProperty = clientProps.DictProperty,
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