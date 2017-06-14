from Tkinter import *        
from PIL import ImageTk, Image

app_root = Tk()
app_root.resizable(width=True, height=True)
#Setting it up

img = ImageTk.PhotoImage(Image.open("RealWorld.png"))
#Displaying it
imglabel = Label(app_root, image=img).grid(row=0, column=0)


app_root.mainloop()
