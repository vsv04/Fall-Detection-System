# Parts and Schematics for Fall Detection System

The following components are required for the fall detection system.

## Raspberry Pi 4
The fall detection system uses a [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/).  A minimum RAM of 2 GB of memory is required to implement deep learning. <br/>
![](https://github.com/vsv04/Fall-Detection-System/blob/master/PARTS%20%26%20SCHEMATICS/Images/Raspberry%20Pi%204.jpg)<br/>
The Raspberry Pi 4 board can be purchased from [CanaKit](https://www.canakit.com/raspberry-pi-4-2gb.html). You can also purchase a [complete starter kit](https://www.canakit.com/raspberry-pi-4-complete-starter-kit-official-case.html) that comes with a Rasperyy Pi 4, case, power supply, keyboard, mouse and SD card. 

## FLIR Lepton Thermal Camera
The [FLIR Lepton](https://www.flir.com/products/lepton/?model=500-0763-01) thermal camera has a 80x60 pixel resolution with a 50° field of view. <br/>
![](https://github.com/vsv04/Fall-Detection-System/blob/master/PARTS%20%26%20SCHEMATICS/Images/FLIR%20Lepton.jpg)<br/>
The FLIR Lepton 2.5 with development board can be purchased from [Sparkfun](https://www.sparkfun.com/products/15948). Alternatively, the [camera module](https://www.digikey.com/products/en?FV=-5|79760) and [development board](https://www.digikey.com/product-detail/en/flir-lepton/250-0577-00/1577-250-0577-00-ND/10385179) can be purchase separately through Digi-Key. 

## Additional components
[Jumper wires](https://www.adafruit.com/product/266) to connect the FLIR Lepton Thermal Camera to the Raspberry Pi. 

[RGB (tri-color) LED](https://www.adafruit.com/product/159) to indicate the status of the fall detection system (Optional)

## Connecting the FLIR Lepton to the Raspberry Pi
The FLIR Lepton breakout board pins are connected to the GPIO pins on the Raspberry Pi using jumper wires. A GPIO pinout diagram is available at [pinout.xyz] https://pinout.xyz/. </br>
```
CS -> Pin 24, CE0
MOSI -> Pin 19, MOSI
MISO -> Pin 21, MISO
CLK -> Pin 23, CLK
GND -> Pin 6, GND
VIN -> Pin 1, 3V3
SDA -> Pin 3, SDA
SCL -> Pin 5, SCL
```

