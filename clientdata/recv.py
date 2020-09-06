class recv:
    def __init__(self):
        print('hello')

    def init(self, sock=None):
        self.sock = sock

    def recieving(self):
        while True:
            print('hello')