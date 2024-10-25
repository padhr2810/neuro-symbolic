
# Add a new user. 
#	"-c" is usually used to specify a user's full name
#	"-s" = specify the default shell
#	username here = mrt
# UID = the next available one.

sudo useradd -c "Mr T" -s /bin/sh mrt


# grep to check out the new user account for 'mrt'

grep mrt /etc/passwd

# set the pw for new user

sudo passwd mrt


# Make a new group called "testing" and give it the group ID 315
sudo groupadd -g 315 testing
grep testing /etc/group

# add mrt (new user) to both the 'testing' and the 'bin' groups.
#	-a = append ... i.e. Add the user to the supplementary group(s). Use only with the -G option.
#	-G = --groups ... i.e. A list of supplementary groups which the user is also a member of. Each group is separated from the next by a comma,
#            with no intervening whitespace. The groups must exist.
#	     If the user is currently a member of a group which is not listed, the user will be removed from the group. This
#            behaviour can be changed via the -a option, which appends the user to the current supplementary group list.

sudo usermod -aG testing,bin mrt
grep mrt /etc/group


# userdel = removes the user account ... removes a user's attributes without removing the user's home directory by default. 
#	The user name must already exist. 
#	If the -r flag is specified, the userdel command also removes the user's home directory.

userdel mrt

