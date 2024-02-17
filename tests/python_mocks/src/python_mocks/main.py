from python_mocks import Connection
from .minimal_mock import get_minimal_mock
from .with_args_mock import get_with_args_mock
from .primitives_mock import get_primitives_mock
from .structs_mock import get_structs_mock
from .arrays_mock import get_arrays_mock
from .arrays_with_structs_mock import get_arrays_with_structs_mock
import asyncio


def main():
    mocks = [
        get_minimal_mock(),
        get_with_args_mock(),
        get_primitives_mock(),
        get_structs_mock(),
        get_arrays_mock(),
        get_arrays_with_structs_mock(),
    ]

    print("Python mock service running")
    asyncio.run(Connection.run(*mocks))

if __name__ == "__main__":
    main()