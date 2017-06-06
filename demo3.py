from Tkinter import *

root = Tk()

frame1 = Frame(root,width=300,height=300,bg="#005bbb")
frame2 = Frame(root,width=300,height=300,bg="green")

label1 = Label(root,text="The question")
label2 = Label(root,text="Assumption 1")
label3 = Label(root,text="Assumption 2")
label4 = Label(root,text="Assumption 3")
label5 = Label(root,text="Assumption 4")
label6 = Label(root,text="Current grade is ---")

button1 = Button(root,text="submit answer")

check1 = Checkbutton(root)
check2 = Checkbutton(root)
check3 = Checkbutton(root)
check4 = Checkbutton(root)

frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
label1.grid(row=1,column=0,sticky=W)
check1.grid(row=2,column=0,sticky=W)
check2.grid(row=3,column=0,sticky=W)
check3.grid(row=4,column=0,sticky=W)
check4.grid(row=5,column=0,sticky=W)
label2.grid(row=2,column=0,sticky=E)
label3.grid(row=3,column=0,sticky=E)
label4.grid(row=4,column=0,sticky=E)
label5.grid(row=5,column=0,sticky=E)

button1.grid(row=6,column=1,sticky=E)
label6.grid(row=7,column=0,sticky=W)

root.mainloop()

#as a  student, I want to get a good grade, so I 
