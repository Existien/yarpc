namespace csharp_service.DBusObjects;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendArraysClientPayloads;
using ServicePayload = TestService.Generated.ArraysInterfacePayloads;

class Arrays
{
    public static async Task<(IClient[], ComYarpcTestserviceArrays)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var arraysClient = new BackendArraysClient();
        await connection.RegisterClient(arraysClient);
        var arraysWithStructsClient = new BackendArraysWithStructsClient();
        await connection.RegisterClient(arraysWithStructsClient);
        var objectPath = new ComYarpcTestserviceArrays();
        await ArraysInterfaces.Arrays.Configure(arraysClient, objectPath, logger, stoppingToken);
        await ArraysInterfaces.ArraysWithStructs.Configure(arraysWithStructsClient, objectPath, logger, stoppingToken);

        await connection.RegisterObjectPathAsync(objectPath);
        Console.WriteLine("Arrays interface configured");
        return ([arraysClient, arraysWithStructsClient], objectPath);
    }
}