#include <avr/io.h>
#include "peri.h"

void init_peripheral()
{
	/*	PC0 RED
		PC1 YELLOW
		PC2 GREEN
		PC3 BLUE*/
	
	//เซ็ตขาของ LED ให้ทำงานเป็น ouput
	//ส่งลอจิก 0 ให้ LED(ปิดไฟ)
	DDRC |= (1<<PC0) | (1<<PC1) | (1<<PC2) | (1<<PC3); 
	PORTC &= ~(1<<PC0);
	PORTC &= ~(1<<PC1);
	PORTC &= ~(1<<PC2);
	PORTC &= ~(1<<PC3); 
	
	//เช็ตขาswitchให้ทำงานเป็น input
	//ส่งลอจิก 1 ให้ switch(ไม่กดswitch)
	DDRD &= ~(1<<PD0); 
	PORTD |= (1<<PD0);
	DDRD &= ~(1<<PD1);
	PORTD |= (1<<PD1);
	DDRD &= ~(1<<PD5);
	PORTD |= (1<<PD5);
	DDRD &= ~(1<<PD6);
	PORTD |= (1<<PD6);
}


void set_led(uint8_t pin,uint8_t state)
{
	if (state)
		PORTC |= (1 << pin);
	else
		PORTC &= ~(1 << pin);
}

void set_led_value(uint8_t value)
{
	PORTC &= ~(0b00001111);
	PORTC |= (value & 0b00001111); 
}
