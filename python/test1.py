from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import random

devs = find_mcu_boards()

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

b = McuWithPeriBoard(devs[0])

#ledcolor = [1,2,4,8]
ledcolor = [1,2]
numled = random.choice(ledcolor)
b.setLedValue(numled)

arrayColor = []
arrayColor.append(numled)
count = 0

print ("START : Switch Ver.")

while True:
    swR = b.getSwitchRed()
    swY = b.getSwitchYellow()
    swG = b.getSwitchGreen()
    swB = b.getSwitchBlue()

    if swR is True:
        if (arrayColor[count]==1):
            numled = random.choice(ledcolor)
            arrayColor.append(numled)
            b.setLedValue(numled)
            print ("Switch"+str(numled))
            count += 1
        else:
            print ("GameOver")
            break
        sleep(0.5)
    elif swY is True:
        if (arrayColor[count]==2):
            numled = random.choice(ledcolor)
            arrayColor.append(numled)
            b.setLedValue(numled)
            print ("Switch"+str(numled))
            count += 1
        else:
            print ("GameOver")
            break
        sleep(0.5)

