namespace csharp_service.testservice.minimal;
using Tmds.DBus;

[DBusInterface("com.yarpc.backend.minimal")]
public interface IMinimalClient : IDBusObject
{
    Task BumpAsync();
    Task<IDisposable> WatchBumpedAsync(Action reply);
}

public class MinimalClient : IClient
{
    private IMinimalClient? _interface;
    public event Action? Bumped;

    public async Task Connect(Tmds.DBus.Connection connection)
    {
        _interface = connection.CreateProxy<IMinimalClient>("com.yarpc.backend", "/com/yarpc/backend/minimal");
        await _interface.WatchBumpedAsync(()=>{Bumped?.Invoke();});
    }

    public void Disconnect()
    {
        _interface = null;
    }

    public async Task BumpAsync()
    {
        if (_interface is null)
        {
            throw new NotConnectedException("MinimalClient is not connected to D-Bus");
        }
        else
        {
            await _interface.BumpAsync();
        }
    }
}