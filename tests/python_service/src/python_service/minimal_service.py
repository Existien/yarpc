from .basic_gen.minimal_interface import MinimalInterface
from .basic_gen.backend_minimal_client import BackendMinimalClient

def get_minimal_service_and_backend_client():
    service = MinimalInterface()
    backend_client = BackendMinimalClient()
    async def bump_handler():
        return await backend_client.Bump()
    def on_bumped():
        service.Bumped()
        print("Bump emitted")
    service.on_Bump(bump_handler)
    backend_client.on_Bumped(on_bumped)
    return service, backend_client