import random
import sys
import os

# lists are like arrays
grocery = ['potatoes', 'cookies', 'tomatoes', 'cake batter']

for item in grocery:
    print(item)

grocery[0] = 'apples'

for item in grocery:
    print(item)

# subset
print(grocery[1:3])  # Note that it prints up to 3 but not 3

# list inside lists

other_events = ['wash car', 'Pick up kids', "Cash Check"]

to_do_list = [other_events, grocery]
print(to_do_list)

print((to_do_list[0][0]))   # [a][b] a: List index b:item in a's index
print()

grocery.append('onions')
grocery.insert(1, 'Pickles')
grocery.remove("cookies")

print()
for item in grocery:
    print(item)

print()
grocery.sort()

for item in grocery:
    print(item)

grocery.reverse()

print()
for item in grocery:
    print(item)

newlist = other_events + grocery    # note that there aren't 2 lists but just 1
print(newlist)

print("There are %i items in the newlist" % (len(newlist)))
print("%s is the last values in  newlist" % (max(newlist)))
print("%s is the first value in  newlist" % (min(newlist)))
