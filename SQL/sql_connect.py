import _mysql

cnx = _mysql.Connect(user='whiterabbit', passwd='ticktock', host="chip.swau.edu", db='library')
cursor = cnx.cursor()

# Creating the add user function
add_user = ('INSERT INTO users'
            '(firstname, lastname, username, password, email)'
            'VALUES (%s, %s. %s, %s, %s)')

user_info = ('abdiel', 'rumaldo', 'abdielrumado', 'password1', 'abdielrumaldom@gmail.com')

# Adding the user
cursor.execute(add_user, user_info)
emp_no = cursor.lastrowid

# Commit to the Database
cnx.commint()

cursor.close()
cnx.close()
