from question import Question
from assumption import Assumption
from truthvalue import TruthValue


# Author: PJ Glasheen
# Parses through the first line of a question in the txt file and creates a Question object
def parseFirstLine(line):
    questionName = ""
    rwModelPath = ""
    idealModelPath = ""
    index = 1 #Skip index 0 because it is a bracket that we don't want included in the question name
    while line[index] != ";": #Reads question name until semicolon is reached
        questionName = questionName + line[index]
        index = index + 1
    while line[index] == " " or line[index] == ";": #ignore spaces and semicolons
        index = index + 1
    while line[index] != ";": #Reads real world model path until semicolon is reched
        rwModelPath = rwModelPath + line[index]
        index = index + 1
    while line[index] == " " or line[index] == ";": #Ignore spaces and semicolons
        index = index + 1
    while len(line) > index: #Reads idealized model path until end of line is reached
        idealModelPath = idealModelPath + line[index]
        index = index + 1
    question = Question(questionName, rwModelPath, idealModelPath, [])
    return question

# Author: PJ Glasheen
# Parses through line of text and creates an Asumption object
# The way it is currently implemented, the true reason of a false assumption will always
# be listed first. We can randomize the order later when it is displayed to the student.
def parseAssumption(line):
    assText = ""
    truthValueText = ""
    index = 1 #Skip index 0 because we know it's a "(" that we don't want in the assumption text
    while line[index] != ";": #Reads assumption text until ";" is reached
        assText = assText + line[index]
        index = index + 1
    while line[index] == " " or line[index] == ";": #Skips over spaces and semicolons
        index = index + 1 #skips space after semicolon to get truth value
    truthValueText = line[index]
    #if truth Value is T or I, we return the assumption here because there is no reason list
    if truthValueText == "T":
        assum = Assumption(TruthValue.true, assText)
        return assum
    elif truthValueText == "I":
        assum = Assumption(TruthValue.irrelevant, assText)
        return assum
    #If the truth value is false, we need to make a reason list:
    else:
        trueReason = ""
        reasonList = []
        while line[index] != "[": #skip to true reason in bracket
            index = index + 1
        index = index + 1
        while line[index] != "]": #Read true reason
            trueReason = trueReason + line[index]
            index = index +1
        reasonList.append((True, trueReason)) #Add true reason to reason list
        index = index + 2
        while index < len(line): #add false reasons to list
            while line[index] == " ":
                index = index + 1
            reason = ""
            while index < len(line) and line[index] != ";" and line[index] != "]" :
                reason = reason + line[index]
                index = index + 1
            reasonList.append((False,reason))
            index = index + 1
        assum = Assumption(TruthValue.false, assText, reasonList)
        return assum #return the false assumption

# Author: PJ Glasheen
# Reads a txt file and returns a list of questions
def readFile(filename):
    index = 0
    QuestionList = []
    questionfile = open(filename, "r")
    for line in questionfile:
        if line[0] == "{": #Signifies beginning of new question
            QuestionList.append(parseFirstLine(line))
        elif line[0] == "(": #Signifies new assumption for current question
            assum= parseAssumption(line)
            QuestionList[index].addAssumption(assum)
        elif line[0] == "}": #Signifies end of question
            index = index + 1
    return QuestionList
#
# qlist = readFile("testfile.txt")
# for q in qlist:
#     print q.getName()
#     q.printAssumptions()
