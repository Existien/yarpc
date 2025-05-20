namespace csharp_service.testservice.minimal;
using Tmds.DBus;

[DBusInterface("com.yarpc.testservice.minimal")]
public interface IMinimal : IDBusObject
{
    Task BumpAsync();
    Task<IDisposable> WatchBumpedAsync(Action reply);
}

class Minimal : IMinimal
{
    public event Action? Bumped;
    public Func<Task>? OnBump {get;set;}

    public static readonly ObjectPath Path = new ObjectPath("/com/yarpc/testservice/minimal");

    public async Task BumpAsync()
    {
        if (OnBump is null)
        {
            throw new NotImplementedException("Missing implementation for Bump method");
        }
        await OnBump.Invoke();;
    }

    public void EmitBumped()
    {
        Bumped?.Invoke();
    }

    public Task<IDisposable> WatchBumpedAsync(Action reply)
    {
        return SignalWatcher.AddAsync(this, nameof(Bumped), reply);
    }

    public ObjectPath ObjectPath{ get{ return Path; }}
}