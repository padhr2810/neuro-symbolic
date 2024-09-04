# create a projects dir in your Home dir.
# Create 9 empty files (house1 - house9) 
# Then list just those 9 files.
mkdir $HOME/projects/
touch $HOME/projects/house{1..9}
ls  $HOME/projects/house{1..9}

# Make a new directory and subdirectory in a single command
mkdir -p  $HOME/d1/d2
# this would not be possible without the `-p` flag. This implies create `parent` directories as needed.

# copy the files `house1` and `house5` to a different directory
cp $HOME/projects/house[15] $HOME

# Recursively copy the xfonts files to a different directory
cp -ra /usr/share/doc/xfonts*/ $HOME/projects/
# -a, --archive   ......        same as -dR --preserve=all
# -R, -r, --recursive  ......   copy directories recursively

# Recursively list the contents of $HOME/projects directory. Pipe the output to the `less` command to page through output.
ls -lR $HOME/projects/ | less

# remove the files house6, house7, house8 without being prompted
rm -f $HOME/projects/house[678]

# move hosue3 and house4 to the $HOME/d1/d2/  directory
mv $HOME/projects/house{3,4} $HOME/d1/d2/

# change the permissions on the $HOME/projects/house2 file so that it can be read and written to by the user who owns the file, only read by the group, and have no permission for others
chmod 640 $HOME/projects/house2

# recursively change the permissions of the $HOME/projects/ directory so that nobody has write permission to any files or directories beneath that point in the file system.
chmod -R a-w  $HOME/projects
ls -lR $HOME/projects

