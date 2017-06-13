from truthvalue import TruthValue
# Author: PJ Glasheen
class Assumption:

    def __init__(self, truth_value, assumption_text, reason_list):
        self.truth_value = truth_value #represented as a TruthValue object
        self.assumption_text = assumption_text #String for text of assumption
        self.reason_list = reason_list #list of tuples in format (bool, reason_text)

    # Add a reason to the assumption that can be either true or false.
    def add_reason(self, boolean, reason_text):
        self.reason_list.append((boolean, reason_text))

    def getTruthValue(self):
        return self.truth_value
