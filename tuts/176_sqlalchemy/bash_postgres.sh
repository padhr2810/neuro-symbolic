
#INSTALL POSTGRESQL ON UBUNTU
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql

# ENABLE 
sudo update-rc.d postgresql enable
sudo service postgresql start

# SET ENV VAR FOR DATA FOLDER.
export PGDATA=/var/lib/postgresql/16/main
echo $PGDATA
# /var/lib/postgresql/16/main

# OPERATE ON THE CLUSTER AS A WHOLE USING "pg_ctlcluster" (WORKS ON UBUNTU)
sudo pg_ctlcluster 16 main start
sudo pg_ctlcluster 16 main status
sudo pg_ctlcluster 16 main restart
sudo pg_ctlcluster 16 main stop

# INSPECT PROCESSES.
pstree
pstree -p postgres

ps -C postgres -af

# CREATE A SQL SCRIPT (CAN ADD SIMPLE COMMANDS AFTER RUN 'nano')
touch test.sql
nano test.sql
# SELECT current_database();
# SELECT current_time;
# SELECT current_role;
cat test.sql

# CLIENT TOOL ON COMMAND LINE.
psql -U postgres

psql -U postgres -d template1




ls /usr/lib/postgresql/16/bin
# this is where oid2name is located.

bin/oid2name -U postgres

# check out a dir
sudo ls main/base/1 | head


#export history to a text file.
history -w ~/history.txt
nano ~/history.txt

# chapter 3:

sudo pg_ctlcluster 16 main start
#  ...  (sql version) (cluster name) action

psql -U postgres
psql postgres -U luca

# SET UP $EDITOR & $VISUAL ENV VARS TO MODIFY THE "pg_hba.conf" FILE:
# SOME FILES USE $VISUAL, SOME USE $EDITOR, SO GOOD TO POINT BOTH TO SAME EDITOR. 
locate bashrc
nano ~/.bashrc
echo $EDITOR
echo $VISUAL
# ADD THESE BOTH TO bashrc AS FOLLOWS:
# export VISUAL=vim
# export EDITOR="$VISUAL"

$EDITOR $PGDATA/pg_hba.conf
locate pg_hba.conf
sudo nano $PGDATA/pg_hba.conf 
sudo nano /etc/postgresql/16/main/pg_hba.conf

# CREATE ROLE pad WITH PASSWORD 'pw';
# CREATE ROLE pad WITH LOGIN PASSWORD 'pw';
# CREATE ROLE pad WITH PASSWORD 'pw' LOGIN;
# CREATE ROLE pad WITH LOGIN PASSWORD 'pw' VALID UNTIL '2030-12-25 23:59:59';

# CREATE ROLE book_authors WITH NOLOGIN;
# CREATE ROLE pad WITH LOGIN PASSWORD 'pw' IN ROLE book_authors;
# CREATE ROLE micko WITH LOGIN PASSWORD 'pw' IN ROLE book_authors;

# GRANT book_authors TO pad;

# CREATE ROLE book_reviewers WITH NOLOGIN ADMIN pad;

# GRANT book_reviewers TO micko WITH ADMIN OPTION;

# DROP ROLE IF EXIST i_dont_exist ;

# SELECT current_role ;

# PSQL COMMAND TO DESCRIBE ALL USERS:
# \du 

# PSQL COMMAND TO SHOW ALL GROUPS A ROLE IS A MEMBER OF:
# \drg 

# SELECT rolname, rolcanlogin, rolconnlimit, rolpassword FROM pg_roles WHERE rolname = 'pad' ;

# SELECT rolname, rolcanlogin, rolconnlimit, rolpassword FROM pg_authid WHERE rolname = 'pad' ;

# SELECT pg_reload_conf() ;

# chapter 4:

<<comment1
 Line 1 of a Bash shell script comment
 Line 2 of the comment 
 The comment's Name can be anything ... the comment is completed by simply stating the name (as below)
comment1

