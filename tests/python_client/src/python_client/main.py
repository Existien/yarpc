from .minimal_client import get_minimal_client
from .with_args_client import get_with_args_client
from .structs_client import get_structs_client
from .arrays_client import get_arrays_client
from .arrays_with_structs_client import get_arrays_with_struct_client

import asyncio

async def runner():
    clients, loops = list( x for x in zip(
        # get_minimal_client(),
        # get_with_args_client(),
        # get_structs_client(),
        # get_arrays_client(),
        get_arrays_with_struct_client(),
    ))

    print("Client running")
    await asyncio.gather(
        *map(
            lambda client: client.connect(),
            clients
        ),
        *loops
    )


def main():
    asyncio.run(runner())

if __name__ == "__main__":
    main()