
# ps 	-e flag = everyprocess running on system
#	-f flag = full set of columns

ps -ef | less


ps -ef --sort=user | less 


# specify column names that you want to display for processes (in quotations)
# ps -o flag =  User-defined format ... then provide the list of column names after this.
# 	process ID / username / group name / nice value / virtual memory size / resident memory size / and command name (e.g. gedit)
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

# !!!!!!!!!!!!!!!!!!!!!!!!!!   CAUTION -- THIS ONLY WORKS if gedit is NOT OPENED ALREADY
# !!!!!!!!!!!!!!!!!!!!!!!!!!		  ENSURE YOU DIDN'T MANUALLY OPEN IT EARLIER .... 

gedit &
jobs 		# similar to 'ps' but only shows this shells jobs.

default SIGTERM signal, which requests the current process to terminate gracefully
The SIGTERM signal is a generic signal used to cause program termination. Unlike SIGKILL , this signal can be blocked, handled, and ignored. It is the normal way to politely ask a program to terminate.

gedit &
kill -SIGSTOP 937942	# get the process ID from previous command

killall -SIGCONT gedit	# this RESTARTS gedit process.

sudo apt-get install -y x11-apps
xeyes &
xeyes &
xeyes &
killall xeyes &


:'
The nice and renice commands allow users to adjust the scheduling priority of processes, influencing how the Linux kernel allocates CPU time among them.
	    ‘nice’ Command: This command is used to start a new process with a specific priority, known as the “nice value.” A higher nice value lowers the process’s priority, while a lower (negative) nice value increases it. Processes with higher priority receive more CPU time.
  	    ‘renice’ Command: Unlike nice, which sets the priority when starting a process, renice modifies the priority of an already running process. This flexibility allows system administrators to manage process priorities based on the current system load dynamically. 

'

nice -n 5 gedit &

renice -n 7 21578  # whatever number appeard for the previous command

# ps -- show the Nice value // command name (e.g. gedit) //  process ID // username.
ps -eo 'pid,user,nice,comm' | grep gedit

