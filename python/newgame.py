import arcade
from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep

class Round:
    count = 0
    def board():
        lastCount = 1
                devs = find_mcu_boards()
                if len(devs) == 0:
                    print("*** No practicum board found.")
                        exit(1)

                b = McuWithPeriBoard(devs[0])


                ledcolor = [1,2]
                numled = random.choice(ledcolor)
                b.setLedValue(numled)

                arrayColor = []
                arrayColor.append(numled)

                print ("START : Switch Ver.")

                while (1):
                    press = -1
                    arraySwitch = []
                    while (press < count):
                        swR = b.getSwitchRed()
                        swY = b.getSwitchYellow()

                        if swR is True:
                            arraySwitch.append(1)
                            press += 1
                            print ("RED")
                        elif swY is True:
                            arraySwitch.append(2)
                            press += 1
                            print ("YEL")
                        sleep(0.2)

                if (press == count):
                    if checkOrder(arrayColor,arraySwitch,count) == True:
                        count += 1
                                numled = random.choice(ledcolor)
                                b.setLedValue(numled)
                                arrayColor.append(numled)
                                lastCount = count
                                print ("Level"+(str(count+1)))
                        else:
                            print ("GameOver")
                            break

        def checkOrder(arrayColor,arraySwitch,count):
            result = False
                for x in range(0,count+1):
                    if arrayColor[x] == arraySwitch[x]:
                        result = True
                    else:
                        result = False
                                break
                return result

