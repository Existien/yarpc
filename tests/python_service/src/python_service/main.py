from .basic_gen.connection import Connection
from .minimal_service import get_minimal_service_and_backend_client
from .with_args_service import get_with_args_service_and_backend_client
from .primitives_service import get_primitives_service_and_backend_client
from .structs_service import get_structs_service_and_backend_client
import asyncio


async def run():
    services, backend_clients = list( x for x in zip(
        get_minimal_service_and_backend_client(),
        get_with_args_service_and_backend_client(),
        get_primitives_service_and_backend_client(),
        get_structs_service_and_backend_client(),
    ))

    print("Service running")
    _, pending = await asyncio.wait(
        map(lambda x: asyncio.create_task(x), [
            *map(
                lambda client: client.connect(),
                backend_clients
            ),
            Connection.run(*services),
        ]),
        return_when=asyncio.FIRST_EXCEPTION
    )
    for task in pending:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

def main():

    asyncio.run(run())

if __name__ == "__main__":
    main()