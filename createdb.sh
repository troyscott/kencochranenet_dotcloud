#!/usr/bin/env bash
# this only works if you have the mysqlclient installed. Keeping it around for an example.

# grab the username and password from the dotcloud environment.yml file
dbuser=`grep DOTCLOUD_DB_SQL_LOGIN ~/environment.yml | cut -f2 -d' '`
dbpass=`grep DOTCLOUD_DB_SQL_PASSWORD ~/environment.yml | cut -f2 -d' '`

# this is the database we want to create
dbname="blogdb"

#check if db exists
echo "Creating a database for $dbname"
DBS=`mysql -u$dbuser -p$dbpass -Bse 'show databases'| egrep -v 'information_schema|mysql'`
for db in $DBS; do
    if [ "$db" = "$dbname" ] ; then
        echo "This database already exists : exiting now"
        exit
    fi
done

#create database
mysqladmin -u$dbuser -p$dbpass create $dbname;
echo "Database $dbname created"

# if you wanted to, this is where you could create your user and give correct permissions
# and have the those values hard coded in your settings.py