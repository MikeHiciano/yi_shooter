import gc
import time
import network
import machine
from machine import Pin
import usocket as socket
import ujson as json

gc.enable()
flag = 1
IP = "192.168.42.1"
PORT = 7878

sta_if = network.WLAN(network.STA_IF)
sta_if.connect('Yi_MikeHiciano','mikeishere')

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
    
    def close_connection(self):
        self.sock.close()

def main():
    button = Pin(5,Pin.IN, Pin.PULL_UP)
    led = Pin(16,Pin.OUT)
    ch = CamHandler(IP,PORT)

    while True:
        if button.value() == False:
            led.value(0)
            ch._get_token()
            ch.take_picture()
            led.value(1)
    
        else:
            gc.collect()

if __name__ == '__main__':
    
    main()





