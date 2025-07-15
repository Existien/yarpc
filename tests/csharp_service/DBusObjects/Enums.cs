namespace csharp_service.DBusObjects;
using TestService.Generated;

class Enums
{
    public static async Task<(IClient[], ComYarpcTestserviceEnums)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var enumsClient = new BackendEnumsClient();
        await connection.RegisterClient(enumsClient);
        var objectPath = new ComYarpcTestserviceEnums();
        await EnumsInterfaces.Enums.Configure(enumsClient, objectPath, logger, stoppingToken);

        await connection.RegisterObjectPathAsync(objectPath);
        Console.WriteLine("Enums interface configured");
        return ([enumsClient], objectPath);
    }
}