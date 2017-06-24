from Tkinter import *
from question import Question
from assumption import Assumption
from truthvalue import TruthValue
from reader import readFile

def resizephotoimagewithin1000pixel(img):
    while (img.height()>1000 or img.width()>1000):
        img = img.subsample(2,2)
    return img

def setuptakenquestionlist(questionlist):
    score = 0.0
    root = Tk()
    if(len(questionlist)>0):
        makelayout(score,root,questionlist)
    root.mainloop()

def makelayout(score,root,questionlist):

    question = questionlist[0]
    
    # image1
    img1 = resizephotoimagewithin1000pixel(PhotoImage(file=question.getRealWorldModel()))
    Label().image=img1
 
    # image2
    img2 = resizephotoimagewithin1000pixel(PhotoImage(file=question.getIdealizedModel()))
    Label().image=img2

    # canvas: holds img1 and img2, 10 pixels around image, 75 pixels reserve for grade label
    can = Canvas(root,width=img1.width()+img2.width()+30,height=max(img1.height(),img2.height())+20)
    can.create_image(10,10+75,image=img1,anchor=NW)
    can.create_image(20+img1.width(),10+75,image=img2,anchor=NW)
    can.pack()

    # question frame and question label
    frameq = Frame(root,width=(img1.width()+img2.width())/2,height=100)
    frameq.pack()
    labelq = Label(frameq,text='Assumptions',font="Helvetica 16 bold",pady=25).grid(row=0,sticky=W)

    # frame for assumptions and reasons
    framear = Frame(root,width=(img1.width()+img2.width())/2,height=100)
    framear.pack()

    # checkbox answer storage list:
    checkboxanswer = []
    Nassumptions = len(question.getAssumptions())
    for x in xrange(0,Nassumptions):
        checkboxvalue = IntVar()
        checkboxanswer.append(checkboxvalue)

    # radiobutton answer storage list:
    radiobuttonanswer = []
    Nassumptions = len(question.getAssumptions())
    for x in xrange(0,Nassumptions):
        radiobuttonvalue = IntVar()
        radiobuttonanswer.append(radiobuttonvalue)
        
    # row# storage list list:
    rowstorage = []
    counter = 0
    for x in xrange(0,Nassumptions):
        row = [counter]
        counter = counter +1
        Nreasons = len(question.getAssumptions()[x].getReasons())
        for y in xrange(0,Nreasons):
            row.append(counter)
            counter = counter+1
        rowstorage.append(row)
        
    # grid list; only putting on the checkbox here, no radiobutton yet
    gridlist = []
    r = 0           # place counter
    for x in xrange(0,Nassumptions):
        assumpttion = Checkbutton(framear,text=question.getAssumptions()[x].getAssumptionText(),variable=checkboxanswer[x])
        gridlist.append(assumpttion)
        gridlist[r].grid(row=r,sticky=W)
        r = r+1
        Nreasons = len(question.getAssumptions()[x].getReasons())
        for y in xrange(0,Nreasons):
            radiobutton = Radiobutton(framear,text=question.getAssumptions()[x].getReasons()[y][1],variable=radiobuttonanswer[x],value=y+1)
            gridlist.append(radiobutton)
            gridlist[r].grid(row=r,padx=25,sticky=W)
            #gridlist[r].grid_remove()
            r = r+1

    # grade label
    labelg = Label(root,text="Current Grade is 0",font="Helvetica 36 bold",fg='black')
    labelg.place(x=0,y=0)

    # submit button
    buttons = Button(framear,text="Submit Answer",command=lambda:firstsubmission(score,root,labelg,framear,checkboxanswer,radiobuttonanswer,question,gridlist,rowstorage))
    gridlist.append(buttons)
    gridlist[len(gridlist)-1].grid(row=len(gridlist)-1,pady=25)






def firstsubmission(score,root,labelg,framear,checkboxanswer,radiobuttonanswer,question,gridlist,rowstorage):
    
    # loop checkbox answer
    for x in xrange(0,len(checkboxanswer)):

        # change checkbox to label
        label = Label(framear,text=question.getAssumptions()[x].getAssumptionText())
        gridlist[rowstorage[x][0]].grid_forget()
        gridlist[rowstorage[x][0]] = label
        gridlist[rowstorage[x][0]].grid(row=rowstorage[x][0],sticky=W)
        
        # if assumption is correct
        if question.getAssumptions()[x].getTruthValue()==1:
            
            # if checkbox is selected: score change
            if checkboxanswer[x].get()==1:
                score = score+1
                labelg.config(text='Current Grade is '+str(score))
                
            # if checkbox is not selected: overstrike
            elif checkboxanswer[x].get()==0:
                gridlist[rowstorage[x][0]].config(font="Helvetica 8 overstrike")
                
            # chang color to green
            gridlist[rowstorage[x][0]].config(fg='#00cc00')
            
        # if assumption is not correct
        elif question.getAssumptions()[x].getTruthValue()==0:
            
            # if checkbox is selected: reasons drop down
            if checkboxanswer[x].get()==1:
                gridlist[rowstorage[x][0]].config(fg='red')
                Nreasons = len(question.getAssumptions()[x].getReasons())
                for y in xrange(0,Nreasons):
                    gridlist[rowstorage[x][y+1]].grid()
                    
            # if checkbox is not selected: gray
            elif checkboxanswer[x].get()==0:
                gridlist[rowstorage[x][0]].config(fg='gray')    
    
    # change submit button function
    gridlist[len(gridlist)-1].config(command=lambda:secondsubmission(score,root,labelg,framear,checkboxanswer,radiobuttonanswer,question,gridlist,rowstorage))   




    
def secondsubmission(score,root,labelg,framear,checkboxanswer,radiobuttonanswer,question,gridlist,rowstorage):

    # loop checkbox answer
    for x in xrange(0,len(checkboxanswer)):
        
        # if checkbox selected
        if checkboxanswer[x].get()==1:

            # loop reasons
            Nreasons = len(question.getAssumptions()[x].getReasons())
            for y in xrange(1,Nreasons+1):

                



                
                # if assumption correct
                if question.getAssumptions()[x].getReasons()[y-1][0]==1:

                    # if selected is correct
                    if radiobuttonanswer[x].get()==y:
                        score = score+0.11
                        labelg.config(text='Current Grade is '+str(score))

                    # if selected is not correct 
                    elif radiobuttonanswer[x].get()!=y:
                        gridlist[rowstorage[x][y]].config(fg='gray')

                # if assumption is not correct 
                elif question.getAssumptions()[x].getReasons()[y-1][0]==0:

                    # if selected is correct: drop reason
                    if radiobuttonanswer[x].get()==y:
                        gridlist[rowstorage[x][y]].config(font='Helvetica 8 overstrike')
                        
                    # if selected is not correct
                    elif radiobuttonanswer[x].get()!=y:
                        gridlist[rowstorage[x][y]].config(fg='gray')

    # change submit button function
    gridlist[len(gridlist)-1].config(text='Next Question',command=lambda:nextquestion(score,root,labelg,framear,checkboxanswer,radiobuttonanswer,question,gridlist,rowstorage)) 





def nextquestion(score,root,labelg,framear,checkboxanswer,radiobuttonanswer,question,gridlist,rowstorage):
    print 'done'
    

            
    





# make question list from file 
questionlist = readFile('example_questions.txt')
# setup taken question list
setuptakenquestionlist(questionlist)

