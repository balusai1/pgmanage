# * Check the user exist on OS by looping on pg_users_active.csv
# * If username not found on OS
# * Delete the Databases with prefix of username
# * Delete the user/role from Database postgresql
# * Remove the userfrom pg_users_active.csv
import sys
import psycopg2
import pwd
import csv

host='localhost'
port='5433'
pguser='admin'
pgpassword='hNg9X7CYcDLv'
database_list=['database1','db2','db3']
conn = psycopg2.connect(
    host=host,
    port=port,
    database='postgres',
    user=pguser,
    password=pgpassword)

def deleteRole(user,cur):
    try:
      cur.execute(f'DROP ROLE {user};')
    except:
      return

def deleteDb(user,cur):
    for i in database_list:
        try:
          cur.execute("DROP DATABASE " + str(user)+"_"+str(i))
        except:
            continue

def deleteList(user):
  lines = list()
  username=(user)

  with open('users_list.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        for field in row:
            if field == username:
                lines.remove(row)

  with open('users_list.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)


def deleteUsers():
    with open("users_list.csv") as users_list:
        conn.autocommit = True
        for userdetails in users_list:
            user=userdetails.split(",")[0]
            try:
              user_id=pwd.getpwnam(user)
            except:
              cur = conn.cursor()
              deleteDb(user,cur)
              deleteRole(user,cur)
              conn.close()
              deleteList(user)
deleteUsers()
