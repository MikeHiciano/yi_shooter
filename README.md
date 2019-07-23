# Yi Shooter

Yi shooter is an esp8266 powered remote control for a Yi Camera.

if you don`t have installed ampy on your computer or micropython on your microcontroller you can download and install it on the links down below.

[Micropython](https://micropython.org/)

[AMPY](https://github.com/pycampers/ampy)

For replicate this proyect there are two topics to do, the Hardware and the Software.


# Hardware

Coming Soon

# Software

## Set the credentials

The steps to insert the credentials are too simple, you only have to do is find this piece of code:

```python
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('<your SSID>','<your Password>')
```
the next you have to do is replace the "your ssid" space with your yi camera's wifi name and the "your password" space with your yi camera's password

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