namespace csharp_service.DBusObjects.DictsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendDictsWithStructsClientPayloads;
using ServicePayload = TestService.Generated.DictsWithStructsInterfacePayloads;

class DictsWithStructs
{
    public static async Task Configure(BackendDictsWithStructsClient client, ComYarpcTestserviceDicts objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.DictsWithStructsInterface.OnDictsStructMethod = async (KeyValuePair<string, StructDict>[] numbers) => {
            return await client.DictsStructMethodAsync(numbers);
        };
        client.DictStructSignal += (ClientPayload.DictStructSignal payload) => {
            objectPath.DictsWithStructsInterface.EmitDictStructSignal(new ServicePayload.DictStructSignal(payload.numbers));
        };

        objectPath.DictsWithStructsInterface.SetDictStructProperty = async (KeyValuePair<string, StructDict>[] newValue, DictsWithStructsInterfaceProperties oldProps) => {
            await client.SetDictStructPropertyAsync(newValue);
            oldProps.DictStructProperty = await client.GetDictStructPropertyAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.DictsWithStructsInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "DictStructProperty":
                        props.DictStructProperty = (KeyValuePair<string, StructDict>[]) entry.Value;
                        break;
                }
            }
            objectPath.DictsWithStructsInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.DictsWithStructsInterface.Properties = new DictsWithStructsInterfaceProperties()
                {
                    DictStructProperty = clientProps.DictStructProperty,
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