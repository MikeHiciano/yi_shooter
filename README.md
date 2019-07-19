# Yi Shooter

Yi shooter is an esp8266 powered remote control for a Yi Camera.

if you dont have installed ampy in your computer or micropython in your microcontroller you can download and install it on the links down below.

[Micropython](https://micropython.org/)

[AMPY](https://github.com/pycampers/ampy)

For replicate this proyect there are two topics to do, the Hardware and the Software.


# Hardware

Coming Soon

# Software

## Set the credentials

Comming soon

## instalation
The steps to do the instalation for the software are the next ones:

* Connect the esp8266 to the pc 
    [insert photo]
* open the terminal
* Giving permission to the port, in my case the port /dev/ttyUSB0 
```
    sudo chmod 666 /dev/ttyUSB0
```
* After that we going to go to the esp directory
```
    cd /yi_shooter/esp
```
* Being in the directory ESP you have to type in the terminal the next command to copy the main.py file to the microcontroller
```
    ampy --port /dev/ttyUSB0 put main.py
```
* To test the program you only have to do is type in the terminal the next command
```
    ampy --port /dev/ttyUSB0 run main.py
```
and thats it, you only have to restart the board