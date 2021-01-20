# * Check the user exist on OS by looping on pg_users_active.csv
# * If username not found on OS
# * Delete the Databases with prefix of username
# * Delete the user/role from Database postgresql
# * Remove the userfrom pg_users_active.csv
