import socket

class Main:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '58.160.92.128'
        self.sock.connect((self.ip, 2288))
        self.whileloop()


        print('hello')

    def whileloop(self):
        while True:
            h = input('msg:')
            print(f'You have sent sam: {h}')
            self.sock.send(h.encode())



main = Main()