#!/usr/bin/env python

from Tkinter import *
import webbrowser

state = False	
ptime=25 #TODO preference to variate this shit
countdown=60*25
default=60*25

def test():
	print "Shit works"


def candytime(countdown):
	m,s=divmod(countdown, 60)
	return "%02d:%02d" %(m, s)
	
	
def tick():
	if state:
		global countdown
		countdown = countdown-1
		timelabel['text'] = candytime(countdown)
	root.after(1000, tick)

def start():
	global state
	state = True
	b.config(state=ACTIVE)
	a.config(state=DISABLED)
	
def stop():
	global state
	state = False
	a.config(state=ACTIVE)
	b.config(state=DISABLED)
	global countdown 
	countdown= default
	timelabel['text'] = candytime(countdown)
	
def openurl(link):
	webbrowser.open(link)

def helpwindow():
	top = Toplevel()
	top.title("About Khren...")
	top.minsize(400,400)
	top.maxsize(400,400)
#INFORMATION
	one=Frame(top)
	one.pack(fill=X, side=TOP)
	
	photo=PhotoImage(file='marisa.gif')
	icon = Label(one, width=80, height=80, image=photo)
	icon.photo=photo
	icon.pack(side=LEFT)
			
	msg = Label(one, text="Khren ver0.1")
	msg.pack(pady=30,padx=30,side=LEFT)
	
	ok= Button(top, text="OK", command=top.destroy)
	ok.pack(side=BOTTOM)
	
	#separator = Frame(top, height=2, bd=4, relief=SUNKEN)
	#separator.pack(fill=X, padx=0, pady=0)
	two=Frame(top)
	two.pack(fill=X, side=TOP)
	homepage = Label(two, text="Home page:")
	homepage.pack(side=LEFT)
	url="https://github.com/Padavan"
	homelink = Label(two, text=url)
	homelink.pack(side=LEFT)
	homelink.bind("<Button-1>",lambda aurl=url:openurl(url))
#KAWAII LICENSE	
	group = LabelFrame(top, text="The MIT License", padx=5, pady=5)
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
	
	
	
	
	
	
	
root=Tk()
menubar = Menu(root)

filemenu=Menu(root, tearoff=0)
filemenu.add_command(label="Start", command=start)
filemenu.add_command(label="Stop", command=stop)
menubar.add_cascade(label="File", menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Donate")
helpmenu.add_separator()
helpmenu.add_command(label="About Khren", command=helpwindow)
menubar.add_cascade(label="Help",menu=helpmenu)

timelabel=Label(root, text=candytime(countdown), font="Segoe 48")
timelabel.pack()

separator = Frame(height=2, bd=4, relief=SUNKEN)
separator.pack(fill=X, padx=0, pady=0)

#TODO make only one button
a = Button(root, text="Start",command=start,state=ACTIVE)
b = Button(root, text="Stop", command=stop,state=DISABLED)
a.pack()
b.pack()

######About###


##
tick()
root.title("Khren")
root.config(menu=menubar)
root.minsize(300, 300)
root.geometry("300x300")
root.iconbitmap('madskilz.ico')

root.mainloop()
root.destroy()