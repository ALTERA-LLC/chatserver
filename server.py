import socket

class Main:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '192.168.0.69'
        self.sock.bind((self.ip, 2288))
        self.sock.listen(1)
        print('hello')
        self.whileloop()


    def whileloop(self):
        self.s, self.a = self.sock.accept()
        while True:
            mesg = self.s.recv(1024).decode('utf-8')
            print(f'Rory: {mesg}')

main = Main()
