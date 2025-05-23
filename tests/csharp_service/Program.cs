using csharp_service;

var builder = Host.CreateApplicationBuilder(args);
// builder.Services.AddHostedService<Worker>();
builder.Services.AddHostedService<DBusWorker>();

var host = builder.Build();
host.Run();
