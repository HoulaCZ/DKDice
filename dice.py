import re
import random

sum = 0
dices = 0
dice = "c"

while(re.search(r"^([0-9]+)[d k]([0-9]+)$", dice) != False):
    dice = input("Insert dices:")
    if re.search(r"^([0-9]+)[d]([0-9]+)$", dice) != None:
        dices = re.split("d", dice)
        break
    elif re.search(r"^([0-9]+)[k]([0-9]+)$", dice) != None:
        dices = re.split("k", dice)
        break

diceAmounts = int(dices[0])
diceValue = int(dices[1])

for i in range(1,(diceAmounts+1)):
    throw = random.randint(1,(diceValue))
    sum = throw + sum

print(sum)