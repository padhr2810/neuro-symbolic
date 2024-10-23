# create a projects dir in your Home dir.
# Create 9 empty files (house1 - house9) 
# Then list just those 9 files. Even if other files are present, don't list them, only the 9.
# if one of the 9 houses is missing (eg. deleted) then the "ls" throws an error
# curly braces for enclosing a variable (e.g. foo) and parameter expansion
# Two dots i.e. '..' is used to specify a range (e.g. a range from 1-9 =  {1..9}
# 	only 2 dots, not an ellipsis.

mkdir $HOME/projects/
touch $HOME/projects/house{1..9}
ls  $HOME/projects/house{1..9}

# Make a new directory and subdirectory in a single command
# this would not be possible without the `-p` flag. This implies create `parent` directories as needed.

mkdir -p  $HOME/d1/d2


# copy the files `house1` and `house5` to a different directory
# square brackets contain a set of characters. e.g. [15] below is a set of 2 numbers, 1 & 5 ... 
# square brackets = like looping over each item in set.

cp $HOME/projects/house[15] $HOME

# Recursively copy the xfonts files to a different directory

cp -ra /usr/share/doc/xfonts*/ $HOME/projects/

# -a, --archive   ......        same as -dR --preserve=all
# 		preserves everything about the file; SELinux attributes, links, xattr, everything. It's "archive mode." 
#		except -a does not preserve hardlinks, coz finding  multiply-linked files is expensive.  You must separately specify -H
# -R, -r, --recursive  ......   copy directories recursively

# Recursively list the contents of $HOME/projects directory. Pipe the output to the `less` command to page through output.

ls -lR $HOME/projects/ | less

# remove the files house6, house7, house8 without being prompted

rm -f $HOME/projects/house[678]

# move hosue3 and house4 to the $HOME/d1/d2/  directory
# can do this with square brackets or curly brackets - here are 2 EQUIVALENT METHODS:

mv $HOME/projects/house{3,4} $HOME/d1/d2/
mv $HOME/projects/house[34] $HOME/d1/d2/

# change the permissions on the $HOME/projects/house2 file so that it can be read and written to by the user who owns the file, only read by the group, and have no permission for others
# chmod = 3 sets of permissions. 1: owner of the file; 2: members of the file's group; 3: everyone else. 

chmod 640 $HOME/projects/house2

# recursively change the permissions of the $HOME/projects/ directory so that nobody has write permission to any files or directories beneath that point in the file system.
chmod -R a-w  $HOME/projects
ls -lR $HOME/projects

# "ls -l" list the file permissions for files and directories.
:'
On each line, the first character identifies the type of entry that is being listed. If it is a dash (-) it is a file. If it is the letter d it is a directory.

The next nine characters represent the settings for the three sets of permissions.

    The first three characters show the permissions for the user who owns the file (user permissions).
    The middle three characters show the permissions for members of the files group (group permissions)
    The last three characters show the permissions for anyone not in the first two categories (other permissions)

There are three characters in each set of permissions. The characters are indicators for the presence or absence of one of the permissions. They are either a dash (-) or a letter. If the character is a dash, it means that permission is not granted. If the character is an r, w, or an x, that permission has been granted.

The letters represent:
    r: Read permissions. The file can be opened, and its content viewed.
    w: Write permissions. The file can be edited, modified, and deleted.
    x: Execute permissions. If the file is a script or a program, it can be run (executed).

For example:
    --- means no permissions have been granted at all.
    rwx means full permissions have been granted. The read, write, and execute indicators are all present.
chmod numerical shorthand: 111 = read/write/execute permission.
    just think of it as binary. So "111" = 7 (i.e. all 3 permissions granted) ... "101" = read and execute only ie. = 5
Silly Linux mistake exposes a terabyte of secret Pokemon company data: foolishly did "chmod 777"
'

