from python_mocks import Connection
from .minimal_mock import get_minimal_mock
from .with_args_mock import get_with_args_mock
from .primitives_mock import get_primitives_mock
import asyncio


def main():
    mocks = [
        get_minimal_mock(),
        get_with_args_mock(),
        get_primitives_mock(),
    ]

    print("Python mock service running")
    asyncio.run(Connection.run(*mocks))

if __name__ == "__main__":
    main()