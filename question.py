class Question:

    def __init__(self, name, rw_model, ideal_model):
        self.name = name
        self.assumptions = {"true" : [], "false" : [], "irrelevant" :[]}
        self.rw_model = rw_model
        self.ideal_model = ideal_model


    # Truth values for asumptions represented as strings 
    def add_assumption(self, truth_value, assumption):
        if truth_value == "true" or truth_value == "false" or truth_value == "irrelevant":
            self.assumptions[truth_value].append(assumption)
        else:
            print "Invalid truth value"



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
        