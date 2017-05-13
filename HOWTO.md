# Build your own DISTRACTINATOR: The customizable, open source cubicle doorbell #

## Hardware Ingredients for 1 (one) Distractinator ##

* Arduino Nano w/ATmega 328 (or comparable)
* RF M4 Receiver - 315 MHz [https://www.adafruit.com/product/1096]
* 4-Button RF remote control [https://www.adafruit.com/product/1095]
* USB cable (to connect microcontroller -> computer)
* Some manner of container (project box, small tin, etc.)

## Software Ingredients for 1 (one) Distractinator ##

* notify.ino sketch (can be found in distractinator/examples)
* Arduino IDE (to flash microcontroller with notify.ino sketch)
* This repository (`pip install distractinator`)

# THE METHOD #

Readying the Distractinator consists of 3 (three) main steps:
	
1.) Obtain the ingredients

2.) Build the hardware

3.) Configure the device

## 1.) Obtain the ingredients ##

### Hardware ###

Acquire the requisite hardware!

### Software (I assume you're running Linux) ###

* Install distractinator (see README.md)
* Install Arduino if you don't have it already [https://code.launchpad.net/ubuntu/+source/arduino]
	* On Ubuntu: `sudo apt install arduino` 

## 2.) Build the Hardware ##

Connect the Arduino pins to the M4 Receiver:

**Power**:

* Arduino GND -> M4 GND
* Arduino 5V -> M4 5V

**Data**:

* Arduino Pin D12 -> M4 Pin D3 ("A" button)
* Arduino Pin D6  -> M4 Pin D2 ("B" button)
* Arduino Pin D9  -> M4 Pin D1 ("C" button)
* Arduino Pin D10 -> M4 Pin D0 ("D" button)

Solder or otherwise secure the connections.

Flash the microcontroller with the sketch:

* Connect the Arduino to your computer via USB
* Open the Arduino IDE and open the notify.ino sketch (in distractinator/examples)
* Select the correct board from **Tools > Board**
* Click **Upload**

Fit these two boards into your container.

## 3.) Configure the device ##

Connect your newly-built Distractinator to your computer. 

Run `distractinator`. 

The installation wizard will guide you from there.

Enjoy!

