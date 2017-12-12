import MySQLdb
import csv
import random

# Create Lists

fname = []
lname = []
title = []
genre = []
level = []


def urlgen():

    imgurl = [
        {"path": "City", "MAX": 8},
        {"path": "Colour", "MAX": 13},
        {"path": "LandWater", "MAX": 14},
        {"path": "Mountains", "MAX": 31},
        {"path": "Nature", "MAX": 37},
        {"path": "Space", "MAX": 4},
        {"path": "Water", "MAX": 13}
        ]
    max = len(imgurl)
    index = random.randrange(0, max)
    suffix = ".jpg"

    urlname = imgurl[index]["path"]
    urlnumber = random.randrange(1, imgurl[index]["MAX"])
    return(urlname + str(urlnumber) + suffix)



# Open and read files
with open('firstname.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        fname.append(row['firstname'])


with open('lastname.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lname.append(row['lastname'])

with open('books_new.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title.append(row['Title'])
        genre.append(row['Genre'].upper())

        # Sort according to genre
        if row['Genre'].upper() == 'NONFICTION':
            randint = random.randrange(1, 4)
            if randint == 1:
                row['Genre'] = 'MUSIC'
            if randint == 2:
                row['Genre'] = 'HISTORY'
            if randint == 3:
                row['Genre'] = 'BIOGRAPHY'
            level.append('1')
        elif row['Genre'].upper() == 'FICTION':
            randint = random.randrange(1, 4)
            if randint == 1:
                row['Genre'] = 'FANTASY'
            if randint == 2:
                row['Genre'] = 'SCI-FI'
            if randint == 3:
                row['Genre'] = 'ROMANCE'
            level.append('2')
        elif row['Genre'].upper() == 'SCIENCE':
            randint = random.randrange(1, 4)
            if randint == 1:
                row['Genre'] = 'CHEMISTRY'
            if randint == 2:
                row['Genre'] = 'PHYSICS'
            if randint == 3:
                row['Genre'] = 'BIOLOGY'
            if randint == 4:
                row['Genre'] = 'ECOLOGY'
            level.append('3')
        else:
            level.append('4')


# Open Connection to MySQL
cnx = MySQLdb.Connection(user='whiterabbit', passwd='ticktock', host="chip.swau.edu", db='library')
cursor = cnx.cursor()

# Creating the add user function
add_user = ("INSERT INTO books (title, lastname, firstname, isbn_16, isbn_10, pub_year,"
            " publisher, category, availability, level, img_url)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

for x in range(len(title)):
    book_title = title[x]   # Book title generation
    isbn10 = random.randrange(1000000000000, 9999999999999)  # Generate ISBN 10
    isbn16 = random.randrange(1000000000000000, 9999999999999999)    # Generate ISBN 16
    year = random.randrange(1400, 2017)  # Generate a year
    lnum = random.randrange(0, len(lname))   # Generate last name
    fnum = random.randrange(0, len(fname))   #Generate first name


    user_info = ( book_title, lname[lnum], fname[fnum], isbn16, isbn10, year, lname[random.randrange(0, len(lname))], genre[x], 1, level[x], urlgen())
    emp_no = cursor.lastrowid
    cursor.execute(add_user, user_info)

# Commit to the Database
cnx.commit()

# Close Connection
cursor.close()
cnx.close()
