import acre
from random import choice 

Hex = ["water", "land"]

def worldBuilder():
    index = 3

    while index > 0:
        print choice(Hex)
        index = index - 1

if __name__ == "__main__":
    worldBuilder()
