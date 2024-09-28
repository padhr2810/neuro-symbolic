
#sudo snap remove docker    # remove the snap installed version coz just want the apt installed version
                           # this allowed me to stop the docker daemon service completely.

sudo service docker stop   #  Before you open up the Docker daemon, you must first shut the running one down.

# sudo service docker restart
                           # this restarts the docker daemon - e.g. if change config file, this will be updated.


ps -ef | grep -E 'docker(d| -d| daemon)\b' | grep -v grep 
                           # you know the daemon is stopped when this command does NOT show any output

### THIS IS WHERE IT STOPS WORKING - COZ "DOCKER DAEMON" IS NOT RECOGNISED AS A COMMAND...........
        # docker daemon = deprecated. replaced by 'dockerd' ... there is no deprecation warning.
#sudo docker daemon -H tcp://0.0.0.0:2375
sudo dockerd -H tcp://0.0.0.0:2375

                          #  restart it manually and open it up to outside users with the following command
                          #  This command starts as a daemon (docker daemon), defines the host server with the
                          #         -H flag, uses the TCP protocol, opens up all IP interfaces (with 0.0.0.0), and opens
                          #         up the standard Docker server port (2375)


ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
        # get your IP address
        # Use grep to filter IP address from ifconfig:

#docker -H tcp://<your host's ip>:2375 <subcommand>    # connect to Docker from outside
# e.g.:
docker -H tcp://192.168.1.18:2375 run hello-world
docker -H tcp://192.168.1.18:2375 ps

#export DOCKER_HOST=tcp://<your host's ip>:2375
export DOCKER_HOST=tcp://192.168.1.18:2375
docker <subcommand>
                          #   Or you can export the DOCKER_HOST environment variable 
                          # (this won’t work if you have to use sudo to run Docker

# Note that you’ll also need to do one of these from inside your local machine as well,
# because Docker is no longer listening in the default location.
# If you want to make this change permanent on your host, you’ll need to configure your startup system.
# WARNING If you use this technique to make your Docker daemon listen on a port, be aware that specifying the IP as 0.0.0.0 gives access to users on all
#        network interfaces (both public and private), which is generally considered insecure.
#  This is a great technique if you have a powerful machine dedicated to Docker inside a secure private local network, because everyone on the network can easily point
#      Docker tools to the right place—DOCKER_HOST is a well-known environment variable that will inform most programs that access Docker where to look.


THIS BIT DOESNOT WORK .... YET
docker run -p 2375:2375 -v /var/run/docker.sock:/var/run/docker.sock sequenceid/socat
        # As an alternative to the somewhat cumbersome process of stopping the Docker service and running it manually, you could combine mounting the Docker socket as a
        # volume (from technique 45) with using the socat tool to forward traffic from an external port
