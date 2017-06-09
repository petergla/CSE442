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
