from Tkinter import *

root = Tk()

imgPath = "RealWorld1.gif"  #file name 
photo = PhotoImage(file = imgPath) 
label = Label(image = photo)
label.image = photo # keep a reference!
label.grid(row = 3, column = 1, padx = 5, pady = 5)

root.mainloop()
