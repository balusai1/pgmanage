# * Check the user exist on OS by looping on pg_users_active.csv
# * If username not found on OS
# * Delete the Databases with prefix of username
# * Delete the user/role from Database postgresql
# * Remove the userfrom pg_users_active.csv
import sys
import psycopg2

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

def deleteRole(user,password):
    print(conn,user,password)
    cur.execute(f"""
    DROP ROLE {user};""")
    return ;

def deleteUsers():
    username=
    print(username)
    deleteRole(username)
    conn.close()
    print("Connection closed")
    deleteDB(username)

deleteUsers()
