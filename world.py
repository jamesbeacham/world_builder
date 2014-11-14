import acre
from random import choice 

Hex = ["water", "land"]

index = 3

while index > 0:
    print choice(Hex)
    index = index - 1

