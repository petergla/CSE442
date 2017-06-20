from truthvalue import TruthValue
from truthvalue import getString
from assumption import Assumption

class Question:

    def __init__(self, name, rw_model, ideal_model, assumptions = []):
        self.name = name #name of the question
        self.assumptions = assumptions #list of assumptions. Defaults to empty list.
        self.rw_model = rw_model #String of path to real world model image
        self.ideal_model = ideal_model #String of path to idealized model image

    # Author: PJ Glasheen
    # Allows assumptions to be entered into the question class.
    def addAssumption(self,assumption):

        self.assumptions.append(assumption)

    # Author: PJ Glasheen
    # remove an assumption from the assumption list by its index
    def removeAssumption(self, index):
        try:
            del self.assumptions[index]
        except IndexError:
            print("The assumption list is empty. There is nothing to remove.")

    # Author: PJ Glasheen
    # prints the index, truth value, and text of all the assumptions
    def printAssumptions(self):
        for item in range(len(self.assumptions)):
            tv_string = getString(self.assumptions[item].getTruthValue())
            spacer = " " * (11 - len(tv_string)) + "| "
            print " " +str(item) + " | " + tv_string + spacer + self.assumptions[item].getAssumptionText()

    def getName(self):
        return self.name

    def getAssumptions(self):
        return self.assumptions

    def getIdealizedModel(self):
        return self.ideal_model

    def getRealWorldModel(self):
        return self.RealWorldModel


# q = Question("question 1", "test", "test")
# q.addAssumption(TruthValue.true, "This is an assumption")
# q.addAssumption(TruthValue.irrelevant, "This is an assumption that is irrelevant")
# q.addAssumption(TruthValue.irrelevant, "This is another assumption")
# q.addAssumption(TruthValue.false, "This is a false assumption")
# q.removeAssumption(1)
# q.removeAssumption(1)
# q.printAssumptions()
