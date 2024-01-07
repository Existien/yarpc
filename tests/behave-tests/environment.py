import sys
import signal
import textwrap
import subprocess
import psutil
import asyncio


def __process_name(process):
    return '"'+' '.join(process.args)+'"'


def __print_process_output(process):
    print(textwrap.indent(f"Stdout for {__process_name(process)}:\n{textwrap.indent(process.stdout.read().decode('unicode_escape') if process.stdout is not None else '', 2*' ')}", 2*' '))
    print(textwrap.indent(f"Stderr for {__process_name(process)}:\n{textwrap.indent(process.stderr.read().decode('unicode_escape') if process.stderr is not None else '', 2*' ')}", 2*' '))

def __shutdown_process(process, timeout_in_s=3):
    proc_name = __process_name(process)
    print(f"\n{'='*len(proc_name)}")
    print(f"{proc_name}")
    print(f"{'='*len(proc_name)}\n")

    if process.poll() is None:
        try:
            process.terminate()
            process.wait(timeout_in_s)
        except subprocess.TimeoutExpired:
            print(f"Process {proc_name} is not terminating after {timeout_in_s} seconds. Attempting SIGKILL", file=sys.stderr)
            parent = psutil.Process(process.pid)
            children = parent.children(recursive=True)
            for child in children:
                try:
                    child.send_signal(signal.SIGKILL)
                    print(f"Sent SIGKILL to child {child}")
                except psutil.NoSuchProcess:
                    pass
            process.kill()
            process.wait(timeout_in_s)
            psutil.wait_procs(children, timeout=timeout_in_s)

    __print_process_output(process)


def before_scenario(context, _scenario):
    context.processes = []
    context.cleanup_actions = []
    context.tasks = []
    context.mocks = {}


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

    # Try to shutdown processes on the processes list
    context.processes.reverse()
    for process in context.processes:
        try:
            __shutdown_process(process)
        except Exception as e:
            print(f"Error during cleanup: {type(e).__name__}: {e}", file=sys.stderr)
            if first_error is None:
                first_error = e

    # Re-raise first error
    if first_error:
        raise first_error


def before_step(context, _step):
    for process in context.processes:
        assert process.poll() is None, \
            f"""
                Process {__process_name(process)} exited unexpectedly with return code {process.returncode}.
                {__print_process_output(process)}
            """