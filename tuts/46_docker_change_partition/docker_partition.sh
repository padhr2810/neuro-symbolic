# Technique 3 from Docker In Practice 2nd ed.

# first stop the docker daemon.
sudo service docker stop

# THIS IS WHERE IT BREAKS:
dockerd -g /home/dockeruser/mydocker

# https://stackoverflow.com/questions/59345566/move-docker-volume-to-different-partition

: '
service docker stop

    Create/Edit the /etc/docker/daemon.json configuration file with location of the new data directory:

{
    "data-root": "/new/path"
}

    Copy docker files to new location:

rsync -aP /var/lib/docker/ /new/path

    Remove old directory (rename it to be safe)

mv /var/lib/docker /var/lib/docker.old

    Create symlink:

ln -s /new/path /var/lib/docker
'



: '
This part of the Docker Daemon is configurable. Best practices would have you change the data folder; 
this can be done with OS-level Linux commands like a symlink... 
I would say it's better to actually configure the Docker Daemon to store the data elsewhere!
You can do that by editing the Docker command line (e.g. the systemd script that starts the Docker daemon), 
or change /etc/docker/daemon.json.

The file should have this content:
{
  "data-root": "/path/to/your/docker"
}
If you add a new hard drive, partition, or mount point you can add it here and docker will store its data there.

'



: '
Ubuntu 16.04 uses systemd, and the /etc/default/docker file is only used for systems running upstart and sysvinit 
(see the comment in that file: https://github.com/docker/docker/blob/v1.12.0/contrib/init/sysvinit-debian/docker.default#L3-L8)
You can configure the daemon by using a daemon.json configuration file, which works independent of the process manager 
in use, and also allows you to live-reload certain settings.
See https://docs.docker.com/engine/reference/commandline/dockerd/#/daemon-configuration-file for details
Alternatively, if you want to configure through systemd, you can create a drop-in (override file), 
as is explained in https://docs.docker.com/engine/admin/systemd/#/custom-docker-daemon-options
'


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
