
# Combination of Techniques 6 & 7 (in the book Docker In Practice 2nd ed.)

:'
1: open up your containers to the host network by exposing ports.
2: connect containers to one another with Docker’s user-defined networks feature, ensuring outsiders can’t access your internal services
'


docker run -d -p 10001:80 --name blog1 wordpress
docker run -d -p 10002:80 --name blog2 wordpress
#       can access these via localhost:10001 and localhost:10002

docker ps | grep blog

docker network create my_network

docker network connect my_network blog1

docker run -it --network my_network ubuntu:16.04 bash

docker rm -f blog1 blog2

:'
You can use this technique to set up any number of containers in a cluster on their
own private network, only requiring that the containers have some way of discovering
each other’s names

One additional point of note is the interesting final state of the blog1 container.
All containers are connected to the Docker bridge network by default, so when we
asked for it to join my_network, it did so in addition to the network it was already on. In
technique 80 we’ll look at this in more detail to see how network straddling can be used
as a model for some real-world situations.
'
