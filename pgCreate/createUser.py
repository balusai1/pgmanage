# * Create a user/role with username and password on postgres with login
    # * Username and password are supplied as stdin(args)
# * Create Databases for user with prefix username
#     username_hr_db
#     username_retail_db
# * grant access to given list of Databases on username
# * Add username to a pg_users_active.csv
import sys
import psycopg2
import os

database_list=['database1','db2','db3']
host='localhost'
port='5433'
pguser='admin'
pgpassword='hNg9X7CYcDLv'
conn = psycopg2.connect(
    host=host,
    port=port,
    database='postgres',
    user=pguser,
    password=pgpassword)
conn.autocommit = True
cur = conn.cursor()

def createRole(user,password):
    cur.execute(f"""
    CREATE ROLE {user} with NOCREATEDB LOGIN ENCRYPTED PASSWORD '{password}';""")
    return ;

def CreateDB(username,paswd):
    for i in database_list:
        cur.execute("CREATE DATABASE " + str(username)+"_"+str(i))

def createUsers():
    list =open("users_list.csv","a")
    username= sys.argv[1]
    paswd= sys.argv[2]
    createRole(username,paswd)
    CreateDB(username,paswd)
    conn.close()
    print("Connection closed")
    list.write(username+","+paswd+"\n")
    list.close()
createUsers()
