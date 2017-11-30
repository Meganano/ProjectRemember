//#define IS_SWITCH_PRESSED() (!(((PINC)&(0b00001000))==0b00001000)) 
#define IS_SWITCH_RED_PRESSED() ~(PIND |~(1 << 0))
#define IS_SWITCH_YELLOW_PRESSED() ~(PIND |~(1 << 1))
#define IS_SWITCH_GREEN_PRESSED() ~(PIND |~(1 << 5))
#define IS_SWITCH_BLUE_PRESSED() ~(PIND |~(1 << 6))

#define RED    PC0
#define YELLOW PC1
#define GREEN  PC2
#define BLUE   PC3

#define ON     1
#define OFF    0

void init_peripheral();
void set_led(uint8_t,uint8_t);
void set_led_value(uint8_t);
