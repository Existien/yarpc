namespace csharp_service.DBusObjects;
using TestService.Generated;

class Enums
{
    public static async Task<(IClient[], ComYarpcTestserviceEnums)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var enumsClient = new BackendEnumsClient();
        await connection.RegisterClient(enumsClient);
        var enumsWithArraysClient = new BackendEnumsWithArraysClient();
        await connection.RegisterClient(enumsWithArraysClient);
        var enumsWithDictsClient = new BackendEnumsWithDictsClient();
        await connection.RegisterClient(enumsWithDictsClient);
        var objectPath = new ComYarpcTestserviceEnums();
        await EnumsInterfaces.Enums.Configure(enumsClient, objectPath, logger, stoppingToken);
        await EnumsInterfaces.EnumsWithArrays.Configure(enumsWithArraysClient, objectPath, logger, stoppingToken);
        await EnumsInterfaces.EnumsWithDicts.Configure(enumsWithDictsClient, objectPath, logger, stoppingToken);

        await connection.RegisterObjectPathAsync(objectPath);
        Console.WriteLine("Enums interface configured");
        return ([enumsClient, enumsWithArraysClient], objectPath);
    }
}