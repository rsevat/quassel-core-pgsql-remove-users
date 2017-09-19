#!/usr/bin/python

import sys
import psycopg2
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user-to-delete', dest='deluser')
    parser.add_argument('--list-users', dest='list', action='store_true', default=False)
    parser.add_argument('--database', default='quassel')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--user', default='pgsql')
    parser.add_argument('--password')
    args = parser.parse_args()
    
    try:
        cmd = "dbname='" + str(args.database) + "' user='" + str(args.user) + \
        "' host='" + str(args.host) + "' password='" + str(args.password) + "'"
        conn = psycopg2.connect(cmd)
    except:
        print("unable to connect to the database")
        sys.exit(1)

    if(args.list):
        listUsers(args, conn)
    if(args.deluser):
        deleteUser(args, conn)

def deleteUser(args, conn):
    user = args.deluser

    cursor = conn.cursor()
    cursor.execute("SELECT userid FROM quasseluser WHERE username='" + user + "'")
    userid = (cursor.fetchone())[0]
    
    print("Deleting user: " + user + ", with userid: " + str(userid))
    cursor.execute("DELETE FROM quasseluser WHERE username='" + user + "'")
    for table in ['buffer', 'network', 'ircserver', 'user_setting', 'identity']:
        cursor.execute("DELETE FROM " + table + " WHERE userid='" + str(userid) + "'")

    cursor.execute("DELETE FROM identity_nick WHERE identityid not in (SELECT identityid FROM identity)")
    cursor.execute("DELETE FROM backlog WHERE bufferid not in (SELECT bufferid from buffer)")
    conn.commit()

def listUsers(args, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT userid,username FROM quasseluser");
    users = cursor.fetchall()
    print(users)

main()
