from Tkinter import *
import webbrowser

class AboutWindow(object):
    def __init__(self):
        object.__init__(self)
        print "AboutWindows class initializated"
        self.makewidget()
    def makewidget(self):
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
    def openurl(self, link):
        webbrowser.open(link)