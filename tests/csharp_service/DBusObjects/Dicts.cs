namespace csharp_service.DBusObjects;
using TestService.Generated;

class Dicts
{
    public static async Task<(IClient[], ComYarpcTestserviceDicts)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var dictsClient = new BackendDictsClient();
        await connection.RegisterClient(dictsClient);
        var objectPath = new ComYarpcTestserviceDicts();
        await DictsInterfaces.Dicts.Configure(dictsClient, objectPath, logger, stoppingToken);

        await connection.RegisterObjectPathAsync(objectPath);
        Console.WriteLine("Dicts interface configured");
        return ([dictsClient], objectPath);
    }
}