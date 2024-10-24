
mkdir $HOME/bin

touch $HOME/bin/myownscript

# if you include #!/bin/bash  ... RENDERS IT EXECUTABLE ... SO CAN JUST USE THE SCRIPT NAME IN BASH ... IF OMIT THIS LINE, NEED TO USE "bash" COMMAND I.E. "bash myscript"
#    	DOUBLE QUOTES = WILL PRINT THE VALUE OF $(date)
#	SINGLE QUOTES = WON'T PRINT THE VALUE, WOULD LITERALLY PRINT THE CHARACTERS.
#	$(pwd) ... $(hostname) ... I.E. THE SCRIPT CAN ACCESS YOUR USUAL BASH COMMANDS
#  BACK-TICKS I.E. ` ` ... MAKES IT SHOW THE RESULT OF A COMMAND INSTEAD OF JUST THE CHARACTERS IN THE COMMAND NAME
#	E.G. `date` WOULD SHOW THE ACTUAL DATE BUT MUST INCLUDE THE BACK-TICKS.
# backslash = escape a special character ... e.g. \$HOME would print the characters including the '$' ... RATHER THAN THE VALUE OF THE ENV VAR.

:' IN TEXT EDITOR:
#!/bin/bash
# myownscript
# List some information about your current system
echo "Today is $(date)."
echo "You are in $(pwd) and your host is $(hostname)"
'

# IT'S ALREADY EXECUTABLE COZ INCLUDED  #!/bin/bash ... THIS ENSURES THE PERMISSIONS ARE OK.

chmod 755 $HOME/bin/myownscript

touch $HOME/bin/myposition

# THESE ARE UNIVERAL VARS FOR EVERY SHELL SCRIPT... $1 IS ALWAYS THE FIRST ARG ... $2 ALWAYS 2ND ARG THAT WAS USED TO RUN THE SHELL SCRIPT ... ETC
#     IN EVERY SHELL SCRIPT, $# GIES THE TOTAL NUMBER OF ARGS / PARAMS THAT WERE USED WITH THE COMMAND WHEN CALLING IT.
#     IN EVERY SHELL SCRIPT $@ IS THE FULL LIST OF ARGS THAT WERE PASSED TO THE COMMAND USED TO CALL THE SHELL SCRIPT.

:' IN TEXT EDITOR:
#!/bin/bash
# myposition
ONE=$1
TWO=$2
THREE=$3
echo "There are $# parameters that include: $@"
echo "The first is $ONE, the second is $TWO, the third is $THREE."
'

chmod 755 $HOME/bin/myposition

myposition Where Is My Hat Buddy?

touch $HOME/bin/myhome
chmod 755 $HOME/bin/myhome

# "read" COMMAND = GETS USER INPUT ... THE VAR NAME ASSIGNED TO USER INPUT IS GIVEN AT THE END OF COMMAND (e.g. below it is "mystreet")
# 	-p FLAG = use the string as a prompt i.e. a prompt for the user.
#	IF DO IT WITHOUT THE "-p FLAG" THERE IS NO STRING PROMPT, BUT THE USER STILL CAN ENTER INPUT.

:'
#!/bin/bash
# myhome
read -p "What street did you grow up on?" mystreet
read -p "What town did you grow up in?" mytown
echo "The street I grew up on was $mystreet and the town was $mytown"
'

myhome

touch $HOME/bin/myos
chmod 755 $HOME/bin/myos

# CONDITION TO BE TESTED IS ALWAYS ENCLOSED IN SQUARE BRACKETS ... 
# "fi" IS THE OPPOSITE OF "if" ... IMPLIES THE "if" STATEMENT IS FINISHED. 
# WHEN ASSIGNING SHELL VARIABLES, CANNOT LEAVE ANY SPACE BEFORE OR AFTER THE "=" ... I.E. X=2
#	BUT IN A CONDITION, FINE TO LEAVE SPACE.

:'
#!/bin/bash
# myos
read -p "What is your favourite operating system, Mac, Windows or Linux?" opsys
if [$opsys = Mac ] ; then 
  echo "Mac is nice, but not tough enough for me."
elif [$opsys = Windows ]  ; then
  echo "I used Windows once. What is that blue screen for?"
elif [$opsys = Linux ] ; then
  echo "Great Choice!"
else
  echo "Is $opsys an operating system?"
fi
'

touch $HOME/bin/animals
chmod 755 $HOME/bin/animals

# "done" ends a while-loop (or for-loop or similar).

:'
#!/bin/bash
# animals
for ANIMALS in moose cow goose sow ; do
  echo "I have a $ANIMALS"
done
' 

animals

