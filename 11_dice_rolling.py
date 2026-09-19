'''
import random

dice = random.randint(1, 6)

print("You rolled:", dice)

'''

import random

choice = input("Roll the dice? (yes/no): ")

if choice.lower() == "yes":
    dice = random.randint(1, 6)
    print("You rolled:", dice)
else:
    print("Game ended")