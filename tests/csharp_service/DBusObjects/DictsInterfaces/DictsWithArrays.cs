namespace csharp_service.DBusObjects.DictsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendDictsWithArraysClientPayloads;
using ServicePayload = TestService.Generated.DictsWithArraysInterfacePayloads;

class DictsWithArrays
{
    public static async Task Configure(BackendDictsWithArraysClient client, ComYarpcTestserviceDicts objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.DictsWithArraysInterface.OnDictsArrayMethod = async (KeyValuePair<string, KeyValuePair<string, UInt32>[][]>[] numbers) => {
            return await client.DictsArrayMethodAsync(numbers);
        };
        client.DictsArraySignal += (ClientPayload.DictsArraySignal payload) => {
            objectPath.DictsWithArraysInterface.EmitDictsArraySignal(new ServicePayload.DictsArraySignal(payload.numbers));
        };

        objectPath.DictsWithArraysInterface.SetDictArrayProperty = async (KeyValuePair<string, KeyValuePair<string, UInt32>[][]>[] newValue, DictsWithArraysInterfaceProperties oldProps) => {
            await client.SetDictArrayPropertyAsync(newValue);
            oldProps.DictArrayProperty = await client.GetDictArrayPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.DictsWithArraysInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "DictArrayProperty":
                        props.DictArrayProperty = (KeyValuePair<string, KeyValuePair<string, UInt32>[][]>[]) entry.Value;
                        break;
                }
            }
            objectPath.DictsWithArraysInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.DictsWithArraysInterface.Properties = new DictsWithArraysInterfaceProperties()
                {
                    DictArrayProperty = clientProps.DictArrayProperty,
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