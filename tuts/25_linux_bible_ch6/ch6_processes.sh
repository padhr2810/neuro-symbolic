
# ps 	-e flag = everyprocess running on system
#	-f flag = full set of columns

ps -ef | less


ps -ef --sort=user | less 


# specify column names that you want to display for processes (in quotations)
# ps -o flag =  User-defined format ... then provide the list of column names after this.

ps -eo 'pid,user,group,nice,vsz,rss,comm' | less 


# ` top` command allows users to interactively manage processes. Pressing 'k' enables the user to kill a specific process by entering its PID.
#  interactive command mode where the top half portion will contain the statistics of processes and resource usage. And Lower half contains a list of the currently running processes. Pressing q will simply exit the command mode. 
#		P = sort by CPU usage.
#		M = sort by memory consumption.

top
:'
P
M
P
M
'


# Run 'gedit' -- Text Editor (gedit) is the default GUI text editor in the Ubuntu operating system
#  With & appended to the command, the process starts in the background, so you can continue to use the shell 
# When you use SIGSTOP to a process, it will pause the process. It will not resume automatically unless you send a SIGCONT signal to it.
# This is great because it allows you to pause a process without terminating it.
# 	I used this to pause my rsync backup at 8 AM in the morning and to resume it at 6 PM (office hours) so the backup wouldn’t bother people working during the day.

gedit &


default SIGTERM signal, which requests the current process to terminate gracefully
The SIGTERM signal is a generic signal used to cause program termination. Unlike SIGKILL , this signal can be blocked, handled, and ignored. It is the normal way to politely ask a program to terminate.

gedit &
kill -SIGSTOP 937942	# get the process ID from previous command

killall -SIGCONT gedit	# this works if you ran the "gedit &" command many times - kills them all.

sudo apt-get install -y x11-apps
xeyes &
xeyes &
xeyes &
killall xeyes &

nice -n 5 gedit &

renice -n 7 21578  # whatever number appeard for the previous command

ps -eo 'pid,user,nice,comm' | grep gedit

