import arcade
from practicum import find_mcu_boards
from peri import McuWithPeriBoard
from time import sleep
import random
from newgame import Round

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Application(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="REMEMBER?")
        self.world = World()

    def setup(self):
        output_round = "ROUND: {}".format(Round.count)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
       	#arcade.draw_text(output_round,300,300,arcade.color.WHITE,40)
        arcade.draw_text("CAN SOMEONE SEE THIS?",300,250,arcade.color.BLUE,40)

def main():
    window = Application(SCREEN_WIDTH,SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
