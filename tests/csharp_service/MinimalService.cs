namespace csharp_service;
using TestService.Generated;

public class MinimalServiceWorker : BackgroundService
{
    private readonly ILogger<MinimalServiceWorker> _logger;

    public MinimalServiceWorker(ILogger<MinimalServiceWorker> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        var client = new BackendMinimalClient();

        var service = new MinimalInterface();
        service.OnBump = async ()=>{
            await client.BumpAsync();
        };

        client.Bumped += ()=>{service.EmitBumped();};
        var connection = new Connection();
        await connection.RegisterInterfaceAsync(service);
        await connection.RegisterClient(client);
        await connection.ConnectAsync(stoppingToken);
    }
}