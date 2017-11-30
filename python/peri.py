from practicum import McuBoard,find_mcu_boards
from time import sleep

####################################
class McuWithPeriBoard(McuBoard):

    ################################
    def setLedValue(self, value):
        '''
        Display value's 3 LSBs on peripheral board's LEDs
        '''
        self.usb_write(request=5,value=value)

    ################################
    def getSwitchRed(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        result = self.usb_read(request=1,length=1)
        return result[0]==1


    ################################
    def getSwitchYellow(self):
        result = self.usb_read(request=2,length=1)
        return result[0]==2

    ################################
    def getSwitchGreen(self):
        result = self.usb_read(request=3,length=1)
        return result[0]==32

    ################################
    def getSwitchBlue(self):
        result = self.usb_read(request=4,length=1)
        return result[0]==64

