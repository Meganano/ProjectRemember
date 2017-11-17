#define F_CPU 16000000UL

#include <avr/io.h>
#include <avr/interrupt.h>  /* for sei() */
#include <util/delay.h>     /* for _delay_ms() */
#include <avr/pgmspace.h>   /* required by usbdrv.h */

#include "peri.h"
#include "usbdrv.h"


//#define RQ_SET_LED         0
#define RQ_GET_SWITCH_RED 1
#define RQ_GET_SWITCH_YELLOW 2
#define RQ_GET_SWITCH_GREEN 3
#define RQ_GET_SWITCH_BLUE 4
#define RQ_SET_LED_VALUE   5



/* ------------------------------------------------------------------------- */
/* ----------------------------- USB interface ----------------------------- */
/* ------------------------------------------------------------------------- */
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
    usbRequest_t *rq = (void *)data;

    /* declared as static so they stay valid when usbFunctionSetup returns */
    static uint8_t switch_state;  

 /*   if (rq->bRequest == RQ_SET_LED)
    {
        uint8_t led_val = rq->wValue.bytes[0];
        uint8_t led_no  = rq->wIndex.bytes[0];
        set_led(led_no, led_val);
        return 0;
    }
*/

    if (rq->bRequest == RQ_SET_LED_VALUE)
    {
        uint8_t led_val = rq->wValue.bytes[0];
        set_led_value(led_val);
        return 0;
    	    
    }

    else if(rq->bRequest == RQ_GET_SWITCH_RED) 
    {
	switch_state = IS_SWITCH_RED_PRESSED();
	usbMsgPtr = &switch_state;
	//_delay_ms(10);
	return 1;
    }
	
    else if(rq->bRequest == RQ_GET_SWITCH_YELLOW) 
    {
	switch_state = IS_SWITCH_YELLOW_PRESSED();
	usbMsgPtr = &switch_state;
	//_delay_ms(10);
	return 1;
    }

	
    else if(rq->bRequest == RQ_GET_SWITCH_GREEN) 
    {
	switch_state = IS_SWITCH_GREEN_PRESSED();
	usbMsgPtr = &switch_state;
	//_delay_ms(10);
	return 1;
    }
	
    if(rq->bRequest == RQ_GET_SWITCH_BLUE) 
    {
	switch_state = IS_SWITCH_BLUE_PRESSED();
	usbMsgPtr = &switch_state;
	//_delay_ms(10);
	return 1;
		
    }

    /* default for not implemented requests: return no data back to host */
    return 0;
}

/* ------------------------------------------------------------------------- */
int main(void)
{
    init_peripheral();

    usbInit();

    /* enforce re-enumeration, do this while interrupts are disabled! */
    usbDeviceDisconnect();
    _delay_ms(300);
    usbDeviceConnect();

    /* enable global interrupts */
    sei();

    /* main event loop */
    for(;;)
    {
        usbPoll();
    }

    return 0;
}

/* ------------------------------------------------------------------------- */
