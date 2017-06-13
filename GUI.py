# import Tkinter as tk
from Tkinter import *

# Author: Paata Ugrekhelidze
# The program contains one class(genStruc) that puts all
# the pages together and links them the way they were defined to.
# All the other classes represent page definitions that genStruc uses.

class genStruc(Tk):
	

	def __init__(self, *args,**kwargs):
		Tk.__init__(self,*args,**kwargs)
		# creating a frame
		container = Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# frames will be a dictionary of the classes that contain pages
		self.frames = {}
		for fs in (homepage,questionpage):
			frame = fs(container,self)
			self.frames[fs] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")
		self.popUp(homepage)
	# Void function that hinders the previous page and brings up the given page
	# that is passed in (cont)
	def popUp(self,cont):
		frame = self.frames[cont]
		frame.tkraise()
# Startup Page
class homepage(Frame):

	def __init__ (self, par, controller):
		Frame.__init__(self,par)

		# basic tkinter library definitions of page creation
		can = Canvas(self,width=400, height=400)
		can.pack()

		line = can.create_line(100,100,100,175,fill="#005bbb")
		line = can.create_line(100,175,125,200,fill="#005bbb")
		line = can.create_line(125,200,175,200,fill="#005bbb")
		line = can.create_line(175,200,200,175,fill="#005bbb")
		line = can.create_line(200,175,200,100,fill="#005bbb")
		line = can.create_line(150,150,150,250,fill="#005bbb")
		line = can.create_line(150,150,240,150,fill="#005bbb")
		line = can.create_line(240,150,250,160,fill="#005bbb")
		line = can.create_line(250,160,250,190,fill="#005bbb")
		line = can.create_line(250,190,240,200,fill="#005bbb")
		line = can.create_line(240,200,175,200,fill="#005bbb")
		line = can.create_line(240,200,250,210,fill="#005bbb")
		line = can.create_line(250,210,250,240,fill="#005bbb")
		line = can.create_line(250,240,240,250,fill="#005bbb")
		line = can.create_line(240,250,150,250,fill="#005bbb")

		button = Button(self,text="Question Page", command = lambda: controller.popUp(questionpage))
		button.pack(side=RIGHT)
		

# Page were questions will be distributed
class questionpage(Frame):
	def __init__ (self, par, controller):
		Frame.__init__(self,par)	
		# Self exlanatory Page definitions
		frame1 = Frame(self,width=300,height=300,bg="yellow")
		frame2 = Frame(self,width=300,height=300,bg="green")

		label1 = Label(self,text="The question")
		label2 = Label(self,text="Assumption 1")
		label3 = Label(self,text="Assumption 2")
		label4 = Label(self,text="Assumption 3")
		label5 = Label(self,text="Assumption 4")
		label6 = Label(self,text="Current grade is ---")

		button1 = Button(self,text="submit answer")

		check1 = Checkbutton(self)
		check2 = Checkbutton(self)
		check3 = Checkbutton(self)
		check4 = Checkbutton(self)

		frame1.grid(row=0,column=0)
		frame2.grid(row=0,column=1)
		label1.grid(row=1,column=0,sticky="W")
		check1.grid(row=2,column=0,sticky="W")
		check2.grid(row=3,column=0,sticky="W")
		check3.grid(row=4,column=0,sticky="W")
		check4.grid(row=5,column=0,sticky="W")
		label2.grid(row=2,column=0,sticky="E")
		label3.grid(row=3,column=0,sticky="E")
		label4.grid(row=4,column=0,sticky="E")
		label5.grid(row=5,column=0,sticky="E")

		button1.grid(row=6,column=1,sticky="E")
		label6.grid(row=7,column=0,sticky="W")
		button3 = Button(self,text="Home Page", command = lambda: controller.popUp(homepage))
		button3.grid(row = 6, column = 1, sticky = "W")

# initializing and running an infinite loop on genStruc until
# the frame is shut down
interface = genStruc()
interface.mainloop()
