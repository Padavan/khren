#!/usr/bin/env python

from Tkinter import *
from ttk import *
import threading
from timer import Timer
from about import AboutWindow

class App(object):
    def __init__(self, root):
        s=Style()
        s.theme_use('clam')

        self.root = root
        self.root.title("Khren")

#---------------------------------------------------------------------
        self.menu = Menu(self.root)
        filemenu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", underline=0, menu=filemenu)
        filemenu.add_command(label="Start", command=self.dummy)
        filemenu.add_command(label="Stop", command=self.dummy)
        filemenu.add_command(label="Exit", underline=1, command=self.dummy)

        self.editmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label="Preference")

        helpmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help",menu=helpmenu)
        helpmenu.add_command(label="Donate")
        #helpmenu.add_separator()
        helpmenu.add_command(label="About Khren", command=self.aboutWindowInit)
        self.root.config(menu=self.menu)
#----------------------------------------------------------------------------
        self.tmr=Timer()
        self.timelabel=Label(root, text="00:00", font="Segoe 48")
        self.timelabel.pack()
        self.update_timer()


        separator = Frame(height=2, relief=SUNKEN)
        separator.pack(fill=X, padx=0, pady=0)

        #TODO make only one button
        self.startButton = Button(root, text="Start",command=self.toggle,state=ACTIVE)
        self.startButton.pack()

        self.timer=threading.Thread(target=self.tmr.start)
#----------------------------------------------------------------------------
    def toggle(self):
        if self.startButton["text"]=="Start":
            self.startButton.config(text="Stop")
            w=threading.Thread(target=self.tmr.start)
            w.start()
        else:
            self.startButton.config(text="Start")
            self.tmr.stop()


    def update_timer(self):
        now=self.tmr.dumb()
        #print "update", now
        now2="%02d:%02d" % divmod(now, 60)
        self.timelabel.configure(text=now2)
        self.root.after(1000, self.update_timer)

    def dummy(self):
        print "dummy fun"

    def quit(self):
        self.root.destroy()

    def aboutWindowInit(self):
        self.aboutWindow=AboutWindow()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()