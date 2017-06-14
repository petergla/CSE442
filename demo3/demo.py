gifdir = "./"
from Tkinter import *


def fun1(label):
    print(checkboxstatus1.get()) #incorrect
    print(checkboxstatus2.get()) #incorrect
    print(checkboxstatus3.get()) #correct
    print(checkboxstatus4.get()) #correct

    answer_key = [0,0,1,1]
    answers = [checkboxstatus1.get(), checkboxstatus2.get(), checkboxstatus3.get(), checkboxstatus4.get()]
    score = 0.0
    for i in range(len(answer_key)):
        if answer_key[i] == answers[i]:
            score = score + 1
    label.configure(text =  "Current grade is " + str((score/4.0)*100.0)  + "%")

root = Tk()
root.wm_title("CodeBusters' Learning Environment")   #change window name
fil1 = 'RealWorld_1.gif'
img1 = PhotoImage(file=gifdir+fil1)
scl1 = img1.subsample(3,3)
# subsample(self, x, y='')
# Return a new PhotoImage based on the same image as this widget but use only every Xth or Yth pixel.
can1 = Canvas(root)
can1.config(width=scl1.width(),height=scl1.height())
can1.create_image(0,0,image=scl1,anchor=NW)
can1.grid(row=0,column=0)

fil2 = 'IdealizedModel1_1.gif'
img2 = PhotoImage(file=gifdir+fil2)
scl2 = img2.subsample(3,3)
can2 = Canvas(root)
can2.config(width=scl2.width(),height=scl2.height())
can2.create_image(0,0,image=scl2,anchor=NW)
can2.grid(row=0,column=2)

labelq = Label(root,text="Please select the correct assumptions:",fg='blue')
labelq.grid(row=1,column=0,sticky=W)

checkboxstatus1 = IntVar()
checkboxstatus2 = IntVar()
checkboxstatus3 = IntVar()
checkboxstatus4 = IntVar()
# checkboxstatus hold the status of checkbox
# use .get() to get status.
# 1 for a check, 0 for no check.
check1 = Checkbutton(root, text="Hip acts as a pivot point (no lifting off the bed)",fg='blue',variable=checkboxstatus1)
check2 = Checkbutton(root, text="Lower leg remains approximately perpendicular to upper leg",fg='blue',variable=checkboxstatus2)
check3 = Checkbutton(root, text="Forces are reasonably approximated using static analysis",fg='blue',variable=checkboxstatus3)
check4 = Checkbutton(root, text="Patient does not slide on the bed",fg='blue',variable=checkboxstatus4)
check1.grid(row=2,column=0,sticky=W)
check2.grid(row=3,column=0,sticky=W)
check3.grid(row=4,column=0,sticky=W)
check4.grid(row=5,column=0,sticky=W)

labelg = Label(root,text="Current grade is ---",fg='white',bg='skyblue')
labelg.grid(row=7,column=0,sticky=W)

buttons = Button(root,text="Submit Answer",fg='white',bg='green',command=lambda: fun1(labelg))
buttons.grid(row=6,column=2,sticky=E)

root.mainloop()

# problem: using PIL library will be easier to handle images, but window only
