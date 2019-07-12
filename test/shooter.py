import json
import socket
import pprint

"""
    adapt to micropythonar
"""

IP = "192.168.42.1"
PORT = 7878

class CamHandler(object):
    def __init__(self,ip,port):
        print("init")
        self.sock = socket.socket()
        self.sock.connect((ip,port))
        self.token = 0

    def _get_token(self):
        print("getting token")
        ti = '{"msg_id":257,"token":0,"heartbeat":1,"param":0}'
        self.sock.send(ti.encode())
        data = ""
        while True:
            data = self.sock.recv(10000)
            print("data: %s" %(data))
            res = json.loads(data)
            if res['msg_id'] == 257:
                self.token = res['param']
                print("TOKEN: %s" %(self.token))
                break
    
    def do_command(self,command):
        command['token'] = self.token
        self.sock.send(json.dumps(command).encode())
        #while True:
        #    res = json.loads(self.sock.recv(10000).decode())
        #    pprint.pprint(res)
        #    if res['msg_id'] == command['msg_id']:
        #        break


    def get_battery(self):
        command = {"msg_id":13}
        self.do_command(command)

    def take_picture(self):
        command = {"msg_id":16777220,"token":5,"param":"precise quality;off"}
        self.do_command(command)

    def start_recording(self):
        command = {"msg_id":513,"token":5}
        self.do_command(command)

    def stop_recording(self):
        command = {"msg_id":514,"token":5}
        self.do_command(command)

    def get_camera_params(self):
        command = {"msg_id":3,"token":5}
        self.do_command(command)

    def set_param(self, param, value):
        command = {"msg_id":2,
                   "type":param,
                   "param":value,
                   "token":1}
        self.do_command(command)

    def test(self):
        command = {"msg_id":260,"token":5}
        self.do_command(command) 

def main():
    ch = CamHandler(IP,PORT)
    ch._get_token()
    ch.get_camera_params()
    ch.take_picture()

if __name__ == '__main__':
    main() 