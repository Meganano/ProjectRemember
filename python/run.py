from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import random
import os

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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

def runGame():
    ledcolor = [1,2,4,8] 
    numled = random.choice(ledcolor)
    b.setLedValue(numled)

    arrayColor = []
    arrayColor.append(numled)
    count = 0

    os.system('clear')
    print ("  START : Press the button in color sequence  ")
    print ("--------------------Level1--------------------")

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
                print ("|                      "+str(press+1)+"                     |")
                print ("|                     "+bcolors.FAIL+"RED"+bcolors.ENDC+"                    |")
            elif swY is True:
                arraySwitch.append(2)
                press +=1
                print ("|                      "+str(press+1)+"                     |")
                print ("|                     "+bcolors.WARNING+"YEL"+bcolors.ENDC+"                    |")
            elif swG is True:
                arraySwitch.append(4)
                press +=1
                print ("|                      "+str(press+1)+"                     |")
                print ("|                     "+bcolors.OKGREEN+"GRN"+bcolors.ENDC+"                    |")
            elif swB is True:
                arraySwitch.append(8)
                press +=1
                print ("|                      "+str(press+1)+"                     |")
                print ("|                     "+bcolors.OKBLUE+"BLU"+bcolors.ENDC+"                    |")
            sleep(0.2) 

        if (press == count): 
            if checkOrder(arrayColor,arraySwitch,count) == True:
                count += 1
                numled = random.choice(ledcolor)
                if (count!=0):
                    while (numled == arrayColor[count-1]):
                        numled = random.choice(ledcolor)
                b.setLedValue(numled)
                arrayColor.append(numled)
                os.system('clear')
                print ("                  REMEMBER??                  ")
                print ("--------------------Level"+(str(count+1))+"--------------------")
            else:
                print (bcolors.FAIL+"-------------------GAMEOVER-------------------"+bcolors.ENDC)
                for x in range(0,2):
                    b.setLedValue(15)
                    sleep(0.2)
                    b.setLedValue(0)
                    sleep(0.2)
                b.setLedValue(6)
                print ("")
                print ("                    Retry?                    ")
                print (bcolors.WARNING+"           Yellow = No  "+bcolors.ENDC+bcolors.OKGREEN+"GREEN = Yes"+bcolors.ENDC)
                while (True):
                    swY2 = b.getSwitchYellow()
                    swG2 = b.getSwitchGreen()
                    if (swG2 is True):
                        print("")
                        print ("                   Continue                  ")
                        sleep(0.5)
                        runGame()
                    elif (swY2 is True):
                        print("")
                        print ("                   Bye Bye!                  ")
                        b.setLedValue(15)
                        sleep(1)
                        b.setLedValue(0)
                        exit()

#############################

runGame()

