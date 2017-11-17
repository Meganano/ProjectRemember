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

	DDRD &= ~(1<<PD0); 
	PORTD |= (1<<PD0);
	DDRD &= ~(1<<PD1);
	PORTD |= (1<<PD1);
	DDRD &= ~(1<<PD2);
	PORTD |= (1<<PD2);
	DDRD &= ~(1<<PD3);
	PORTD |= (1<<PD3);

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
	int count = 0;
	init_peripheral();
	while(1)
	{
		set_led_value(count);
		count = (count+1)%8;
		while(!(PIND & (1<<PD0))){
		
		}
		_delay_ms(5);
		while(PIND & (1<<PD0)){
		
		}
		_delay_ms(5);
		
	}
}





