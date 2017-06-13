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
		frame = homePage(container,self)
		self.frames[homePage] = frame
		frame.grid(row = 0, column = 0, sticky = "nsew")
		self.popUp(homePage)


class homePage(tk.Frame):

	def __init__ (self, par, controller):
		tk.Frame.__init__(self,par)
		label = tk.Label(self,text = "Start Page", font = ("Verdana", 12))
		label.pack(pady= 10, padx=10)



interface = genStruc()
interface.mainloop()
