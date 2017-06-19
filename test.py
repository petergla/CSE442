import unittest
from assumption import Assumption
from question import Question
import random
# Author: Paata Ugrekhelidze

# This class is designed to perform unit tests over the major testable functions


class MyTest(unittest.TestCase):
	# test cases for assumption library
	# tests getTruthValue function from assumption library
    def test_getTruthValue(self):
    	self.Numerical_truth_value = random.randint(0,2) #always randomize truthvalue for every test run
    	self.assumption_text = 'Lorem Ipsum'
    	self.reason_list = [(bool(random.getrandbits(1)),'Lorem Ipsum1'),(bool(random.getrandbits(1)), "Lorem Ipsum2")] #always randomize boolean values for reason list
    	self.temp_assumption = Assumption(self.Numerical_truth_value,self.assumption_text,self.reason_list)
        self.assertEqual(self.temp_assumption.getTruthValue(), self.Numerical_truth_value)
    # tests getAssumptionText function from assumption library
    def test_getAssumptionText(self):
    	self.Numerical_truth_value = random.randint(0,2)
    	self.assumption_text = 'Lorem Ipsum'
    	self.reason_list = [(bool(random.getrandbits(1)),'Lorem Ipsum1'),(bool(random.getrandbits(1)), "Lorem Ipsum2")]
    	self.temp_assumption = Assumption(self.Numerical_truth_value,self.assumption_text,self.reason_list)
        self.assertEqual(self.temp_assumption.getAssumptionText(), self.assumption_text)
    # tests add_reason function from assumption library
    def test_add_reason(self):
    	self.Numerical_truth_value = random.randint(0,2)
    	self.assumption_text = 'Lorem Ipsumus'
    	self.reason_list = [(bool(random.getrandbits(1)),'Lorem Ipsumus1'),(bool(random.getrandbits(1)), "Lorem Ipsumus2")]
    	self.temp_assumption = Assumption(self.Numerical_truth_value,self.assumption_text,self.reason_list)
        self.test_value = bool(random.getrandbits(1))
        self.test_reason = "Lorem Ipsum3"
        self.temp_assumption.add_reason(self.test_value,self.test_reason)
        self.assertEqual(self.temp_assumption.reason_list[-1], (self.test_value,self.test_reason))
    # test cases for question library
    # tests addAssumption function in question library
    def test_addAssumption(self):
    	self.name = "Lorem Ipsum"
    	self.rw_model = 'Lorem Ipsum2'
    	self.ideal_model = 'Lorem Ipsum3'
    	# temporary assumptions
    	self.Numerical_truth_value = random.randint(0,2)
    	self.assumption_text = 'Lorem Ipsumus'
    	self.reason_list = [(bool(random.getrandbits(1)),'Lorem Ipsum1'),(bool(random.getrandbits(1)), "Lorem Ipsum2")]
    	self.temp_assumption = Assumption(self.Numerical_truth_value,self.assumption_text,self.reason_list)

    	self.Numerical_truth_value1 = random.randint(0,2)
    	self.assumption_text1 = 'Lorem Ipsumus'
    	self.reason_list1 = [(bool(random.getrandbits(1)),'Lorem Ipsum1'),(bool(random.getrandbits(1)), "Lorem Ipsum2")]
    	self.temp_assumption1 = Assumption(self.Numerical_truth_value1,self.assumption_text1,self.reason_list1)
    	self.assumptions = [self.temp_assumption]
    	self.temp_question = Question(self.name,self.rw_model,self.ideal_model,self.assumptions)
        self.temp_question.addAssumption(self.Numerical_truth_value1,self.assumption_text,self.reason_list1)
        self.assertEqual(self.temp_question.assumptions[-1].getAssumptionText(), self.temp_assumption1.getAssumptionText())
    


if __name__ == '__main__':
    unittest.main()