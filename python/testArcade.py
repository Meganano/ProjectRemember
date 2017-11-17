import arcade
from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import random


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


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
    count = 0

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

    return lastCount
                                    


def on_draw(self):
    arcade.start_render()
    test = board()
    print (test)
    text = 1
    arcade.draw_text("ROUND"+str(text),300,300,arcade.color.RED,30,width=200,align="center",anchor_x="center",anchor_y="center")

def checkOrder(arrayColor,arraySwitch,count):
    result = False
    for x in range(0,count+1):
        if arrayColor[x] == arraySwitch[x]:
            result = True
        else:
            result = False
            break
    return result

def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"REMEMBER?")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw,1/80)
    arcade.run()

if __name__ == '__main__':
    main()
