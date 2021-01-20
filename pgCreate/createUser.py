# * Create a user/role with username and password on postgres with login
    # * Username and password are supplied as stdin(args)
# * Create Databases for user with prefix username
#     username_hr_db
#     username_retail_db
# * grant access to given list of Databases on username
# * Add username to a pg_users_active.csv
import sys
import 


# createRole(user,password)
#
# return 1
#
# CreateDB(user,password)


def createUsers():

    username= sys.argv[1]
    paswd= sys.argv[2]
    print(username,paswd)
createUsers()
# createRole(username,paswd)
# CreateDB(username,paswd)
