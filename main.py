#!/usr/bin/env python
from Tkinter import *
import sys
class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)
        fileMenu.add_command(label="About", command=About.shit)
    def quit(self):
        sys.exit(0)

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

class About():
    def __init__(self):
        #Toplevel.__init__(self)
        pass
    def shit():
        top = Toplevel()
        top.title("About Khren...")
        top.minsize(400,400)
        top.maxsize(400,400)
        one=Frame(top)
        one.pack(fill=X, side=TOP)

if __name__ == "__main__":
    app=App()
    app.mainloop()

