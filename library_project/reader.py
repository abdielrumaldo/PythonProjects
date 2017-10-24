import csv
from random import *

# Create Lists

fname = []
lname = []


with open('firstname.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        fname.append(row['firstname'])


with open('lastname.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lname.append(row['lastname'])


for x in range(100):
    isbn10 = randint(1000000000000, 9999999999999)
    isbn13 = randint(1000000000000, 9999999999999)
    year = randint(1400, 2017)
    lnum = randint(0, len(lname))
    fnum = randint(0, len(fname))
    print(x, fname[fnum], lname[lnum], isbn10, isbn13, year, lname[randint(0, len(lname))])
