from question import Question
from assumption import Assumption

def parseFirstLine(line):
    questionName = ""
    rwModelPath = ""
    idealModelPath = ""
    index = 1
    while line[index] != ",":
        questionName = questionName + line[index]
        index = index + 1
    while line[index] == " " or line[index] == ",": #ignores spaces and commas
        index = index + 1
    while line[index] != ",":
        rwModelPath = rwModelPath + line[index]
        index = index + 1
    while line[index] == " " or line[index] == ",":
        index = index + 1
    while len(line) > index:
        idealModelPath = idealModelPath + line[index]
        index = index + 1
    question = Question(questionName, rwModelPath, idealModelPath)
    return question

def parseAssumption(line):
    index = 1
    assText = ""
    truthValueText = ""
    while line[index] != ",":
        assText = assText + line[index]
        index = index + 1
    while line[index] == " " or line[index] == ",":
        index = index + 1
    truthValueText = line[index]
    if truthValueText == "T":
        assum = Assumption()


#
# def readFile(filename):
#     state = -1
#     index = 0
#     QuestionList = []
#     questionfile = open(filename, "r")
#     for line in questionfile:
#         if line[0] == "{":
#             question = parseFirstLine(line)
#             QuestionList.append(question)
#         else:


parseAssumption("(Assumption 1, T)")
