import random
import sys
import os

# if else elif == != > < >= >=

age = 34;

if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")


if (age >= 1) and (age <= 18):
    print("You get a birthday!")
elif (age >= 50) or (age == 65):
    print('You get an alright B-Day..')
elif not(age == 30):
    print('You have a B-day I guess')

