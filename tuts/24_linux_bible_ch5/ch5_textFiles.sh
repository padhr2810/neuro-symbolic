

cp /etc/services /tmp
vi /tmp/services

# / searches forward in vim
#     and ? searches backwards.
# cw = erase the next word and enter input mode.
# ESC = back to command mode.

# VIM:
:'
/WorldWideWeb<Enter>
cwWorld Wide Web<Esc>
:wq
'

# 5dd = delete 5 lines.
# dd = delete 1 line.
# G = go to end of file.
# p = put i.e. paste

vi /tmp/services
:'
/Note that it is<Enter>
5dd
G
p
'

# : = ex mode
# :g = go or get
# /s/ = substitute
# /s// ..../g = substitute ALL
# g = implies all occurrences (not just the first one)
# s// implies the entire file, but s/ implies just this line.
vi /tmp/services
:'
:g/tcp/s//WHATEVER/g<Enter>
'


# 2 = implies error e.g. permission error. e.g. no matches found.
# file descriptor '2' is standard errors. (integer = 2)
#		'0' is standard output. (integer = 0 )
# 		'1' is standard input. (integer = 1 )
#  redirect any errors to "/dev/null"
#  -name = gives the name of the file you're searching for (i.e. "passwd"). The directory is "/etc".
# locate is quicker than find coz uses database. find is slower but always up-to-date and has more options (size, modification time, etc)

find /etc -name passwd 2> /dev/null


# chmod 777 = gives ALL users read / write / execute permissions.
# NEVER RUN THIS - DANGEROUS - chmod -R 777  ..... applies 777 to every file on system under Root.
#		will impact home / media directories etc if these are under root.
#  -type f  =  only files.
#  -perm -002  =  permissions... 2 = files must be writeable for others.
#       WITHOUT THE SECOND HYPHEN IT'S STRICTER:
# 	I.E. -perm 002 IMPLIES ONLY FILES WITH ZERO PRIVILEGES FOR OWNER / GROUP, BUT write FOR ALL OTHERS.
#		-perm -002 IMPLIES write FOR OTHERS, AND WILDCARD FOR OWNER / GROUP.
# if omit the 2nd "-" IT DOESN'T FIND ANY RESULTS AT ALL COZ IT'S MUCH MORE CONSTRAINED.

mkdir $HOME/TEST
touch $HOME/TEST/{one,two,three}
chmod 777 $HOME/TEST/{one,two,three}
find $HOME -perm  -002 -type f -ls


find /usr/share/doc -mtime +300


# -exec = EXECUTE ON A NEW SHELL. BUT WITHOUT CREATING A NEW PROCESS.
# {var} = VARIABLE SUBSTITUTION ... { } MEANS WHATEVER THE HECK YOU FOUND.
# \; = end of command given after 'exec'

mkdir /tmp/FILES
find /usr/share -size +5M -size  -10M  -exec cp {}  /tmp/FILES \;
du -sh /tmp/FILES/*


find /tmp/FILES/  -type f  -exec cp {} {}.mybackup \;

# grep = -r = Recursive in a directory.
# 	 -l = List the results.
#	 -i = case-insensitive.
#	SINGLE DOT i.e. '. IMPLIES SEARCH THE CURRENT DIRECTORY.
# Looking for the term 'e1000' obviously.
#  --color = highlight the term in colour.

yum install kernel-doc		# for RedHat
apt install linux-doc		# Ubuntu
cd /usr/share/doc/linux-doc*   # for RedHat: cd /usr/share/doc/kernel-doc*
grep -rli e1000 . 
grep -ri  --color e1000 .

