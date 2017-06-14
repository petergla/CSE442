#gifdir = "./"
from sys import argv
from Tkinter import *

def fun1():
    print(checkboxstatus1.get())
    print(checkboxstatus2.get())
    print(checkboxstatus3.get())
    print(checkboxstatus4.get())
    print

root = Tk()

frame1 = Frame(root,width=200,height=200,bg="#005bbb")
frame1.grid(row=0,column=0)
frame2 = Frame(root,width=200,height=200,bg="green")
frame2.grid(row=0,column=1)
frame3 = Frame(root,width=200,height=200,bg="red")
frame3.grid(row=0,column=2)



label1 = Label(root,text="The question")
label6 = Label(root,text="Current grade is ---")

button1 = Button(root,text="submit answer",command=fun1)

checkboxstatus1 = IntVar()
checkboxstatus2 = IntVar()
checkboxstatus3 = IntVar()
checkboxstatus4 = IntVar()

check1 = Checkbutton(root, text="Assumption 1", variable=checkboxstatus1)
check2 = Checkbutton(root, text="Assumption 2", variable=checkboxstatus2)
check3 = Checkbutton(root, text="Assumption 3", variable=checkboxstatus3)
check4 = Checkbutton(root, text="Assumption 4", variable=checkboxstatus4)


label1.grid(row=1,column=0,sticky=W)
check1.grid(row=2,column=0,sticky=W)
check2.grid(row=3,column=0,sticky=W)
check3.grid(row=4,column=0,sticky=W)
check4.grid(row=5,column=0,sticky=W)
button1.grid(row=6,column=2,sticky=E)
label6.grid(row=7,column=0,sticky=W)

filename = 'demo.gif' 
img = PhotoImage(file=filename)
#img = PhotoImage(file=gifdir+filename)
can = Canvas(root)
can.grid(row=8,column=0,sticky=W)
can.config(width=img.width(), height=img.height())
can.create_image(2, 2, image=img, anchor=NW)


root.mainloop()
