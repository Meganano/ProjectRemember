from practicum import McuBoard,find_mcu_boards

####################################
class McuWithPeriBoard(McuBoard):

    ################################
    def setLed(self, led_no, led_val):
        '''
        Set status of LED led_no on peripheral board to led_val
        '''
        self.usb_write(request=0,index=led_no,value=led_val)

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
        return result[0]==0

    ################################
    def getSwitchBlue(self):
        result = self.usb_read(request=4,length=1)
        return result[0]==1

    ################################
'''    def getLight(self):
        result = self.usb_read(request=3,length=2)
#        print(result)
        return (result[1]*256) + result[0]'''
