from Tkinter import *
from truthvalue import TruthValue
from truthvalue import getString
from assumption import Assumption
from question import Question

def resizephotoimagewithin1000pixel(img):
    while (img.height()>1000 or img.width()>1000):
        # subsample(self, x, y='')
        # Return a new PhotoImage based on the same image as this widget but use only every Xth or Yth pixel.
        img = img.subsample(2,2)
    return img
def submisson():
    print 'need to write something here'
    
# making question list example manually  
# assumption 1
Numerical_truth_value1 = 0
assumption_text1 = "Hip acts as a pivot point (no lifting off the bed)"
reason_list1 = [(True,'Valid Reason #1.1.1'),(False,"Invalid Reason #1.1.2"),(False, "Invalid Reason #1.1.3")]
assumption1 = Assumption(Numerical_truth_value1,assumption_text1,reason_list1)
# assumption 2
Numerical_truth_value2 = 0
assumption_text2 = "Lower leg remains approximately perpendicular to upper leg"
reason_list2 = [(False,'Invalid Reason #1.2.1'),(False,"Invalid Reason #1.2.2"),(False, "Invalid Reason #1.2.3"),(True,"Valid Reason #1.2.4")]
assumption2 = Assumption(Numerical_truth_value2,assumption_text2,reason_list2)
# assumption 3
Numerical_truth_value3 = 1
assumption_text3 = "Forces are reasonably approximated using static analysis"
reason_list3 = []
assumption3 = Assumption(Numerical_truth_value3,assumption_text3,reason_list3)
# assumption 4
Numerical_truth_value4 = 1
assumption_text4 = "Patient does not slide on the bed"
reason_list4 = []
assumption4 = Assumption(Numerical_truth_value4,assumption_text4,reason_list4)
# assumption list
assumptionlist = [assumption1,assumption2,assumption3,assumption4]
# question list
question1 = Question("First Example",'RealWorld_1.gif','IdealizedModel1_1.gif',assumptionlist)
question2 = Question("First Example",'./IdealizedModel1_1.gif','./RealWorld_1.gif',assumptionlist)
questionlist = [question1,question2]

root = Tk()

# current queston number
currentquestion = 0
    
# image1
img1 = PhotoImage(file=questionlist[currentquestion].getRealWorldModel())
scl1 = resizephotoimagewithin1000pixel(img1)

# image2
img2 = PhotoImage(file=questionlist[currentquestion].getIdealizedModel())
scl2 = resizephotoimagewithin1000pixel(img2)

# canvas
# holds image1 and image2
# 10 pixels around image
# 50 pixels reserve for label
can = Canvas(root,width=scl1.width()+scl2.width()+30,height=max(scl1.height(),scl2.height())+20)
can.create_image(10,10+50,image=scl1,anchor=NW)
can.create_image(20+scl1.width(),10+50,image=scl2,anchor=NW)
can.pack()

# frame
# width = image1 + image 2
frame = Frame(root,width=(scl1.width()+scl2.width())/2,height=100)
frame.pack()

# problem label
labelq = Label(frame,text='Assumptions',font="Helvetica 16 bold",pady=25).grid(row=0,column=0,sticky=W)

# anwer list
answer = []
for x in xrange(0,len(questionlist[currentquestion].getAssumptions())):
    checkboxstatus = IntVar()
    answer.append(checkboxstatus)

# reason instance list
reasonselection = []
for x in xrange(0,len(questionlist[currentquestion].getAssumptions())):
    reasoninstance = IntVar()
    reasonselection.append(reasoninstance)

r = 1   # row number

# list of element on grid
gridlist = []
for x in xrange(0,len(questionlist[currentquestion].getAssumptions())):
    assumpttion = Checkbutton(frame,text=questionlist[currentquestion].getAssumptions()[x].getAssumptionText(),variable=answer[x])
    gridlist.append(assumpttion)
    gridlist[r-1].grid(row=r,sticky=W)
    r = r+1
    for y in xrange(0,len(questionlist[currentquestion].getAssumptions()[x].getReasons())):
        radiobutton = Radiobutton(frame,text=questionlist[currentquestion].getAssumptions()[x].getReasons()[y][1],variable=reasonselection[x],value=y+1)
        gridlist.append(radiobutton)
        gridlist[r-1].grid(row=r,padx=25,sticky=W)
        #gridlist[r-1].grid_remove()     # grid_remove() does not remove component from grid, it hides it, grid() makes it showing again 
        r = r+1

# submit button
buttons = Button(frame,text="Submit Answer",command=lambda: submisson())
buttons.grid(row=r,pady=25)

root.mainloop()

















