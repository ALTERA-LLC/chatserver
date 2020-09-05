import socket
from multiprocessing import Process

class Main:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = 'localhost'
        self.sock.connect((self.ip, 8888))
        self.whileloop()


        print('hello')

    def whileloop(self):
        while True:
            h = input('msg:')
            print(f'You have sent sam: {h}')
            self.sock.send(h.encode())



    def recv(self):
        print('recv')
        print(self.sock.recv(1024).decode())

main = Main()