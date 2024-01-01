FROM ubuntu:23.04

RUN apt-get -y update && \
    apt-get install --no-install-recommends -y \
        build-essential \
        cmake \
        dbus \
        git \
        ninja-build \
        python3 \
        python3-pip \
        python3-venv \
        python3-dbus \
        tmux \
        vim \
    && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --break-system-packages -U pip pdm
    # pip \
    # behave \
    # dbus-next \
    # pytest \
    # jsonschema \
    # Jinja2

ENTRYPOINT ["/bin/bash", "-lc", "exec dbus-run-session -- \"$0\" \"$@\""]
