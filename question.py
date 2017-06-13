from truthvalue import TruthValue
from assumption import Assumption
class Question:

    def __init__(self, name, rw_model, ideal_model):
        self.name = name
        self.assumptions = []
        self.rw_model = rw_model #String of path to real world model image
        self.ideal_model = ideal_model #String of path to idealized model image

    # Author: PJ Glasheen
    # Allows assumptions to be entered into the question class.
    def add_assumption(self,truth_value, assumption_text, reason_list):
        newAssumption = Assumption(truth_value, assumption_text, reason_list)
        self.assumptions.append(newAssumption)
        print self.assumptions

    # Author: Paata Ugrekhelidze
    # Allows to get all the values from the data depending what is requested
    def getVal(value):
        if (value == "name"):
            return self.name
        elif (value == "assumption"):
            return self.assumption
        elif (value == "ideal"):
            return self.ideal_model
        elif (value == "real"):
            return self.rw_model
        else:
            print "Invalid Input"
