import random

tries = 0
total = 0

while total != 12:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    tries += 1
    total = die1 + die2

print(tries)