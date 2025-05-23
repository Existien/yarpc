namespace csharp_service.DBusObjects.WithArgsInterfaces;
using TestService.Generated;

using ClientPayload = TestService.Generated.BackendWithArgsClientPayloads;
using ServicePayload = TestService.Generated.WithArgsInterfacePayloads;

class WithArgs
{
    public static async Task Configure(BackendWithArgsClient client, ComYarpcTestserviceWithArgs objectPath, ILogger<DBusWorker> logger, CancellationToken stoppingToken)
    {
        objectPath.WithArgsInterface.OnNotify = async (string message) => {
            await client.NotifyAsync(message);
        };
        client.Notified += (ClientPayload.Notified payload) => {
            objectPath.WithArgsInterface.EmitNotified(new ServicePayload.Notified(payload.message));
        };

        objectPath.WithArgsInterface.OnOrder = async (string item, UInt32 amount, double pricePerItem) => {
            return await client.OrderAsync(item, amount, pricePerItem);
        };
        client.OrderReceived += (ClientPayload.OrderReceived payload) => {
            objectPath.WithArgsInterface.EmitOrderReceived(new ServicePayload.OrderReceived(
                payload.item, payload.amount, payload.pricePerItem
            ));
        };

        objectPath.WithArgsInterface.SetSpeed = async (double newValue, WithArgsInterfaceProperties oldProps) => {
            await client.SetSpeedAsync(newValue);
            oldProps.Speed = await client.GetSpeedAsync();
            return oldProps;
        };
        objectPath.WithArgsInterface.SetDistance = async (uint newValue, WithArgsInterfaceProperties oldProps) => {
            await client.SetDistanceAsync(newValue);
            oldProps.Distance = await client.GetDistanceAsync();
            return oldProps;
        };

        client.OnPropertiesChanged += (KeyValuePair<string, object>[] changes) => {
            var props = objectPath.WithArgsInterface.Properties;
            foreach (KeyValuePair<string, object> entry in changes)
            {
                switch (entry.Key)
                {
                    case "Speed":
                        props.Speed = (double)entry.Value;
                        break;
                    case "Distance":
                        props.Distance = (uint)entry.Value;
                        break;
                    case "Duration":
                        props.Duration = (double)entry.Value;
                        break;
                }
            }
            objectPath.WithArgsInterface.Properties = props;
        };

        bool arePropertiesSet = false;
        while(!arePropertiesSet)
        {
            try
            {
                var clientProps = await client.GetAllAsync();
                objectPath.WithArgsInterface.Properties = new WithArgsInterfaceProperties()
                {
                    Speed = clientProps.Speed,
                    Duration = clientProps.Duration,
                    Distance = clientProps.Distance
                };
                arePropertiesSet=true;
            }
            catch (Exception e)
            {
                await Task.Delay(1000, stoppingToken);
                logger.LogWarning($"{e.Message}");
            }
        }
    }
}