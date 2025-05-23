namespace csharp_service.DBusObjects;
using TestService.Generated;

class Minimal
{
    public static async Task<(BackendMinimalClient, ComYarpcTestserviceMinimal)> Configure(Connection connection)
    {
        var client = new BackendMinimalClient();
        var objectPath = new ComYarpcTestserviceMinimal();
        objectPath.MinimalInterface.OnBump = async ()=>{
            await client.BumpAsync();
        };
        client.Bumped += ()=>{objectPath.MinimalInterface.EmitBumped();};
        await connection.RegisterClient(client);
        await connection.RegisterObjectPathAsync(objectPath);
        return (client, objectPath);
    }
}