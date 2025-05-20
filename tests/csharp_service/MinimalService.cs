namespace csharp_service;
using testservice;
using testservice.minimal;

public class MinimalServiceWorker : BackgroundService
{
    private readonly ILogger<MinimalServiceWorker> _logger;

    public MinimalServiceWorker(ILogger<MinimalServiceWorker> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        var client = new MinimalClient();

        var service = new Minimal();
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