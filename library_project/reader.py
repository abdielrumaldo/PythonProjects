import csv
from random import *

# Create Lists

fname = []
lname = []
title = []
genre = []
level = []


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

        if row['Genre'].upper() == 'NONFICTION':
            level.append('1')
        elif row['Genre'].upper() == 'FICTION':
            level.append('2')
        elif row['Genre'].upper() == 'SCIENCE':
            level.append('3')
        else:
            level.append('4')


for x in range(len(title)):
    book_title = title[x]
    isbn10 = randint(1000000000000, 9999999999999)
    isbn13 = randint(1000000000000, 9999999999999)
    year = randint(1400, 2017)
    lnum = randint(0, len(lname))
    fnum = randint(0, len(fname))
    print(x, level[x], book_title, genre[x], fname[fnum], lname[lnum], isbn10, isbn13, year, lname[randint(0, len(lname))])
