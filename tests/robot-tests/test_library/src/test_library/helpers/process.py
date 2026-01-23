import psutil
import textwrap

def __process_name(process):
    return '"'+' '.join(process.args)+'"'


def __print_process_output(process):
    stdout = process.stdout.read()
    stdout = stdout.decode('unicode_escape') if stdout is not None else ''
    print(textwrap.indent(f"Stdout for {__process_name(process)}:\n{textwrap.indent(stdout, 2*' ')}", 2*' '))
    stderr = process.stderr.read()
    stderr = stderr.decode('unicode_escape') if stderr is not None else ''
    print(textwrap.indent(f"Stderr for {__process_name(process)}:\n{textwrap.indent(stderr, 2*' ')}", 2*' '))

def shutdown_process(process, timeout_in_s=3):
    proc_name = __process_name(process)
    print(f"\n{'='*len(proc_name)}")
    print(f"{proc_name}")
    print(f"{'='*len(proc_name)}\n")

    if process.poll() is None:
        parent = psutil.Process(process.pid)
        children = parent.children(recursive=True)
        alive = [parent, *children]
        for survivor in alive:
            survivor.terminate()
        _, alive = psutil.wait_procs(alive, timeout=timeout_in_s)
        for survivor in alive:
            survivor.kill()
        _, alive = psutil.wait_procs(alive, timeout=timeout_in_s)
        if alive:
            raise RuntimeError(f"Unkillable processes: {alive}")

    __print_process_output(process)