# 21/12/01:
- After wasting most part of yesterday and today trying to fix the mitosis layout to the way I wanted, it still does not work.
- But at least I got some ideas of how I want my keyboard to look with the same 42 keys. ![[Mitosis-modify.svg]]
- Starting from scratch now using https://github.com/ruiqimao/keyboard-pcb-guide
 - Board selection seems like a hard job:
 	-  The EFR32BG22 thunderboard for the main controller, since it got enough sensors and BLE built in. [Board schematic](https://www.silabs.com/documents/public/schematic-files/BRD4184A-A01-schematic.pdf) But sadly it does not have enough GPIO ports, only 16 pins usable really, so that's not going to work
	 - The [teensy 4.1](https://www.sparkfun.com/products/16771) seems to have enough pins, but also consume a lot of power 100ma, running a cortex m7, that is a lot of power I doubt I will need that for a keyboard. This probably not going to work for a wireless keyboard. 
	 - ESP got a lot of really nice devkits with plenty of GPIO, with somewhat reasonable power consumption levels. The [ESP32 PICO kit](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-pico-kit.html) is looking like the most promising chip right now, but still a lot of power consumption for typical BLE operations.
	 - I don't know why I wasted so much time thinking about this, just straight up use the recommend [chip](https://www.waveshare.com/core51822-b.htm) and be done with it. They also make a version of it for NRF52840
	 - And now I have found https://github.com/foostan/crkbd this should be the closest I need to a working keyboard

# 21/12/02
Okay this is stupid I am just going to go with Lily58 pro	 

And now there is also this [Nice!Nano](https://docs.nicekeyboards.com/#/nice!nano/) thing that I can eventually replace for wireless connection.