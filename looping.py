import random
import sys
import os

for x in range(0, 10):  # up to 10 but not 10
    print(x + 1, ' ', end='')

grocery = ['potatoes', 'cookies', 'tomatoes', 'cake batter']

print('\n')    # Break

for item in grocery:
    print(item, " ", end='')

print('\n')    # Break

num_list = [[1, 2, 3,], [10, 20, 30], [100, 200, 300]]


for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

avg = 0
for x in range(0, 100000):
    times = 0;
    end = False
    total_count = 0
    while end == False:
        random_number = random.randrange(1, 21)
        count = 1;
        while random_number != 20:
            random_number = random.randrange(1, 21)
            # print(random_number, "Try number: ", count)
            count += 1

        print("It took %i tries to get to 1 attempt # %i" % (count, times))
        total_count += count
        times += 1
        if count == 1:
            end = True

    print("We had to do this %i times in order roll a 20 in your first try" % (times))
    print("That is a 1 in %i chance to roll 1 in your first try" % (total_count))
    avg += total_count

avg = avg / 100000;

print("On average there is a 1 in %i chance that you will roll a 20 in your first try" % (avg))
print("That's a %f percent chance." % ((1/avg) * 100))