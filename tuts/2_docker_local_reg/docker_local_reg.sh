# set up a registry server on local network.

docker run -d -p 5000:5000 -v $HOME/registry:/var/lib/registry registry:2
# registry:2 is the name of the image - it gets pulled from docker hub the first time.

docker ps
