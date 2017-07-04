from question import Question
from assumption import Assumption
from truthvalue import TruthValue

def readQuestion(line):
    index = 9 #Index of the string where the question name begins
    while line[index] == " ":
        index = index + 1 #Ignores preceding spaces
    # print line[index:]
    return line[index:-1] #returns the question name & deletes the \n char at the end

def readImgPath(imgType, line):
    index = 0
    if imgType == "I":
        index = 16
    elif imgType == "R":
        index = 17
    while line[index] == " ":
        index = index + 1
    return line[index:-1]

def readAssumption(line):
    index = 11
    assText = ""
    while line[index] == " ":
        index = index + 1
    while line[index] != "|":
        assText = assText + line[index]
        index = index + 1
    # print line[index]
    index = index + 1
    while line[index] == " ":
        index = index + 1
    if line[index] == "T":
        return Assumption(TruthValue.true, assText, [])
    elif line[index] == "F":
        return Assumption(TruthValue.false, assText, [])
    else:
        print "The letter is " + line[index]
        reasonList = []
        return Assumption(TruthValue.irrelevant, assText, reasonList)

def readReason(line):
    # print "AAAAAAAAAAAAAAA"
    index = 7
    reasonText = ""
    while line[index] == " ":
        index = index + 1
    while line[index] != "|":
        reasonText = reasonText + line[index]
        index = index + 1
        # print reasonText
    index = index + 1
    while line[index] == " ":
        index = index + 1
    if line[index] == "T":
        return (True, reasonText)
    else:
        return (False, reasonText)

def readFile(filename):
    questionList = []
    questionfile = open(filename, "r")
    questionName = ""
    idealizedModel = ""
    realWorldModel = ""
    assumptions = []
    assIndex = 0

    for line in questionfile:
        if line[0] == "Q":
            if assIndex != 0:
                questionList.append(Question(questionName, realWorldModel, idealizedModel, assumptions))
            assumptions = [] #clears the assumption list
            questionName = readQuestion(line)
            assIndex = 1
        elif line[0] == "I":
            idealizedModel = readImgPath("I", line)
        elif line[0] == "R" and line[3] == "l":
            realWorldModel = readImgPath("R", line)
        elif line[0] == "A":
            assumptions.append(readAssumption(line))
        elif line[0] == "R" and line[3] == "s":
            reason = readReason(line)
            assumptions[-1].add_reason(reason[0], reason[1])
    questionList.append(Question(questionName, realWorldModel, idealizedModel, assumptions))
    questionList[0].printAssumptions()
    print len(questionList)
    return questionList


# print readImgPath("I", "Idealized Model: sample.gif\n")
# print readImgPath("R", "Real World Model: sample.gif\n")
