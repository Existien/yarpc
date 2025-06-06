namespace csharp_service.DBusObjects;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendStructsClientPayloads;
using ServicePayload = TestService.Generated.StructsInterfacePayloads;

// 'com.yarpc.testservice.structs', 'Simple', GLib.Variant('((sd)u)', (('A',2.2),52))
class Structs
{
    public static async Task<(BackendStructsClient, ComYarpcTestserviceStructs)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var client = new BackendStructsClient();
        var objectPath = new ComYarpcTestserviceStructs();
        objectPath.StructsInterface.OnSendStruct = async (SimpleStruct simpleStruct)=>{
            return await client.SendStructAsync(simpleStruct);
        };
        client.StructReceived += (ClientPayload.StructReceived payload) => {
            objectPath.StructsInterface.EmitStructReceived(new ServicePayload.StructReceived(
                payload.simpleStruct, payload.totalCosts
            ));
        };

        objectPath.StructsInterface.SetSimple = async (SimpleStruct newValue, StructsInterfaceProperties oldProps) => {
            await client.SetSimpleAsync(newValue);
            oldProps.Simple = await client.GetSimpleAsync();
            return oldProps;
        };
        await connection.RegisterClient(client);

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.StructsInterface.Properties = new StructsInterfaceProperties()
                {
                    Simple = clientProps.Simple,
                };
                arePropertiesSet=true;
            }
            catch (Exception e)
            {
                await Task.Delay(1000, stoppingToken);
                logger.LogWarning($"{e.Message}");
            }
        }

        await connection.RegisterObjectPathAsync(objectPath);
        Console.WriteLine("Structs interface configured");
        return (client, objectPath);
    }
}