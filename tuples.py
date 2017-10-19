import random
import sys
import os

# cant really change tuples

pi_tuple = (3, 1, 4, 1, 5, 9)

new_tuple = list(pi_tuple)
# make changes to tuple
new_list = tuple(new_tuple)

print('Lenth:', len(new_list))
print('Min:', min(new_tuple))
print('Max:', max(pi_tuple))

for item in new_tuple:
    print(item, end='')