import socket

class Main:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = 'altera-server.ddns.net'
        self.sock.connect((self.ip, 2288))
        self.whileloop()


        print('hello')

    def whileloop(self):
        while True:
            print('Type "quit" to exit the program ')
            h = input('msg:')
            if h == 'quit':
                print('shutting down server')
                self.sock.send('quit'.encode('utf-8'))
                print('shutdown: goodbye :)')
                exit()
            else:
                print(f'You have sent sam: {h}')
                self.sock.send(h.encode('utf-8'))



main = Main()