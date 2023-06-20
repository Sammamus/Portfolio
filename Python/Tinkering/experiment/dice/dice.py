import json
from random import randint

my_dict = {}

for i in range(100):
    num = randint(1, 6)

    if num not in my_dict:
        my_dict[num] = 1
    else:
        my_dict[num] += 1

    print(f"Dice Roll: {num}")

print(json.dumps(my_dict, indent=4, sort_keys=True))