FROM ubuntu:24.04

RUN apt-get -y update && \
    apt-get install --no-install-recommends -y \
        bash-completion \
        build-essential \
        bustle \
        cmake \
        dbus \
        d-feet \
        git \
        less \
        locales \
        ninja-build \
        python3 \
        python3-pip \
        python3-venv \
        python3-dbus \
        tmux \
        vim \
        # Qt dependencies
        libglib2.0-dev \
        libgles2 \
        libgles-dev \
        libglvnd-dev \
        libdbus-1-dev \
        libfontconfig1-dev \
        libfreetype6-dev \
        libx11-dev \
        libx11-xcb-dev \
        libxext-dev \
        libxfixes-dev \
        libxi-dev \
        libxrender-dev \
        libxcb1-dev \
        libxcb-cursor-dev \
        libxcb-glx0-dev \
        libxcb-keysyms1-dev \
        libxcb-image0-dev \
        libxcb-shm0-dev \
        libxcb-icccm4-dev \
        libxcb-sync-dev \
        libxcb-xfixes0-dev \
        libxcb-shape0-dev \
        libxcb-randr0-dev \
        libxcb-render-util0-dev \
        libxcb-util-dev \
        libxcb-xinerama0-dev \
        libxcb-xkb-dev \
        libxkbcommon-dev \
        libxkbcommon-x11-dev \
        xvfb \
        xfwm4 \
        psmisc \
    && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --break-system-packages -U \
    pdm \
    aqtinstall \
    cookiecutter \
    sphinx \
    sphinx_rtd_theme

WORKDIR /Qt
RUN aqt install-qt linux desktop 6.5.3 gcc_64

RUN sed -Ei '/en_US\.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8

ENTRYPOINT ["/bin/bash", "-lc", "exec dbus-run-session -- \"$0\" \"$@\""]
