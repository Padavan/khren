#!/usr/bin/env python

from Tkinter import *
import webbrowser
import time
import threading

class App(object):
    def __init__(self, root):
        self.root = root
#---------------------------------------------------------------------
        self.menu = Menu(self.root)
        filemenu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", underline=0, menu=filemenu)
        filemenu.add_command(label="Start", command=self.dummy)
        filemenu.add_command(label="Stop", command=self.dummy)
        filemenu.add_command(label="About", command=self.about)
        filemenu.add_command(label="Exit", underline=1, command=self.quit)
        helpmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help",menu=helpmenu)
        helpmenu.add_command(label="Donate")
        helpmenu.add_separator()
        helpmenu.add_command(label="About Khren", command=self.about)
        self.root.config(menu=self.menu)
#----------------------------------------------------------------------------
        self.timelabel=Label(root, text="00:00", font="Segoe 48")
        self.timelabel.pack()
        self.update_timer()

        separator = Frame(height=2, bd=4, relief=SUNKEN)
        separator.pack(fill=X, padx=0, pady=0)

        #TODO make only one button
        startButton = Button(root, text="Start",command=self.dummy,state=ACTIVE)
        stopButton = Button(root, text="Stop", command=self.dummy,state=DISABLED)
        startButton.pack()
        stopButton.pack()
#----------------------------------------------------------------------------


    def about(self):
        # TODO Make frame not window
        # TODO Make grid() geometry here
        window = Toplevel()
        window.title("About")
        window.minsize(400,400)
        window.maxsize(400,400)
        one=Frame(window)
        one.pack(fill=X, side=TOP)
        photo=PhotoImage(file='image/marisa.gif')
        icon = Label(one, width=80, height=80, image=photo)
        icon.photo=photo
        icon.pack(side=LEFT)
        msg = Label(one, text="Khren ver0.1").pack(pady=30,padx=30,side=LEFT)
        ok= Button(window, text="OK", command=window.destroy).pack(side=BOTTOM)
        two=Frame(window)
        two.pack(fill=X, side=TOP)
        homepage = Label(two, text="Home page:")
        homepage.pack(side=LEFT)
        url="https://github.com/Padavan/khren"
        homelink = Label(two, text=url, fg="blue")
        homelink.pack(padx=40,pady=5, side=LEFT)
        homelink.bind("<Button-1>",lambda aurl=url:self.openurl(url))

        group = LabelFrame(window, text="The MIT License", padx=5, pady=5)
        group.pack(padx=10, pady=10)
        scrollbar = Scrollbar(group)
        scrollbar.pack(side=RIGHT, fill=Y)
        f = open('COPYING', 'r')
        license=f.read()
        lic = Text(group, width=100, height=100, state=NORMAL, yscrollcommand=scrollbar.set)
        lic.pack(side=BOTTOM)
        lic.insert(END,license)
        lic.config(state=DISABLED)
        scrollbar.config(command=lic.yview)

    def update_timer(self):
        now = time.strftime("%M:%S")
        self.timelabel.configure(text=now)
        self.root.after(1000, self.update_timer)

    def dummy(self):
        print "dummy fun"

    def openurl(self, link):
        webbrowser.open(link)

    def quit(self):
        self.root.destroy()

class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.minutes=25
        self.count=self.minutes*60
    def start(self):
        self.count-=1
        self.event.wait(1)
    def stop(self):
        self.event.set()
    def dumb(self):
        return self.count

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()