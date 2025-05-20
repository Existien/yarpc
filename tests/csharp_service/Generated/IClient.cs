namespace csharp_service.testservice;
using Tmds.DBus;

public interface IClient
{
    Task Connect(Tmds.DBus.Connection connection);
    void Disconnect();
}