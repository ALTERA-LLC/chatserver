from tkinter import *
import socket
import threading
import os
from time import sleep


class Main:
    def __init__(self):
        self.root = Tk()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = input('name:')
        self.root.config(bg='black')
        self.root.resizable(0, 0)
        self.exiting = False
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.geometry('600x400')
        threading.Thread(target=self.join).start()

    def exit(self):
        self.exiting = True
        print('you have closed the connection')
        self.sock.close()
        sys.exit()

    def join(self):
        conlabel = Label(text='Connecting', font=('Consolas', 15, 'bold'), bg='black', fg='white')
        conlabel.pack(side=TOP)
        try:
            self.sock.connect(('altera-server.ddns.net', 2288))
            self.sock.send(self.name.encode('utf-8'))
        except:
            print("error couldn't connect to server\nretrying in 2 seconds")
            sleep(2)
            conlabel.destroy()
            print('retrying')
            self.join()
        finally:
            sleep(3)
            conlabel.place(x=1000, y=1000)
            print('connected to server')
            conlabel = Label(text='Connected to server', font=('Consolas', 15, 'bold'), bg='black', fg='white')
            conlabel.pack(side=TOP)
            self.initbild()
            sleep(2)
            conlabel.destroy()
            threading.Thread(target=self.recv).start()


    def initbild(self):
        self.root.bind('<Return>', func=self.sendmsg)
        self.entry()

    def entry(self):
        Label(self.root, bg='black', fg='white', text='Messsge:', font=('Consolas', 15, 'bold')).place(x=0, y=320)
        self.hello = Text(self.root, bg='black', fg='white', height=2, font=('Consolas', 15, 'bold'))
        self.hello.place(x=0, y=350)

    def sendmsg(self, event):
        self.sock.send(str(self.hello.get("1.0", 'end-1c')).encode('utf-8'))
        self.entry()

    def recv(self):
        self.running = True
        while self.running:
            try:
                print(self.sock.recv(1024).decode('utf-8'))
            except:
                if not self.exiting:
                    print('error: server connection lost')
                    self.join()
                    self.running = False
                else:
                    self.running = False




mainmf = Main()
mainmf.root.mainloop()

