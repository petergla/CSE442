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
    root.wm_title("CodeBusters' Learning Environment")
    if(len(questionlist)>0):
        makelayout(score,root,questionlist)
    root.mainloop()

def makelayout(score,root,questionlist):

    # question = first question object of list
    question = questionlist[0]

    # image 1 and image 2
    img1 = resizephotoimagewithin1000pixel(PhotoImage(file=question.getRealWorldModel()))
    Label().image=img1
    img2 = resizephotoimagewithin1000pixel(PhotoImage(file=question.getIdealizedModel()))
    Label().image=img2

    # frame 1: has grade label, canvas for two image ,and question label  
    frame1 = Frame(root,width=(img1.width()+img2.width())/2,height=100)
    frame1.pack()

    # grade label
    labelg = Label(frame1,text="Current Grade is "+str(score),font="Helvetica 36 bold",fg='black')
    labelg.grid(row=0,sticky=W)

    # canvas: holds image1 and image2, 10 pixels around each image, 75 pixels reserve for grade label
    can = Canvas(frame1,width=img1.width()+img2.width()+30,height=max(img1.height(),img2.height())+20)
    can.create_image(10,10,image=img1,anchor=NW)
    can.create_image(20+img1.width(),10,image=img2,anchor=NW)
    can.grid(row=1,sticky=W)

    # question label
    labelq = Label(frame1,text=question.getName(),font="Helvetica 16 bold",pady=25)
    labelq.grid(row=2)
    
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
        
    # grid list: has visible assumptions and invisible reasons
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
            gridlist[r].grid_remove()
            r = r+1
            
    # submit button
    buttons = Button(framear,text="Submit Answer",command=lambda:firstsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear))
    gridlist.append(buttons)
    gridlist[len(gridlist)-1].grid(row=len(gridlist)-1,pady=25)

def firstsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear):
    
    question = questionlist[0]        
    
    # loop checkbox answer
    for x in xrange(0,len(checkboxanswer)):

        # add label overlapping checkbox text
        label = Label(framear,text=question.getAssumptions()[x].getAssumptionText())
        gridlist[rowstorage[x][0]].config(state=DISABLED)
        gridlist[rowstorage[x][0]] = label
        gridlist[rowstorage[x][0]].grid(row=rowstorage[x][0],padx=24,sticky=W)
        
        # if assumption is correct
        if question.getAssumptions()[x].getTruthValue()==1:
            
            # if checkbox is selected: score change
            if checkboxanswer[x].get()==1:
                score = score+1
                labelg.config(text='Current Grade is '+str(score))
                
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

    # change submit button to next question
    gridlist[len(gridlist)-1].config(text='Next Question',command=lambda:nextquestion(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear))

    # if reason drop down change submit button to second submission button
    for x in xrange(0,len(checkboxanswer)):
        if question.getAssumptions()[x].getTruthValue()==0:
            if checkboxanswer[x].get()==1:
                gridlist[len(gridlist)-1].config(text='Submit Answer',command=lambda:secondsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear))
                break



        
  
def secondsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear):

    question = questionlist[0]

    # loop checkbox answer
    for x in xrange(0,len(checkboxanswer)):
        
        # if checkbox selected
        if checkboxanswer[x].get()==1:

            # loop reasons
            Nreasons = len(question.getAssumptions()[x].getReasons())
            for y in xrange(1,Nreasons+1):

                # change radiobutton to label
                label = Label(framear,text=question.getAssumptions()[x].getReasons()[y-1][1])
                gridlist[rowstorage[x][y]].grid_forget()
                gridlist[rowstorage[x][y]] = label
                gridlist[rowstorage[x][y]].grid(row=rowstorage[x][y],padx=25,sticky=W)

                # if assumption correct
                if question.getAssumptions()[x].getReasons()[y-1][0]==1:

                    # if selected is correct
                    if radiobuttonanswer[x].get()==y:
                        score = score+0.11
                        labelg.config(text='Current Grade is '+str(score))

                    # if selected is not correct 
                    elif radiobuttonanswer[x].get()!=y:
                        print
                        #gridlist[rowstorage[x][y]].config(fg='gray')

                # if assumption is not correct 
                elif question.getAssumptions()[x].getReasons()[y-1][0]==0:

                    # if selected is correct: drop reason
                    if radiobuttonanswer[x].get()==y:
                        gridlist[rowstorage[x][y]].config(font='Helvetica 8 overstrike')
                        
                    # if selected is not correct
                    elif radiobuttonanswer[x].get()!=y:
                        print
                        gridlist[rowstorage[x][y]].config(fg='gray')

    # change submit button function and text
    gridlist[len(gridlist)-1].config(text='Next Question',command=lambda:nextquestion(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear)) 

def nextquestion(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear):
    
    if len(questionlist)==1:
        gridlist[len(gridlist)-1].config(command=lambda:endingpage(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear)) 

    elif len(questionlist)>1:
        frame1.destroy()
        framear.destroy()
        del questionlist[0]
        makelayout(score,root,questionlist)

def endingpage(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,framear):
    print "this is the final page"
    

    

    







# make question list from file 
questionlist = readFile('example_questions.txt')
# setup taken questionlist
setuptakenquestionlist(questionlist)

