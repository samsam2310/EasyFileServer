from Tkinter import *
 

class ServerGUI(Frame):
    def __init__(self, *a, **kw):
        self.master = Tk()
        self.master.resizable(height=False,width=False)
        kw['height'] = 300
        kw['width'] = 400
        Frame.__init__(self, self.master, *a, **kw)
        self.pack()
        self.setButton(self.master)

    def mainloop(self):
        self.master.mainloop()

    def setButton(self, master=None):
        self.start = Button(master)
        self.stop = Button(master)

        self.start['text'] = 'start'
        self.stop['text'] = 'stop'

        self.start.pack()
        self.stop.pack()

        self.start.place(height=50, width=100,x=70,y=230)
        self.stop.place(height=50, width=100,x=230,y=230)

    def setStart(self, start_fun):
        self.start['command'] = start_fun

    def setStop(self, stop_fun):
        self.stop['command'] = stop_fun
