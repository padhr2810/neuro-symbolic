# Technique 3 from Docker In Practice 2nd ed.

# first stop the docker daemon.
sudo service docker stop

dockerd -g /home/dockeruser/mydocker

# A new set of folders and files will be created in this directory. These folders are internal to Docker, so play with them at your peril (as we’ve discovered!

# You should be aware that this command will appear to wipe the containers and
# images from your previous Docker daemon. Don’t despair. If you kill the Docker process you just ran, and restart your Docker service, 
# your Docker client will be pointed
# back at its original location, and your containers and images will be returned to you. If
# you want to make this move permanent, you’ll need to configure your host system’s
# startup process accordingly.

: '
Aside from the obvious use case for this (reclaiming space on disks with limited disk
space), you could also use this technique if you wanted to strictly partition sets of
images and containers. For example, if you have access to multiple private Docker
registries with different owners, it might
Private network
be worth the extra effort to make sure
you don’t accidentally give private data You invoke the Docker
Your host machine
client program to get
to the wrong person.
'
