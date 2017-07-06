from question import Question
from assumption import Assumption
from truthvalue import TruthValue
# Author: PJ Glasheen

# Reads a line of the text file that begins with question and returns string of question name
def readQuestion(line):
    index = 9 #Index of the char where the question name begins
    while line[index] == " ":
        index = index + 1 #Ignores preceding spaces
    return line[index:-1] #returns the question name & deletes the \n char at the end

# Reads line that is an image path and returns string of image path
def readImgPath(imgType, line):
    index = 0
    #changes index of where path begins depending on whether it is RW or Ideal image
    if imgType == "I":
        index = 16 #if the line begins with "idealized image" the name of the path would not begin until index 16
    elif imgType == "R":
        index = 17 #16 for rw model
    while line[index] == " ":
        index = index + 1
    return line[index:-1] #returns string excluding the last \n char

#reads assumption line and returns an assumption with the text & truth value
def readAssumption(line):
    index = 11 #index of char where assumption name begins
    assText = ""
    while line[index] == " ": #ignores preceding spaces
        index = index + 1
    while line[index] != "|": #reads up to | which signifies end of text
        assText = assText + line[index]
        index = index + 1
    while assText[-1] == " ": #removes trailing spaces from assText
        assText = assText[:-1]
    index = index + 1
    while line[index] == " ": #ignores preceding spaces
        index = index + 1
    #Checks first char of truth value in line and assigns the truth value accordingly
    if line[index] == "T":
        return Assumption(TruthValue.true, assText, [])
    elif line[index] == "F":
        return Assumption(TruthValue.false, assText, [])
    else:
        return Assumption(TruthValue.irrelevant, assText, [])


#reads a reason line and returns a tuple of (bool, reason text)
def readReason(line):
    index = 7
    reasonText = ""
    while line[index] == " ":
        index = index + 1
    while line[index] != "|":
        reasonText = reasonText + line[index]
        index = index + 1
    while reasonText[-1] == " ": #removes trailing spaces
        reasonText = reasonText[:-1]
    index = index + 1
    while line[index] == " ":
        index = index + 1
    if line[index] == "T":
        return (True, reasonText)
    else:
        return (False, reasonText)

# reads a weight line and returns weight as a float
def readWeight(type, line):
    index = 0
    #checks the type of weight and assigns the starting index
    if type == "R": #R signifies reason weight. The weight would begin at index 14 in this case
        index = 14
    elif type == "C": #C signifies correct assumption weight. The indes would be 26
        index = 26
    elif type == "W": #Wrong assumtion weight. Index is 14.
        index = 24
    while line[index] == " ": #ignore preceding spaces
        index = index + 1
    weightString = line[index:-1] #removes last \n char
    while weightString[-1] == " ": #removes trailing spaces
        weightString = weightString[:-1]
    return float(weightString) #returns weight as floating point number


#reads txt file with questions and returns list of Questions
def readFile(filename):
    questionList = []
    questionfile = open(filename, "r")
    questionName = ""
    idealizedModel = ""
    realWorldModel = ""
    assumptions = []
    wrongAssumptionWeight = 0 #default value
    correctAssumptionWeight = 4 #default value
    reasonWeight = 1 #default value
    firstQuestionRead = False

    for line in questionfile:
        if line[0] == "Q":
            if firstQuestionRead: #Appends prev. question to question list only if first question has been read
                questionList.append(Question(questionName, realWorldModel, idealizedModel, assumptions, correctAssumptionWeight, wrongAssumptionWeight, reasonWeight))
            assumptions = [] #clears the assumption list
            wrongAssumptionWeight = 0    #\
            correctAssumptionWeight = 4  # > Resets these vars to default values for new question
            reasonWeight = 1             #/
            questionName = readQuestion(line)
            firstQuestionRead = True
        elif line[0] == "I": #If line is idealized model line, runs readImgPath with I identifier
            idealizedModel = readImgPath("I", line)
        elif line[0] == "R" and line[3] == "l": #if line defines real world model, runs readImgPath with R identifier
            realWorldModel = readImgPath("R", line)
        elif line[0] == "A": #If line is assumption line, runs readAssumption
            assumptions.append(readAssumption(line))
        elif line[0] == "R" and line[3] == "s" and line[6] == ":": #If line is reason line, runs readReason
            reason = readReason(line)
            assumptions[-1].add_reason(reason[0], reason[1])
        elif line[0] == "R" and line[3] == "s" and line[6] == " ": #If line is Reason Weight line, runs readWeight with R identifier
            reasonWeight = readWeight("R",line)
        elif line[0] == "C": #If the line is a correct assumption weight, runs readWeight with C identifier
            correctAssumptionWeight = readWeight("C", line)
        elif line[0] == "W": #If the line is a wrong assumption weight, runs readWeight with W identifier
            wrongAssumptionWeight = readWeight("W", line)
    #Appends last question read to question list
    questionList.append(Question(questionName, realWorldModel, idealizedModel, assumptions, correctAssumptionWeight, wrongAssumptionWeight, reasonWeight))
    return questionList
