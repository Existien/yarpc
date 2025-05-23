namespace csharp_service.DBusObjects;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendWithArgsClientPayloads;
using ServicePayload = TestService.Generated.WithArgsInterfacePayloads;

class WithArgs
{
    public static async Task<(IClient[], ComYarpcTestserviceWithArgs)> Configure(Connection connection, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        var withArgsClient = new BackendWithArgsClient();
        var objectPath = new ComYarpcTestserviceWithArgs();
        await connection.RegisterClient(withArgsClient);
        await WithArgsInterfaces.WithArgs.Configure(withArgsClient, objectPath, logger, stoppingToken);

        var primitivesClient = new BackendPrimitivesClient();
        await connection.RegisterClient(primitivesClient);
        WithArgsInterfaces.Primitives.Configure(primitivesClient, objectPath);

        await connection.RegisterObjectPathAsync(objectPath);
        return ([withArgsClient, primitivesClient], objectPath);
    }
}