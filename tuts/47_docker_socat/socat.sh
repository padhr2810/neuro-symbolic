
:'
Using socat is a powerful way to debug not only Docker, but any other network ser-
vices you might come across in the course of your work

Socat is quite a Swiss Army knife and can handle quite a number of different
protocols. The preceding example shows it listening on a Unix socket, but you
could also make it listen on an external port with TCP-LISTEN:2375,fork
instead of the UNIX-LISTEN:… argument. This acts as a simpler version of tech-
nique 1. With this approach there’s no need to restart the Docker daemon
(which would kill any running containers). You can just bring the socat listener
up and down as you desire.

 Because the preceding point is so simple to set up and is temporary, you can use
it in combination with technique 47 to join a colleague’s running container
remotely and help them debug an issue. You can also employ the little-used
docker attach command to join the same terminal they started with docker
run, allowing you to collaborate directly.

If you have a shared Docker server (perhaps set up with technique 1) you could
use the ability to expose externals and set up socat as the broker between the
outside world and the Docker socket to make it act as a primitive audit log,
recording where all requests are coming from and what they’re doing.
'

socat -v UNIX-LISTEN:/tmp/dockerapi.sock,fork \
UNIX-CONNECT:/var/run/docker.sock &

# now run a simple docker command and can inspect the output thanks to socat.
docker -H unix:///tmp/dockerapi.sock ps -a
