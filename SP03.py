from Tkinter import *
from truthvalue import TruthValue
from truthvalue import getString
from assumption import Assumption
from question import Question
from reader import readFile

def resizephotoimagewithin1000pixel(img):
    while (img.height()>1000 or img.width()>1000):
        # subsample(self, x, y='')
        # Return a new PhotoImage based on the same image as this widget but use only every Xth or Yth pixel.
        img = img.subsample(2,2)
    return img

def nextquestion(buttons,labelg,score,question,answer,frame,gridlist,reasonsdropreferencetable):
    print 'done'

# second submission
def submisson2ndtime(buttons,labelg,score,question,answer,frame,gridlist,reasonsdropreferencetable):

    # makes radiobuttons go away 
    for x in xrange(0,len(answer)):
        if answer[x][0].get()==1:
            for y in xrange(0,len(question.getAssumptions()[x].getReasons())):
                label = Label(frame,text=question.getAssumptions()[x].getReasons()[y][1],padx=25)
                gridlist[reasonsdropreferencetable[x][y]].grid_forget()
                gridlist[reasonsdropreferencetable[x][y]] = label
                gridlist[reasonsdropreferencetable[x][y]].grid(row=reasonsdropreferencetable[x][y]+1,sticky=W)

    # chang color of selected reason base on correctness
    # update score
    for x in xrange(0,len(answer)):
        if answer[x][0].get()==1:
            for y in xrange(0,len(question.getAssumptions()[x].getReasons())):
                if question.getAssumptions()[x].getReasons()[y][0]==1:
                    if answer[x][1].get()-1==y:
                        gridlist[reasonsdropreferencetable[x][y]].config(fg='green')
                        score = score+0.11
                        labelg.config(text='Current Grade is '+str(score))
                if question.getAssumptions()[x].getReasons()[y][0]==0:
                    if answer[x][1].get()-1==y:
                        gridlist[reasonsdropreferencetable[x][y]].config(fg='red')
    
    buttons.config(text='Next Question',command=lambda:nextquestion(buttons,labelg,score,question,answer,frame,gridlist,reasonsdropreferencetable))
    
# first submission
def submisson(buttons,labelg,score,question,answer,frame,gridlist,reasonsdropreferencetable):
    
    for x in xrange(0,len(answer)): # update score base on assumption selections 
        if answer[x][0].get()==question.getAssumptions()[x].getTruthValue():
            score = score+1
    labelg.config(text='Current Grade is '+str(score))

    # makes checkboxes go away
    for x in xrange(0,len(question.getAssumptions())):  #
        label = Label(frame,text=question.getAssumptions()[x].getAssumptionText())
        gridlist[reasonsdropreferencetable[x][0]-1].grid_forget()
        gridlist[reasonsdropreferencetable[x][0]-1] = label
        gridlist[reasonsdropreferencetable[x][0]-1].grid(row=reasonsdropreferencetable[x][0],sticky=W)
        
    # update the selected assumption color base on correctness
    # change score 
    for x in xrange(0,len(answer)): 
        if answer[x][0].get()==1:
            if answer[x][0].get()==question.getAssumptions()[x].getTruthValue():
                gridlist[reasonsdropreferencetable[x][0]-1].config(fg='green')
            if answer[x][0].get()!=question.getAssumptions()[x].getTruthValue():
                gridlist[reasonsdropreferencetable[x][0]-1].config(fg='red')
                for y in xrange(0,len(question.getAssumptions()[x].getReasons())):
                    gridlist[reasonsdropreferencetable[x][y]].grid()                # drop down reasons if selected assumption is wrong

    buttons.config(command=lambda:submisson2ndtime(buttons,labelg,score,question,answer,frame,gridlist,reasonsdropreferencetable))

def makelayouttakenquestionobject(root,question):
    
    # image1
    fil1 = question.getRealWorldModel()
    img1 = PhotoImage(file=fil1)
    scl1 = resizephotoimagewithin1000pixel(img1)
    label = Label(image = scl1)
    label.image = scl1
    
    # image2
    fil2 = question.getIdealizedModel()
    img2 = PhotoImage(file=fil2)
    scl2 = resizephotoimagewithin1000pixel(img2)
    label2 = Label(image = scl2)
    label2.image = scl2

    # canvas
    # holds image1 and image2
    # 10 pixels around image
    # 50 pixels reserve for label
    can = Canvas(root,width=scl1.width()+scl2.width()+30,height=max(scl1.height(),scl2.height())+20)
    can.create_image(10,10+75,image=scl1,anchor=NW)
    can.create_image(20+scl1.width(),10+75,image=scl2,anchor=NW)
    can.pack()

    # grade label
    labelg = Label(root,text="Current Grade is ---",font="Helvetica 36 bold",fg='black')
    labelg.place(x=0,y=0)

    # frame
    # width = image1 + image 2
    frame = Frame(root,width=(scl1.width()+scl2.width())/2,height=100)
    frame.pack()

    # problem label
    labelq = Label(frame,text='Assumptions',font="Helvetica 16 bold",pady=25).grid(row=0,column=0,sticky=W)

    # answer list
    answer = []
    howmanyassumptionsinquestion = len(question.getAssumptions())
    for x in xrange(0,howmanyassumptionsinquestion):
        checkboxstatus = IntVar()
        reasoninstance = IntVar()
        answer.append([checkboxstatus,reasoninstance])

    # reasons drop reference table
    r = 1   # plae counter
    reasonsdropreferencetable = []
    for x in xrange(0,howmanyassumptionsinquestion):
        rowcurrent = r
        row = [rowcurrent]
        r = r+1
        howmanyreasonsinassumption = len(question.getAssumptions()[x].getReasons())
        for y in xrange(0,howmanyreasonsinassumption):
            columncurrent = r
            row.append(columncurrent)
            r = r+1
        reasonsdropreferencetable.append(row)

    # list of element on grid
    gridlist = []
    r = 1   # place counter
    for x in xrange(0,howmanyassumptionsinquestion):
        assumpttion = Checkbutton(frame,text=question.getAssumptions()[x].getAssumptionText(),variable=answer[x][0])
        gridlist.append(assumpttion)
        gridlist[r-1].grid(row=r,sticky=W)
        r = r+1
        howmanyreasonsinassumption = len(question.getAssumptions()[x].getReasons())
        for y in xrange(0,howmanyreasonsinassumption):
            radiobutton = Radiobutton(frame,text=question.getAssumptions()[x].getReasons()[y][1],variable=answer[x][1],value=y+1)
            gridlist.append(radiobutton)
            gridlist[r-1].grid(row=r,padx=25,sticky=W)
            gridlist[r-1].grid_remove()     # grid_remove() does not remove component from grid, it hides it, grid() makes it showing again
            r = r+1

    # submit button
    score = 0.0
    buttons = Button(frame,text="Submit Answer",command=lambda:submisson(buttons,labelg,score,question,answer,frame,gridlist,reasonsdropreferencetable))
    buttons.grid(row=r,pady=25)


def makelayouttakenquestionlist(score,root,questionlist):
    print



questionlist = readFile('example_questions.txt')

root = Tk()

makelayouttakenquestionobject(root,questionlist[1])

root.mainloop()

















