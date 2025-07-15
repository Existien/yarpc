namespace csharp_service.DBusObjects;
using TestService.Generated;

class Dicts
{
    public static async Task<(IClient[], ComYarpcTestserviceDicts)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var dictsClient = new BackendDictsClient();
        await connection.RegisterClient(dictsClient);
        var dictsWithStructsClient = new BackendDictsWithStructsClient();
        await connection.RegisterClient(dictsWithStructsClient);
        var dictsWithArraysClient = new BackendDictsWithArraysClient();
        await connection.RegisterClient(dictsWithArraysClient);
        var dictKeysClient = new BackendDictKeysClient();
        await connection.RegisterClient(dictKeysClient);
        var objectPath = new ComYarpcTestserviceDicts();
        await DictsInterfaces.Dicts.Configure(dictsClient, objectPath, logger, stoppingToken);
        await DictsInterfaces.DictsWithStructs.Configure(dictsWithStructsClient, objectPath, logger, stoppingToken);
        await DictsInterfaces.DictsWithArrays.Configure(dictsWithArraysClient, objectPath, logger, stoppingToken);
        await DictsInterfaces.DictKeys.Configure(dictKeysClient, objectPath, logger, stoppingToken);

        await connection.RegisterObjectPathAsync(objectPath);
        Console.WriteLine("Dicts interface configured");
        return ([dictsClient, dictsWithStructsClient, dictsWithArraysClient, dictKeysClient], objectPath);
    }
}