#!/bin/bash
set -o errexit
set -o nounset

thisdir="$(realpath "$(dirname "$(readlink -f "$0")")")"

if [[ $# > 0 ]]; then
    interactive=0
else
    interactive=1
fi

# cleanup actions on script exit
cleanup_cmds=()
cleanup() {
    for cmd in "${cleanup_cmds[@]}"; do
        bash -c "$cmd"
    done
}
trap cleanup EXIT

docker_args=()
docker_env=()
docker_args+=(--rm)
if [[ $interactive == 1 ]]; then
    args="exec /bin/bash"
    docker_args+=(-ti)
else
    args="$@"
fi

# use current user in container
user_id="$(id -u)"
group_id="$(id -g)"
user_name="$(id -un)"
user_home="/home/$user_name"
docker_args+=(-u "$user_id:$group_id")
docker_env+=("USER=$user_name")

docker_args+=(--tmpfs "${user_home}:rw,exec,uid=$user_id,mode=0700")
docker_env+=("HOME=$user_home")
docker_env+=("XDG_RUNTIME_DIR=$user_home")

passwd="$(mktemp --suffix=.docker.passwd)"
cleanup_cmds+=("rm -f $passwd")
echo "$user_name:x:$user_id:$group_id::$user_home:/bin/bash" > "$passwd"
docker_args+=("--volume" "$passwd:/etc/passwd")
docker_args+=("--volume" "${user_home}/.gitconfig:${user_home}/.gitconfig:ro")

# forward x11
if [ -n "${DISPLAY:-}" ]; then
    xauth="$(mktemp --suffix=.docker.xauth)"
    cleanup_cmds+=("rm -f $xauth")
    xauth nlist "$DISPLAY" | sed -e 's/^..../ffff/' | xauth -f "$xauth" nmerge -
    docker_args+=(-v "/tmp/.X11-unix:/tmp/.X11-unix:ro")
    docker_args+=(-v "$xauth:$xauth:ro")
    docker_env+=("DISPLAY=$DISPLAY")
    docker_env+=("XAUTHORITY=$xauth")
    docker_args+=(--ipc "host")
else
    echo "DISPLAY variable not set"
fi

# mount repo
docker_args+=(-v "$thisdir/..:/workspace")
docker_args+=(--workdir "/workspace")

# create env file
envfile="$(mktemp --suffix=.env)"
cleanup_cmds+=("rm -f $envfile")
for var in "${docker_env[@]}"; do
    echo "$var" >> "$envfile"
done
docker_args+=(--env-file "$envfile")
docker_args+=(-v "$envfile:/run/sdk-env")

# Export D-Bus session to other shells
args="echo \"export DBUS_SESSION_BUS_ADDRESS=\$DBUS_SESSION_BUS_ADDRESS\" >> /run/sdk-env; $args"

docker run "${docker_args[@]}" yarpc-sdk bash -c "$args"