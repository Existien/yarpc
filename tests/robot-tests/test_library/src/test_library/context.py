import asyncio

class Context:
    def __init__(self):
        self.cleanup_actions = []
        self.tasks = []
        self.mocks = {}
        self.loop = asyncio.get_event_loop()