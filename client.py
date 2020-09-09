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
        self.listbox = Listbox(self.root, font=('Consolas', 15, 'bold'), bg='black', fg='white', width=54)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.geometry('600x400')
        threading.Thread(target=self.join).start()

    def exit(self):
        self.exiting = True
        print('you have closed the connection')
        self.sock.close()
        exit()

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
        Label(text='ALTERA CHAT CLIENT V.1.0', font=('Consolas', 15, 'bold'), bg='black', fg='white').place(x=0, y=0)
        self.listbox.place(x=0, y=50)
        self.root.bind('<Return>', func=self.sendmsg)
        self.entry()

    def entry(self):
        Label(self.root, bg='black', fg='white', text='Messsge:', font=('Consolas', 15, 'bold')).place(x=0, y=320)
        self.hello = Text(self.root, bg='black', fg='white', height=1, font=('Consolas', 15, 'bold'),
                          insertbackground='white', bd=3)
        self.hello.place(x=0, y=369)

    def sendmsg(self, event):
        if not self.exiting:
            self.sock.send(str(self.hello.get("1.0", 'end-1c')).encode('utf-8'))
            self.entry()
        else:
            exit()

    def initrecv(self):
        for msg in self.sock.recv(1024).decode('utf-8'):
            self.listbox.insert(END, msg)

    def recv(self):
        self.running = True
        while self.running:
            try:
                hello = self.sock.recv(1024).decode('utf-8')
                print(hello)
                self.listbox.insert(END, hello)
            except:
                if not self.exiting:
                    print('error: server connection lost')
                    threading.Thread(target=self.join).start()
                    self.running = False
                else:
                    self.running = False




mainmf = Main()
mainmf.root.mainloop()

