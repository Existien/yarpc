namespace csharp_service;
using TestService.Generated;

public class DBusWorker : BackgroundService
{
    private readonly ILogger<DBusWorker> _logger;
    private Connection _connection = new Connection();

    public DBusWorker(ILogger<DBusWorker> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        var connectionTask = _connection.ConnectAsync(stoppingToken);
        var withArgs = await DBusObjects.WithArgs.Configure(_connection, _logger, stoppingToken);
        var minimal = await DBusObjects.Minimal.Configure(_connection);
        await connectionTask;
    }
}