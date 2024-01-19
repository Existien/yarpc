from .minimal_client import get_minimal_client
from .with_args_client import get_with_args_client

import asyncio

async def runner():
    clients, loops = list( x for x in zip(
        get_minimal_client(),
        get_with_args_client(),
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