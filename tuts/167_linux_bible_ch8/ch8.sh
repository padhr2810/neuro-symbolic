

# switch to root
# "su" works in Red Hat but not Ubuntu coz The root account is disabled by default in Ubuntu, so there is no root password, thats why su fails with an authentication error.

sudo -i

# To find your IP address:

ip a

 
systemctl enable --now cockpit.socket


# To access cockpit on Ubuntu:

http://127.0.0.1:9090

find /var/spool -not -user root -ls | less


sudo -i 
touch /mnt/test.txt
ls -l /mnt/test.txt

# give full root privilege to a regular user via the sudo command.
sudo -i 
visudo
:'
paddy ALL=(ALL) ALL
'


############ MOUNT A USB:

sudo -i
journalctl -f 		# AFTER RUNNING THIS COMMAND, PLUG IN YOUR USB.


# IF THE USB DOES NOT MOUNT, RUN THESE COMMANDS IN A SECOND TERMINAL (AS ROOT)
# 	THIS CREATES A MOUNT POINT DIRECTORY AND MOUNTS THE DEVICE:

mkdir /mnt/test
mount /dev/sdb1 /mnt/test
umount /dev/sdb1

# SEE WHAT USB DEVICES ARE CONNECTED TO YOUR COMPUTER:
lsusb

# LOAD THE "bttv" MODULE:
#	mod = module ... adds or removes a module from the Linux kernel
#	-a = all ... i.e.     Insert all module names on the command line.
# lsmod = shows which loadable kernel modules are currently loaded 

modprobe -a bttv
lsmod | grep bttv

# modprobe -r ... If the modules it depends on are also unused, modprobe will try to remove them too. 
# 	Unlike insertion, more than one module can be specified on the command line (it does not make sense to specify module parameters when removing modules). 

modprobe -r bttv
lsmod | grep bttv


