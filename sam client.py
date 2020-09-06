import socket
import threading
from clientdata import recv, send

class Main:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '58.160.92.128'
        self.sock.connect((self.ip, 2288))
        recv.recv.init(sock=self.sock, self=self)
        threading.Thread(target=recv.recv.recieving).start()








main = Main()