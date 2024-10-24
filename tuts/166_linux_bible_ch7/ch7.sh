
mkdir $HOME/bin

touch $HOME/bin/myownscript

:' IN TEXT EDITOR:
#!/bin/bash
# myownscript
# List some information about your current system
echo "Today is $(date)."
echo "You are in $(pwd) and your host is $(hostname)"
'

chmod 755 $HOME/bin/myownscript

touch $HOME/bin/myposition

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

:'
#!/bin/bash
# animals
for ANIMALS in moose cow goose sow ; do
  echo "I have a $ANIMALS"
done
' 

animals

