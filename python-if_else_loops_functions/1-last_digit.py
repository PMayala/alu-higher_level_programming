#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end="")
if number > 0:
    last = number % 10
    if last > 5:
        print(f"{last} and is greater than 5")
    elif last == 0:
        print(f"{last} and is 0")
    else:
        print(f"{last} and is less than 6 and not 0")
elif number < 0:
    last = abs(number) % 10
    if last == 0:
        print(f"{last} and is 0")
    else:
        print(f"-{last} and is less than 6 and not 0")
else:
    print("0 and is 0")
