namespace csharp_service;
using csharp_service.Services;

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
        var minimal = Minimal.Configure(_connection);
        await _connection.ConnectAsync(stoppingToken);
    }
}