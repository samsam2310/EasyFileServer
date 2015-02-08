# -*- coding: utf-8 -*-
import os
import sys
import ScrolledText
import tkMessageBox
import tkFileDialog
import time

from Tkinter import *
 

class RedirectText(object):
    def __init__(self, text_ctrl):
        self.output = text_ctrl

    def write(self, string):
        self.output.insert(END, string)


class ServerGUI(Frame):
    def __init__(self, start_fun, stop_fun, set_file_path, app, *a, **kw):
        self.start_fun = start_fun
        self.stop_fun = stop_fun
        self.set_file_path = set_file_path
        self.app = app
        self.SERVERRUNNING = False
        
        self.master = Tk()
        self.master.resizable(height=False,width=False)
        self.master.title("INFOR 27th - EasyFileServer Console")
        self.master.protocol("WM_DELETE_WINDOW", self.quit)
        self.master.iconbitmap('icon.ico')
        Frame.__init__(self, self.master, *a, **kw)
        self.center(600,500)
        self.pack()
        
        self.setButton(self.master)
        self.setTerminal(self.master)

    def mainloop(self):
        if self.listen():
            self.master.mainloop()

    def center(self,width,height):
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def setButton(self, master=None):
        self.ctrlbtn = Button(master)
        self.ctrlbtn['text'] = 'Start Server'
        self.ctrlbtn['command'] = self.start_server
        self.ctrlbtn.pack()
        self.ctrlbtn.place(height=50, width=160,x=60,y=430)

        self.changebtn = Button(master)
        self.changebtn['text'] = 'Change path'
        self.changebtn['command'] = self.change_file_path
        self.changebtn.pack()
        self.changebtn.place(height=50, width=160,x=260,y=430)

        self.readmebtn = Button(master)
        self.readmebtn['text'] = 'Read Me'
        self.readmebtn['command'] = self.readme
        self.readmebtn.pack()
        self.readmebtn.place(height=25, width=80,x=460,y=430)

        self.aboutbtn = Button(master)
        self.aboutbtn['text'] = 'About'
        self.aboutbtn['command'] = self.about
        self.aboutbtn.pack()
        self.aboutbtn.place(height=25, width=80,x=460,y=455)

    def start_server(self):
        self.SERVERRUNNING = True
        self.changebtn['state'] = 'disabled'
        self.ctrlbtn['text'] = 'Loading...'
        self.ctrlbtn['state'] = 'disabled'
        self.start_fun()
        self.ctrlbtn['text'] = 'Stop Server'
        self.ctrlbtn['state'] = 'active'
        self.ctrlbtn['command'] = self.stop_server
        self.master.title("INFOR 27th - EasyFileServer Console - Server Running")

    def stop_server(self):
        self.ctrlbtn['text'] = 'Loading...'
        self.ctrlbtn['state'] = 'disabled'
        self.stop_fun()
        self.ctrlbtn['text'] = 'Start Server'
        self.ctrlbtn['state'] = 'active'
        self.ctrlbtn['command'] = self.start_server
        self.SERVERRUNNING = False
        self.changebtn['state'] = 'active'
        self.master.title("INFOR 27th - EasyFileServer Console")

    def setTerminal(self, master):
        self.text = ScrolledText.ScrolledText(master)
        self.text.pack()
        self.text.place(height=400, width=580,x=10,y=10)

        redir = RedirectText(self.text)
        sys.stdout = redir

    def quit(self):
        if tkMessageBox.askokcancel("Quit?", "Are you sure you want to quit?"):
            if self.SERVERRUNNING:
                self.stop_fun()
            self.master.quit()

    def listen(self):
        try:
            self.app.listen(8888)
        except:
            tkMessageBox.showerror('Error! Port 8888 already in use!',
                'Pleace don\'t run more then one EasyFileServer at the same time, or check there is no program occupies port 8888.')
            return False
        return True

    def change_file_path(self):
        path = tkFileDialog.askdirectory(mustexist=True)
        if path and os.path.exists(path):
            self.set_file_path(path)
            print('Change file path to "%s"' % path)

    def readme(self):
        with open('readme.txt','r') as f:
            message = f.read()
            tkMessageBox.showinfo('Read Me', message)

    def about(self):
        message = \
"""
Hi!
因為累了所以我要用中文寫!!!
會寫這個都是因為一時興起，沒想到竟然寫出了這麼複雜的東西，也學到很多~~~。
感謝支援(TMD)Windows的Tornado和nginx，雖然因為big5和utf-8出了很多問題。

github: https://github.com/samsam2310/EasyFileServer

by INFOR 27th 果茶
"""
        tkMessageBox.showinfo('About', message)
