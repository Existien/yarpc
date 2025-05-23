namespace csharp_service.Services;
using TGM = TestService.Generated.Minimal;

class Minimal
{
    public static async Task<(TGM.BackendMinimalClient, TGM.MinimalInterface)> Configure(Connection connection)
    {
        var client = new TGM.BackendMinimalClient();
        var service = new TGM.MinimalInterface();
        service.OnBump = async ()=>{
            await client.BumpAsync();
        };
        client.Bumped += ()=>{service.EmitBumped();};
        await connection.RegisterClient(client);
        await connection.RegisterInterfaceAsync(service);
        return (client, service);
    }
}