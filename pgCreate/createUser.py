# * Create a user/role with username and password on postgres with login
    # * Username and password are supplied as stdin(args)
# * Create Databases for user with prefix username
#     username_hr_db
#     username_retail_db
# * grant access to given list of Databases on username
# * Add username to a pg_users_active.csv
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

def createRole(user,password):
    print(conn,user,password)
    conn.close()
    print("Connection closed")
    conn

def createUsers():
    username= sys.argv[1]
    paswd= sys.argv[2]
    print(username,paswd)
    createRole(username,paswd)

createUsers()

# CreateDB(username,paswd)
