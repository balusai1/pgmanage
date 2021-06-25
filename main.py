import sys
import psycopg2
import os
from app import load_dotenv
from app.createUser import create_role
from app.sendMail import send_email


def main():
    useremail = sys.argv[1]
    username = sys.argv[2]
    userpassword = sys.argv[3]
    create_role(username, userpassword)
    with open("users_list.csv", "a+") as list:
        list.seek(0)
        data = list.read(100)
        if len(data) > 0:
            list.write("\n")
        list.write(f'{username},{userpassword}')
    list.close()
    send_email(useremail, username)


if __name__ == '__main__':
    main()
