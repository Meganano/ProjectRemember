from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import random

def checkOrder(arrayColor,arraySwitch,count):
    result = False
    for x in range(0,count+1):
        if arrayColor[x] == arraySwitch[x]:
            result = True
        else:
            result = False
            break
    return result

def pAr(array):
    string = ""
    for x in array:
        string = string + " " + str(x)
    print(string)

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

while (1):
    press = -1
    arraySwitch = []
    while (press < count):
        #print ("p"+str(press)+" c"+str(count))
        swR = b.getSwitchRed()
        swY = b.getSwitchYellow()
        swG = b.getSwitchGreen()
        swB = b.getSwitchBlue()

        if swR is True:
            arraySwitch.append(1)
            press +=1
            print ("RED")
        elif swY is True:
            arraySwitch.append(2)
            press +=1
            print ("YEL")
        sleep(0.2) 

    if (press == count):
        pAr(arrayColor)
        print("---------")
        pAr(arraySwitch)
        if checkOrder(arrayColor,arraySwitch,count) == True:
            count += 1
            numled = random.choice(ledcolor)
            b.setLedValue(numled)
            arrayColor.append(numled)
            print ("Level"+(str(count+1)))
        else:
            print ("GameOver")
            break


