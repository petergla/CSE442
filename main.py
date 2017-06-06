import Tkinter as tk



class genStruc(tk.Tk):
	def popUp(self,cont):
		frame = self.frames[cont]
		frame.tkraise()

	def __init__(self, *args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.frames = {}
		frame = li_branch(container,self)
		self.frames[li_branch] = frame
		frame.grid(row = 0, column = 0, sticky = "nsew")
		self.popUp(li_branch)


class homePage(tk.Frame):

	def __init__ (self, par, controller):
		tk.Frame.__init__(self,par)
		label = tk.Label(self,text = "Start Page", font = ("Verdana", 12))
		label.pack(pady= 10, padx=10)

class li_branch(tk.Frame):
	def __init__ (self, par, controller):
		tk.Frame.__init__(self,par)	
		root = tk.Tk()
		frame1 = tk.Frame(root,width=300,height=300,bg="yellow")
		frame2 = tk.Frame(root,width=300,height=300,bg="green")

		label1 = tk.Label(root,text="The question")
		label2 = tk.Label(root,text="Assumption 1")
		label3 = tk.Label(root,text="Assumption 2")
		label4 = tk.Label(root,text="Assumption 3")
		label5 = tk.Label(root,text="Assumption 4")
		label6 = tk.Label(root,text="Current grade is ---")

		button1 = tk.Button(root,text="submit answer")

		check1 = tk.Checkbutton(root)
		check2 = tk.Checkbutton(root)
		check3 = tk.Checkbutton(root)
		check4 = tk.Checkbutton(root)

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

interface = genStruc()
interface.mainloop()
