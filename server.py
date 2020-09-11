import socket
import threading


class Main:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.nicks = []
        self.msghistory = []
        try:
            self.sock.bind(('192.168.0.69', 2288))
        except:
            self.sock.bind(('localhost', 2288))
        finally:
            self.sock.listen(1)
            self.handle()

    def users(self, user):
        self.clients.append(self.s)
        self.nicks.append(user)
        self.index = str(len(self.clients) - 1)
        print(self.clients)
        print(self.nicks)

    def joinnexit(self, message, nickname):
        if len(self.clients) == 0:
            return 'no one is connected to server'
        else:
            self.brodcast(message, nickname)
            print(f'{nickname} {message}')

    def brodcast(self, message, nickname, index=None):
        for clinet in self.clients:
            clinet
            clinet.send(f'{nickname} {message}'.encode('utf-8'))
            self.msghistory.append(f'{nickname}: {message}')

    def handle(self):
        while True:
            self.s, self.a = self.sock.accept()
            nick = self.s.recv(1024).decode('utf-8')
            self.users(nick)
            self.s.send(self.index.encode('uft-8'))
            print(self.joinnexit('joined the chat', nick))
            le = threading.Thread(target=self.recv, args=(self.index))
            le.start()

    def recv(self, index):
        running = True
        client = self.clients[int(index)]
        nick = self.nicks[int(index)]
        while running:
            try:
                msg = client.recv(1024).decode('utf-8')
                print(msg)
                self.brodcast(msg, self.nicks[int(index)] + ':', index)
                print(index)
            except:
                self.clients.remove(client)
                self.nicks.remove(nick)
                self.joinnexit('left the chat', nick)
                client.close()
                running = False
        print(f'{nick}: Thread has stopped')



main = Main()
