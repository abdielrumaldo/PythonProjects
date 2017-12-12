import _mysql

cnx = _mysql.Connect(user='whiterabbit', passwd='ticktock', host="chip.swau.edu", db='library')
cursor = cnx.cursor()

# Adding the user
cursor.execute(add_user, user_info)
emp_no = cursor.lastrowid

# Commit to the Database
cnx.commint()

cursor.close()
cnx.close()
