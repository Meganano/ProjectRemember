MCU=atmega168
F_CPU=16000000
CFLAGS=-mmcu=$(MCU) -DF_CPU=$(F_CPU) -O


.SECONDARY:

all: *.hex

%.flash: %.hex
	avrdude -p $(MCU) -c usbasp -u -U flash:w:$<

%.hex: %.elf
	avr-objcopy -j .text -j .data -O ihex $< $@

%.elf: %.o $(OBJS)
	avr-gcc $(CFLAGS) -o $@ $^

%.o: %.c
	avr-gcc $(CFLAGS) -c -o $@ $<

clean:
	rm -f *~
	rm -f *.o
	rm -f *.elf
	rm -f *.hex
	rm -f $(OBJS)
	rm -f $(TARGET)
