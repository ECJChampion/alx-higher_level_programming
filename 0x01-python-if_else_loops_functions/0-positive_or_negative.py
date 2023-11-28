#!/usr/bin/python3
import random
# print whether the number stored in the variable numbei
# is positive or negative
number = random.randint(-10, 10)

if number < 0:
    print(f"{number} is negative")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is zero")
