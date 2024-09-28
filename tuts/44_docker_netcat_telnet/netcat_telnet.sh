
# Technique 2 in the Docker In Practice 2nd Ed. book

docker run -d -i -p 1234:1234 --name daemon ubuntu:14.04 nc -l 1234

telnet localhost 1234

q

docker logs daemon

docker rm daemon

docker run -d --restart=always ubuntu echo done

docker ps

docker run -d --restart=on-failure:10 ubuntu /bin/false

docker ps -a
