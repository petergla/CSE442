gifdir = "./"
from Tkinter import *

def resizephotoimagewithin1000pixel(img):
    while (img.height()>1000 or img.width()>1000):
        # subsample(self, x, y='')
        # Return a new PhotoImage based on the same image as this widget but use only every Xth or Yth pixel.
        img = img.subsample(2,2)
    return img

def submisson(frame,labelg,checkboxstatus1,checkboxstatus2,checkboxstatus3,checkboxstatus4,assumpttion1,assumpttion2,assumpttion3,assumpttion4,radiobutton1,radiobutton2,radiobutton3,radiobutton4,radiobutton5,radiobutton6,radiobutton7):
    answer_key = [0,0,1,1]
    answers = [checkboxstatus1.get(),checkboxstatus2.get(),checkboxstatus3.get(),checkboxstatus4.get()]
    score = 0.0
    for i in range(len(answer_key)):
        if answer_key[i] == answers[i]:
            score = score+1
    labelg.config(text='Current Grade is '+str(score))
    if answers[0] == 1:
        if answer_key[0] != answers[0]:
            assumpttion1.config(fg='red')
            radiobutton1.grid(row=2,column=0,padx=25,sticky='W')
            radiobutton2.grid(row=3,column=0,padx=25,sticky='W')
            radiobutton3.grid(row=4,column=0,padx=25,sticky='W')
    if answers[1] == 1:
        if answer_key[1] != answers[1]:
            assumpttion2.config(fg='red')
            radiobutton4.grid(row=6,column=0,padx=25,sticky='W')
            radiobutton5.grid(row=7,column=0,padx=25,sticky='W')
            radiobutton6.grid(row=8,column=0,padx=25,sticky='W')
            radiobutton7.grid(row=9,column=0,padx=25,sticky='W')
    if answers[2] == 1:
        if answer_key[2] == answers[2]:
            assumpttion3.config(fg='green')
    if answers[3] == 1:
        if answer_key[3] == answers[3]:
            assumpttion4.config(fg='green')
root = Tk()

# image1
fil1 = 'RealWorld_1.gif'
img1 = PhotoImage(file=gifdir+fil1)
scl1 = resizephotoimagewithin1000pixel(img1)

# image2
fil2 = 'IdealizedModel1_1.gif'
img2 = PhotoImage(file=gifdir+fil2)
scl2 = resizephotoimagewithin1000pixel(img2)

# canvas
# holds image1 and image2
# 10 pixels around image
can = Canvas(root,width=scl1.width()+scl2.width()+30,height=max(scl1.height(),scl2.height())+20)
can.create_image(10,             10+50,image=scl1,anchor=NW)
can.create_image(20+scl1.width(),10+50,image=scl2,anchor=NW)
can.pack()

# grade label
labelg = Label(root,text="Current Grade is ---",font="Helvetica 36 bold",fg='black')
labelg.place(x=0,y=0)

# frame
# width = image1 + image 2
frame = Frame(root,width=(scl1.width()+scl2.width())/2,height=100)
frame.pack()

# problem label
labelq = Label(frame,text="Please select the correct assumptions:",font="Helvetica 16 bold").grid(row=0,column=0,sticky=W)

# checkboxes and radiobuttons
checkboxstatus1 = IntVar()
checkboxstatus2 = IntVar()
checkboxstatus3 = IntVar()
checkboxstatus4 = IntVar()
reasonselection1 = IntVar()
reasonselection2 = IntVar()
assumpttion1 = Checkbutton(frame, text="Hip acts as a pivot point (no lifting off the bed)",variable=checkboxstatus1)
assumpttion2 = Checkbutton(frame, text="Lower leg remains approximately perpendicular to upper leg",variable=checkboxstatus2)
assumpttion3 = Checkbutton(frame, text="Forces are reasonably approximated using static analysis",variable=checkboxstatus3)
assumpttion4 = Checkbutton(frame, text="Patient does not slide on the bed",variable=checkboxstatus4)
assumpttion1.grid(row=1, column=0,sticky=W)
assumpttion2.grid(row=5, column=0,sticky=W)
assumpttion3.grid(row=10,column=0,sticky=W)
assumpttion4.grid(row=11,column=0,sticky=W)
radiobutton1 = Radiobutton(frame,text="Valid Reason #1.1.1",   variable=reasonselection1,value=1)
radiobutton2 = Radiobutton(frame,text="Invalid Reason #1.1.2", variable=reasonselection1,value=2)
radiobutton3 = Radiobutton(frame,text="Invalid Reason #1.1.3", variable=reasonselection1,value=3)
radiobutton4 = Radiobutton(frame,text="Invalid Reason #1.2.1", variable=reasonselection2,value=4)
radiobutton5 = Radiobutton(frame,text="Invalid Reason #1.2.2", variable=reasonselection2,value=5)
radiobutton6 = Radiobutton(frame,text="Invalid Reason #1.2.3", variable=reasonselection2,value=6)
radiobutton7 = Radiobutton(frame,text="Valid Reason #1.2.4",   variable=reasonselection2,value=7)
radiobutton1.grid(row=2,column=0,sticky=W)
radiobutton2.grid(row=3,column=0,sticky=W)
radiobutton3.grid(row=4,column=0,sticky=W)
radiobutton4.grid(row=6,column=0,sticky=W)
radiobutton5.grid(row=7,column=0,sticky=W)
radiobutton6.grid(row=8,column=0,sticky=W)
radiobutton7.grid(row=9,column=0,sticky=W)
radiobutton1.grid_forget()
radiobutton2.grid_forget()
radiobutton3.grid_forget()
radiobutton4.grid_forget()
radiobutton5.grid_forget()
radiobutton6.grid_forget()
radiobutton7.grid_forget()

# submit button
buttons = Button(frame,text="Submit Answer",command=lambda: submisson(frame,labelg,checkboxstatus1,checkboxstatus2,checkboxstatus3,checkboxstatus4,assumpttion1,assumpttion2,assumpttion3,assumpttion4,radiobutton1,radiobutton2,radiobutton3,radiobutton4,radiobutton5,radiobutton6,radiobutton7))
buttons.grid(row=13,column=0,padx=10,pady=10)

root.mainloop()
