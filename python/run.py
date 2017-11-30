from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def checkOrder(arrayColor,arraySwitch,count):
    result = False
    for x in range(0,count+1):
        if arrayColor[x] == arraySwitch[x]:
            result = True
        else:
            result = False
            break
    return result

devs = find_mcu_boards()

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

b = McuWithPeriBoard(devs[0])

ledcolor = [1,2,4,8]
numled = random.choice(ledcolor)
b.setLedValue(numled)

arrayColor = []
arrayColor.append(numled)
count = 0

print ("START : Switch Ver.")

while (1):
    press = -1
    arraySwitch = []
    while (press < count):
        swR = b.getSwitchRed()
        swY = b.getSwitchYellow()
        swG = b.getSwitchGreen()
        swB = b.getSwitchBlue()
        if swR is True:
            arraySwitch.append(1)
            press +=1
            print ("-----------"+str(press+1)+"-----------")
            print (bcolors.FAIL+"----------RED----------"+bcolors.ENDC)
        elif swY is True:
            arraySwitch.append(2)
            press +=1
            print ("-----------"+str(press+1)+"-----------")
            print (bcolors.WARNING+"----------YEL----------"+bcolors.ENDC)
        elif swG is True:
            arraySwitch.append(4)
            press +=1
            print ("-----------"+str(press+1)+"-----------")
            print (bcolors.OKGREEN+"----------GRN----------"+bcolors.ENDC)
        elif swB is True:
            arraySwitch.append(8)
            press +=1
            print ("-----------"+str(press+1)+"-----------")
            print (bcolors.OKBLUE+"----------BLU----------"+bcolors.ENDC)
        sleep(0.2) 

    if (press == count):
        if checkOrder(arrayColor,arraySwitch,count) == True:
            count += 1
            numled = random.choice(ledcolor)
            b.setLedValue(numled)
            arrayColor.append(numled)
            print ("Level"+(str(count+1)))
        else:
            print ("GameOver")
            break


