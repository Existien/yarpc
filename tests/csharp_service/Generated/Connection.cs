namespace csharp_service.testservice;
using Tmds.DBus;
using testservice.minimal;

class Connection
{
    private Tmds.DBus.Connection? _connection;
    private HashSet<IDBusObject> _interfaces = [];
    private HashSet<IClient> _clients = [];

    public async Task RegisterInterfaceAsync(IDBusObject iface)
    {
        _interfaces.Add(iface);
        if (_connection is not null)
        {
            await _connection.RegisterObjectAsync(iface);
        }
    }

    public void UnregisterInterface(IDBusObject iface)
    {
        _interfaces.Remove(iface);
        if (_connection is not null)
        {
            _connection.UnregisterObject(iface);
        }
    }

    public async Task RegisterClient(IClient client)
    {
        _clients.Add(client);
        if (_connection is not null)
        {
            await client.Connect(_connection);
        }
    }

    public void UnregisterClient(IClient client)
    {
        _clients.Remove(client);
        if (_connection is not null)
        {
            client.Disconnect();
        }
    }

    private void Disconnect()
    {
        if (_connection is null) {
            return;
        }
        foreach (var iface in _interfaces)
        {
            _connection.UnregisterObject(iface);
        }
        _interfaces.Clear();
        foreach (var client in _clients)
        {
           client.Disconnect();
        }
        _clients.Clear();
        _connection?.Dispose();
        _connection = null;
    }

    public async Task ConnectAsync(CancellationToken stoppingToken)
    {
        if (_connection is not null)
        {
            return;
        }
        try {
            _connection = new Tmds.DBus.Connection(Address.Session);
            await _connection.ConnectAsync();
            await _connection.RegisterServiceAsync("com.yarpc.testservice");
            foreach (var iface in _interfaces)
            {
                await _connection.RegisterObjectAsync(iface);
            }
            foreach (var client in _clients)
            {
                await client.Connect(_connection);
            }
            await Task.Delay(Timeout.Infinite, stoppingToken);
        } finally {
            Disconnect();
        }
    }
}
