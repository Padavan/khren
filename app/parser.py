#!/usr/bin/env python

from Tkinter import *
import tkFont
from ttk import *


"""
class Parser():
    def __init__(self):
        pass
    def read(self):
        pass
    def write(self):
        pass
    def update(self):
        pass
"""

class App(object):
    def __init__(self, root):
        print "AboutWindows class initializated"
        self.makewidget()

    def makewidget(self):

        root.minsize(700,500)
        root.title("Preferences")
        title=Frame(root)
        title.pack(fill=X, side=TOP)
        photo=PhotoImage(file='image/marisa_small.gif')
        icon = Label(title,image=photo, width=80)
        icon.photo=photo
        icon.pack(side=LEFT)
        appHighlightFont = tkFont.Font(family='Helvetica', size=12, weight='bold')
        msg = Label(title, text="Preferences", font=appHighlightFont).pack(pady=30,padx=30,side=LEFT)
        separator = Frame(height=2, relief=SUNKEN)
        separator.pack(fill=X, padx=0, pady=0)


        tabs=Notebook(root)
        tabs.pack(fill=X)
        self.f1=Frame(tabs)
        f2=Frame(tabs)
        f3=Frame(tabs)
        tabs.add(self.f1, text="Timer")
        tabs.add(f2,text="Tasks")
        tabs.add(f3, text="Smth else")

        subt1 = Label(self.f1, text="Time").grid(row=0,pady=2, sticky=W)

        subsub1=Label(self.f1, text="Duration").grid(row=1, padx=50, sticky=W)
        self.scale1 = Scale(self.f1, from_=1, to=100,length=500)
        self.scale1.grid(row=2, padx=50, pady=5,sticky=W+E)
        self.scale1.set(25)
        self.valuedisplay1=Label(self.f1, text=self.scale1.get())
        self.valuedisplay1.grid(row=2, column=1, sticky=W)

        subsub2=Label(self.f1, text="Break").grid(row=3, padx=50, pady=5, sticky=W)
        self.scale2 = Scale(self.f1, from_=1, to=100,length=500)
        self.scale2.grid(row=4, padx=50,pady=5, sticky=W+E)
        self.scale2.set(5)
        self.valuedisplay2=Label(self.f1, text=self.scale2.get())
        self.valuedisplay2.grid(row=5, column=1, sticky=W)

        subsub3=Label(self.f1, text="Long Break").grid(row=6, padx=50, sticky=W)
        self.scale3 = Scale(self.f1, from_=1, to=100,length=500)
        self.scale3.grid(row=7, padx=50, pady=5, sticky=W+E)
        self.scale3.set(15)
        self.valuedisplay3=Label(self.f1, text=self.scale3.get())
        self.valuedisplay3.grid(row=8, column=1, sticky=W)

        self.update_values()



    def update_values(self):
        self.valuedisplay1.config(text=int(self.scale1.get()))
        self.valuedisplay2.config(text=int(self.scale2.get()))
        self.valuedisplay3.config(text=int(self.scale3.get()))
        self.f1.after(100, self.update_values)







root = Tk()

app = App(root)

root.mainloop()
#root.destroy()




