from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import random

devs = find_mcu_boards()

if len(devs) == 0 :
    print("*** No practicum board found.")
    exit(1)

b = McuWithPeriBoard(devs[0])

ledcolor = [1,2,4,8]
randomNum = random.choice(ledcolor)
b.setLedValue(randomNum)
print("START : Switch Ver.")

while True:
    inp = input()
#    if inp == 3: #for python
    if inp == "3": #for python3 
        randomNum = random.choice(ledcolor)
        b.setLedValue(randomNum)
        print (randomNum)

