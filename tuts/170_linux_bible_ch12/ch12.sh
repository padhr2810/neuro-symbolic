
#  3 x Methods to check the device name of a USB that you insert into your computer.

# Method 1: 
# lsblk = lists information about all available or the specified block devices.
#	By default, the command prints all block devices (except RAM
#       disks) in a tree-like format. The same device can be repeated in
#       the tree if it relates to other devices.

lsblk

# Using lsblk with some custom output columns I was able to find a more precise solution. See:
lsblk -o NAME,MAJ:MIN,RM,SIZE,RO,TYPE,MOUNTPOINT,VENDOR,HOTPLUG

# Using lsblk -h its possible to see all available output columns
lsblk -h 


# Method 2: 
# List the contents of /dev directory before and after inserting the USB.
# 	then use the "diff" command to see what changed.

ls -1 /dev > ~/before.txt
# plug it in, then
ls -1 /dev > ~/after.txt
diff ~/before.txt ~/after.txt





# Method 3:
# try doing lsusb with and without the USB installed ... see if it shows up.

lsusb


# List partitions on the USB device:
# 	Linux allows only 4 primary partitions. You can have a much larger number of logical partitions by sub-dividing one of the primary partitions. Only one of the primary partitions can be sub-divided. 
# 	fdisk = short for "format disk"

sudo fdisk -l /dev/sdb

