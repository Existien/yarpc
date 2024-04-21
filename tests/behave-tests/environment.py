import sys
import asyncio


def before_scenario(context, _scenario):
    context.cleanup_actions = []
    context.tasks = []
    context.mocks = {}
    context.last_return_values = {}


def after_scenario(context, _scenario):
    first_error = None

    # Run cleanup actions
    context.cleanup_actions.reverse()
    for cleanup_action in context.cleanup_actions:
        try:
            cleanup_action()
        except Exception as e:
            print(f"Error during cleanup: {type(e).__name__}: {e}", file=sys.stderr)
            if first_error is None:
                first_error = e

    # Cancel remaining tasks
    for task in context.tasks:
        if not task.done():
            task.cancel()
            try:
                asyncio.get_event_loop().run_until_complete(task)
            except asyncio.CancelledError:
                pass

    # Re-raise first error
    if first_error:
        raise first_error
