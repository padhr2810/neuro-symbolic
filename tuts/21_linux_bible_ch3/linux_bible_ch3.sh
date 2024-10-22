
# To switch virtual console (i.e. a shell prompt that simulates a physical terminal)
# hold CTRL+ALT +F2
#       or CTRL+ALT +F3 ... etc ...
# After running commands such as id, pwd, ls, press CTRL+ALT+F1 to return to the virtual console that holds your desktop.

#########  type = gives info re a command. e.g. is it shell built-in command / subroutine / alias / keyword. Also gives path to command if possible.
#########      more parsimonious output than using 'locate'
#########      for 'mount' it gives the same result as: 'which mount'
######### Find the mount command (dont want tons of results from locate mount)

type mount

#########  'type cd' doesn't give any path coz not an executable.
#########  'which cd' also doesn't give any path obviously.
#########  'type cd' --- output: `cd is a shell builtin`

type cd

###### locate = very fast way to fild a file based on filename (ie searches a database)
###### note: if cant find the file using locate, then run `sudo updatedb`
###### man pages are usually found in: /usr/share/man/ 
###### find the man page for tracepath - this finds all paths containing 'tracepath' - need to eyeball to find the 'man' page
######       e.g. for 'tracepath' it's in: /usr/share/man/man8/tracepath.8.gz


locate tracepath
sudo updatedb

###### get to end of a line in shell
###### CTRL+E
###### get to start of a line in shell
# CTRL+X

######  whats the different between `man ls` and `ls --help`
# For one, --help is not a command, it is an argument that is often given to a command to get help using it.
#  Meanwhile, man is a command, short for `manual`. MANUAL pages are installed by many programs, and are a common way to find help about commands

man ls 

ls --help 

# list the contents of your home dir (and order it by time)
ls $HOME
ls -t $HOME

# show current date. And then format to: DD/MM/YYYY
date
date +%D

man date
date --help

######   cat = reads file. cat is short for CONCATENATE - will concat multiple data streams into one.
######   Pipe the file called: /etc/services to the `less` command

cat /etc/services | less


# Creating files in Linux is a simple task that can be accomplished using various commands such as touch, echo, cat, nano and vi or vim

######  view variables to find current hostname, username, shell, and home directories

echo $HOSTNAME       #   p-HP-Pavilion-x360-Convertible-14-ba0xx
echo $USERNAME       #   p 
echo $SHELL          #   /bin/bash
echo $HOME           #   /home/p


# Add a permanent alias that displays the contents of the "/etc/passwd" file

nano $HOME/.bashrc	          # can store your aliases in this file. This allows BASH to use your aliases.
                              # the dot implies it is a hidden file in the directory. So it won't appear with a simple `ls` command. Need to do `ls -a`
                              # at the bottom of this page type:

alias m="cat /etc/passwd"


# back in shell type:

source $HOME/.bashrc	               # source = execute a script file in current shell environment.
alias m		                           # ensure the alias was set properly
m		                                 # the /etc/passwd file displays on the screen.

######   display the man page for the mount system call ... i.e. first find man pages that include the word mount.
######      grep ^mount	... i.e. must start with "mount" - hence discard if mount appears anywhere else in the phrase..

man -k mount | grep ^mount	      # -k = regexp 
                                  # grep = search for matching patterns in a file. Stands for: "global regular expression print". 
                                  # Powerful tool for scraping log files / code etc.
                                  #     -k, --apropos
              #    Approximately equivalent to apropos.  Search the short
              #    manual page descriptions for keywords and display any matches. 
              #   Each manual page has a short description available within it.
              #   apropos searches the descriptions for instances of keyword.
              #       keyword is usually a regular expression, as if (-r) was used

alias                                      # display a list of all currently set aliases.
unalias [name] 	           # e.g. `unalias m`         # remove an alias

######   run a shell script from bash

bash myscript.sh                           

