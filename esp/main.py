import gc
import time
import network
import machine
from machine import Pin
import usocket as socket
import ujson as json

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('<your SSID>','<your Password>')

IP = "192.168.42.1"
PORT = 7878

picture_button = Pin(5,Pin.IN, Pin.PULL_UP)
video_button = Pin(4,Pin.IN, Pin.PULL_UP)
led = Pin(16,Pin.OUT)
status_led = Pin(2,Pin.OUT)

class CamHandler(object):
    def __init__(self,ip,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.token = 0
    
    def _get_token(self):
        self.sock.send('{"msg_id":257,"token":0,"heartbeat":1,"param":0}')
        data = ""
        while True:
            res = json.loads(self.sock.recv(10000))
            if res['msg_id'] == 257:
                self.token = res['param']
                break
    
    def do_command(self,command):
        command['token'] = self.token
        self.sock.send(json.dumps(command))

    def take_picture(self):
        command = {"msg_id":16777220,"token":5,"param":"precise quality;off"}
        self.do_command(command)
    
    def start_recording(self):
        command = {"msg_id":513,"token":5}
        self.do_command(command)

    def stop_recording(self):
        command = {"msg_id":514,"token":5}
        self.do_command(command)

    def cl ose_connection(self):
        self.sock.close()

def main():

    ch = CamHandler(IP,PORT)

    if sta_if.ifconfig()[3] == "192.168.42.1":
        status_led.value(0)
    
    elif sta_if.ifconfig()[3] != "192.168.42.1":
        status_led.value(1)

    if picture_button.value() != False or video_button.value() != False:
        gc.enable()
        gc.collect()

    if picture_button.value() == False:
        led.value(0)
        ch._get_token()
        ch.take_picture()
        led.value(1)

'''
    elif video_button.value() == False:
        
        if == False:
            led.value(0)
            ch._get_token()
            ch.start_recording()
            led.value(1)
        
        else:
            led.value(0)
            ch._get_token()
            ch.stop_recording()
            led.value(1)
'''

def blink():
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)

while True:
    try:
        main()
        time.sleep(0.2)

    except OSError:
        status_led.value(0)
        blink()
