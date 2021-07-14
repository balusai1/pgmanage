import sys
import psycopg2
import os
import logging

database_list=['hr_db','sms_db','retail_db']
database_user_list=['hr_user','sms_user','retail_user']
host='localhost'
port='5433'
pguser='pgadmin'
pgpassword='xmL9FkR9xHrx'
conn = psycopg2.connect(
    host=host,
    port=port,
    database='postgres',
    user=pguser,
    password=pgpassword)
conn.autocommit = True
cur = conn.cursor()

def createRole(user,password):
    for i in database_user_list:
      cur.execute(f"""CREATE ROLE {user}_{i} with NOCREATEDB LOGIN ENCRYPTED PASSWORD '{password}';""")
    return ;

def CreateDB(user,paswd):
    for i in database_list:
        cur.execute(f"""CREATE DATABASE {user}_{i};""")

def accessPermissions(user):
    for i in database_list:
        cur.execute(f"""revoke ALL on DATABASE {user}_{i} FROM PUBLIC;""")
    for i in range(len(database_user_list)):
        cur.execute(f"""Grant ALL on DATABASE {user}_{database_list[i]} TO {user}_{database_user_list[i]};""")


def createUsers():
    username= sys.argv[1]
    paswd= sys.argv[2]
    userEmail=sys.argv[3]
    createRole(username,paswd)
    CreateDB(username,paswd)
    conn.close()
    with open("users_list.csv","a+") as list:
            list.seek(0)
            data = list.read(100)
            if len(data) > 0 :
                list.write("\n")
            list.write(f'{username},{paswd}')
    print("Connection closed")
    list.close()

createUsers()
