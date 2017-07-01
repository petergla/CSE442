from Tkinter import *
from question import Question
from assumption import Assumption
from truthvalue import TruthValue
from reader import readFile



def resizephotoimagewithin1000pixel(img):
    while (img.height()>1000 or img.width()>1000):
        img = img.subsample(2,2)
    return img
# sets up the questions before it is passed to the function that displays the frame
def setuptakenquestionlist(questionlist):
    # score begins initially from 0
    score = 0.0
    # setup a root for a frame
    root = Tk()
    # Title of the frame
    root.wm_title("CodeBusters' Learning Environment")
    # making sure that we have at least one question to start the frame
    if(len(questionlist)>0):
        # function that builds the frame
        makelayout(score,root,questionlist)
    root.mainloop()


# displayes the whole frame
def makelayout(score,root,questionlist):

    # question = first question object of list
    question = questionlist[0]

    # image 1 and image 2
    img1 = resizephotoimagewithin1000pixel(PhotoImage(file=question.getRealWorldModel()))
    img2 = resizephotoimagewithin1000pixel(PhotoImage(file=question.getIdealizedModel()))
    # show() function for the image that was passed in
    Label().image=img1
    Label().image=img2
    # Everything starting from this point is in frame 1: grade, images and question number
    # frame 1: has grade label, canvas(inner frame where images are packed) for two images ,and a question label  
    frame1 = Frame(root,width=(img1.width()+img2.width())/2,height=100)
    frame1.pack()

    # Displays grade label on top left corner. Frozen version of the grade. Updates when makelayout is recalled with a new score. Gets recalled after a new question
    labelg = Label(frame1,text="Current Grade is "+str(score),font="Helvetica 36 bold",fg='black')
    labelg.grid(row=0,sticky=W)

    # canvas: holds image1 and image2, 10 pixels around each image
    can = Canvas(frame1,width=img1.width()+img2.width()+30,height=max(img1.height(),img2.height())+20)
    can.create_image(10,10,image=img1,anchor=NW)
    can.create_image(20+img1.width(),10,image=img2,anchor=NW)
    can.grid(row=1,sticky=W)

    # question number label
    labelq = Label(frame1,text=question.getName(),font="Helvetica 16 bold",pady=25)
    labelq.grid(row=2)
    

    # frame 1 ends here. frame 2 starts from here: includes assumptions and submition button
    frame2 = Frame(root,width=(img1.width()+img2.width())/2,height=100)
    frame2.pack()

    # list of values(int) that store answers(1 of 0) for each checkbox:
    checkboxanswer = []
    # amount of assumptions in total
    Nassumptions = len(question.getAssumptions())
    for x in xrange(0,Nassumptions):
        checkboxvalue = IntVar()
        checkboxanswer.append(checkboxvalue)

    # list of values(int) that store answers(1 of 0) for each radiobutton:
    radiobuttonanswer = []
    Nassumptions = len(question.getAssumptions())
    for x in xrange(0,Nassumptions):
        radiobuttonvalue = IntVar()
        radiobuttonanswer.append(radiobuttonvalue)
        
    # list of list that stores the numbers that represent rows for each assumption andntheir own reasons:
    rowstorage = []
    counter = 0
    for x in xrange(0,Nassumptions):
        # get the assumption and store its row
        row = [counter]
        counter = counter +1
        # get the assumptions' reasons length
        Nreasons = len(question.getAssumptions()[x].getReasons())
        # if the assumption has reason(s) then we will loop and store rows for them
        for y in xrange(0,Nreasons):
            row.append(counter)
            counter = counter+1
        rowstorage.append(row)
    

    # grid list: has visible assumptions and invisible reasons
    gridlist = []
    r = 0           # row counter for assumptions and reasons
    for x in xrange(0,Nassumptions):
        # create a checkbox for each assumption
        assumpttion = Checkbutton(frame2,text=question.getAssumptions()[x].getAssumptionText(),variable=checkboxanswer[x])
        # grid list will store all the chechboxes and radiobuttons in order
        gridlist.append(assumpttion)
        # display the chckbox
        gridlist[r].grid(row=r,sticky=W)
        # move on to the next row
        r = r+1
        # get the size of reasons for the assumption and loop
        Nreasons = len(question.getAssumptions()[x].getReasons())
        for y in xrange(0,Nreasons):
            # create a radiobutton
            radiobutton = Radiobutton(frame2,text=question.getAssumptions()[x].getReasons()[y][1],variable=radiobuttonanswer[x],value=y+1)
            # store in the grid
            gridlist.append(radiobutton)
            # display it
            gridlist[r].grid(row=r,padx=25,sticky=W)
            # hides from the frame initially
            gridlist[r].grid_remove()
            # move on to the next row
            r = r+1
            
    # submit button
    buttons = Button(frame2,text="Submit Answer",command=lambda:firstsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2))
    gridlist.append(buttons)
    gridlist[len(gridlist)-1].grid(row=len(gridlist)-1,pady=25)

def firstsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2):
    # get the first question
    question = questionlist[0]        
    
    # loop checkbox answer
    for x in xrange(0,len(checkboxanswer)):

        # disable all the checkboxes. add the overlapping assumption text so we could color it afterwards
        label = Label(frame2,text=question.getAssumptions()[x].getAssumptionText())
        gridlist[rowstorage[x][0]].config(state=DISABLED)
        gridlist[rowstorage[x][0]] = label
        gridlist[rowstorage[x][0]].grid(row=rowstorage[x][0],padx=24,sticky=W)
        
        # if assumption is correct
        if question.getAssumptions()[x].getTruthValue()==1:
            
            # if checkbox is selected: score change
            if checkboxanswer[x].get()==1:
                score = score+1
                # updates the score when the assumptions are chosen
                labelg.config(text='Current Grade is '+str(score))
                
            # change assumption color to green because it is correct
            gridlist[rowstorage[x][0]].config(fg='#00cc00')
            
        # if assumption is not correct
        elif question.getAssumptions()[x].getTruthValue()==0:
            
            # if checkbox is selected: reasons drop down
            if checkboxanswer[x].get()==1:
                # assumption color becomes red
                gridlist[rowstorage[x][0]].config(fg='red')
                Nreasons = len(question.getAssumptions()[x].getReasons())
                for y in xrange(0,Nreasons):
                    # loops through all the reasons for the assumption and displayes them in order
                    gridlist[rowstorage[x][y+1]].grid()
                    
            # if checkbox is not selected: gray it out
            elif checkboxanswer[x].get()==0:
                gridlist[rowstorage[x][0]].config(fg='gray')    

    # change submit button to next question
    gridlist[len(gridlist)-1].config(text='Next Question',command=lambda:nextquestion(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2))

    # if reason drop down change submit text "Next Question" button to second submission text "Submit Answer" button
    for x in xrange(0,len(checkboxanswer)):
        # if the assumption is wrong
        if question.getAssumptions()[x].getTruthValue()==0:
            # if the assumption checkbox was chosen
            if checkboxanswer[x].get()==1:
                # change the button text to "Submit Answer"
                gridlist[len(gridlist)-1].config(text='Submit Answer',command=lambda:secondsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2))
                break



        
  
def secondsubmission(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2):

    question = questionlist[0]

    # loop checkbox answer
    for x in xrange(0,len(checkboxanswer)):
        
        # if checkbox selected
        if checkboxanswer[x].get()==1:

            # loop reasons
            Nreasons = len(question.getAssumptions()[x].getReasons())
            for y in xrange(1,Nreasons+1):

                # change radiobutton to label
                label = Label(frame2,text=question.getAssumptions()[x].getReasons()[y-1][1])
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
    gridlist[len(gridlist)-1].config(text='Next Question',command=lambda:nextquestion(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2)) 

def nextquestion(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2):
    
    if len(questionlist)==1:
        gridlist[len(gridlist)-1].config(command=lambda:endingpage(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2)) 

    elif len(questionlist)>1:
        frame1.destroy()
        frame2.destroy()
        del questionlist[0]
        makelayout(score,root,questionlist)

def endingpage(score,root,labelg,checkboxanswer,radiobuttonanswer,questionlist,gridlist,rowstorage,frame1,frame2):
    print "this is the final page"
    

    

    







# reads a textfile where the questions are written, returns a list of question objects
questionlist = readFile('example_questions.txt')
# pass the list of questions to a function that creates the frame
setuptakenquestionlist(questionlist)

