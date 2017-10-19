import random
import sys
import os

super_villains = {'Fiddler' : 'Isacc Bowin',
                 'Captain Cold' : 'Leonard Snart',
                 'Weather Wizard' : 'Mark Mardon',
                 'Mirror Master' : "Sam Scudder",
                 'Pied Piper' : 'Thomas Peterson'}

print(super_villains['Captain Cold'])

del super_villains['Fiddler']
super_villains['Pied Piper'] = 'Hartley Rathway'

print("Number of supervillans %i." % (len(super_villains)))

print(super_villains.get('Pied Piper'))

print("Villans: %s " % (super_villains.keys()))

print("Secret ID's: %s " % (super_villains.values()))