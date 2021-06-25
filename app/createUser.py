import os
import psycopg2

DATABASE_LIST = os.getenv('DATABASE_LIST').split(",")
DATABASE_USER_LIST = os.getenv('DATABASE_USER_LIST').split(",")


def db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_HOST'),
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASSWORD'))
    conn.autocommit = True
    return conn.cursor()


def create_role(user, password):
    cur = db_connection()
    for i in DATABASE_USER_LIST:
        cur.execute(f"CREATE ROLE {user}_{i} with NOCREATEDB LOGIN ENCRYPTED PASSWORD '{password}';")
    create_db(cur, user)


def create_db(cur, user):
    for i in DATABASE_LIST:
        cur.execute(f"CREATE DATABASE {user}_{i};")
    access_permissions(cur, user)


def access_permissions(cur, user):
    for i in DATABASE_LIST:
        cur.execute(f"revoke ALL on DATABASE {user}_{i} FROM PUBLIC;")
    for i in range(len(DATABASE_USER_LIST)):
        cur.execute(f"Grant ALL on DATABASE {user}_{DATABASE_LIST[i]} TO {user}_{DATABASE_USER_LIST[i]};")
    cur.close()
    return
