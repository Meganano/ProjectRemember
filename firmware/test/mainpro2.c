#define F_CPU 16000000UL

#include<stdio.h>
#include<avr/io.h>
#include<util/delay.h>



void init_peripheral()
{
	DDRC |= (1<<PC0) | (1<<PC1) | (1<<PC2) | (1<<PC3);
        PORTC &= ~(1<<PC0);
	PORTC &= ~(1<<PC1);
	PORTC &= ~(1<<PC2);
	PORTC &= ~(1<<PC3);

}

void set_led(uint8_t pin,uint8_t state)
{
        if (state){
               PORTC |= (1 << pin);
        }
        else{
               PORTC &= ~(1 << pin);
        }
}

void set_led_value(uint8_t value)
{
        PORTC &= ~(0b00001111);
        PORTC |= (value & 0b0001111);
}

int main()
{
	init_peripheral();
	while(1)
	{
		set_led_value(1);
		_delay_ms(100);
		set_led_value(2);
		_delay_ms(100);
		set_led_value(4);
		_delay_ms(100);
		set_led_value(8);
		_delay_ms(100);
		
	}
}





