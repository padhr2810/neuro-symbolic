
git clone https://github.com/aidanhs/Docker-Terminal.git
cd Docker-Terminal

python3 -m http.server 9000
#      THEN GO TO localhost:9000
#      can start a container here
#      connects to the Docker daemon on your local computer to perform any operations

:'
It’s worth being aware of the following points if you want to give this link to other
people:
------- The other person must not be using a proxy of any kind. This is the most com-
mon source of errors we’ve seen—Docker terminal uses WebSockets, which
don’t currently work through proxies.
------- Giving a link to localhost obviously won’t work—you’ll need to give out the
external IP address.
'
