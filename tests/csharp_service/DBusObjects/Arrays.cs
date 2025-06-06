namespace csharp_service.DBusObjects;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendArraysClientPayloads;
using ServicePayload = TestService.Generated.ArraysInterfacePayloads;

class Arrays
{
    public static async Task<(IClient[], ComYarpcTestserviceArrays)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var arraysClient = new BackendArraysClient();
        var objectPath = new ComYarpcTestserviceArrays();
        await connection.RegisterClient(arraysClient);
        await ArraysInterfaces.Arrays.Configure(arraysClient, objectPath, logger, stoppingToken);

        await connection.RegisterObjectPathAsync(objectPath);
        Console.WriteLine("Arrays interface configured");
        return ([arraysClient], objectPath);
    }
}