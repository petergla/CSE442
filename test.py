import unittest
from assumption import Assumption
from question import Question
import random
# Author: Paata Ugrekhelidze


# returns a unique assumption
def get_random_assumption():
    Numerical_truth_value = random.randint(0,2) #always randomize truthvalues and texts for every test run
    assumption_text = 'Lorem Ipsum{}'.format(random.randint(0,1000))
    reason_list = [(bool(random.getrandbits(1)),'Lorem Ipsum{}'.format(random.randint(0,1000))),(bool(random.getrandbits(1)), 'Lorem Ipsum{}'.format(random.randint(0,1000)))] #always randomize boolean values for reason list
    temp_assumption = Assumption(Numerical_truth_value,assumption_text,reason_list)
    return temp_assumption

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
    	
    	self.temp_assumption = get_random_assumption()
        self.test_value = bool(random.getrandbits(1))
        self.test_reason = "Lorem Ipsum{}".format(random.randint(0,1000)) #randomize
        self.temp_assumption.add_reason(self.test_value,self.test_reason)
        self.assertEqual(self.temp_assumption.reason_list[-1], (self.test_value,self.test_reason))
    # test cases for question library
    # tests addAssumption function in question library
    def test_addAssumption(self):
    	# temporary assumptions
    	self.temp_assumption = get_random_assumption()
    	self.temp_assumption1 = get_random_assumption()
    	self.assumptions = [self.temp_assumption]
        # temporary question
        self.name = "Lorem Ipsum{}".format(random.randint(0,1000)) # randomize string inputs
        self.rw_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.ideal_model = "Lorem Ipsum{}".format(random.randint(0,1000))
    	self.temp_question = Question(self.name,self.rw_model,self.ideal_model,self.assumptions)
        self.temp_question.addAssumption(self.temp_assumption1)
        self.assertEqual(self.temp_question.assumptions[-1].getAssumptionText(), self.temp_assumption1.getAssumptionText())
    
    # test whether an assumption is properly removed
    def test_removeAssumption(self):
        # temporary assumptions
        self.temp_assumption = get_random_assumption()
        self.temp_assumption1 = get_random_assumption()
        self.assumptions = [self.temp_assumption,self.temp_assumption1]
        # temporary question
        self.name = "Lorem Ipsum{}".format(random.randint(0,1000)) # randomize string inputs
        self.rw_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.ideal_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.temp_question = Question(self.name,self.rw_model,self.ideal_model,self.assumptions)
        randomizer = random.randint(0,1)
        self.target_assumption = self.assumptions[randomizer-1]
        
        self.temp_question.removeAssumption(randomizer)

        # compare the assumption text of what was now removed
        self.assertEqual(self.temp_question.assumptions[0].getAssumptionText(), self.target_assumption.getAssumptionText())
            
    
    # test whether a name could be retrieved
    def test_getName(self):
        self.temp_assumption = get_random_assumption()
        self.temp_assumption1 = get_random_assumption()
        self.assumptions = [self.temp_assumption,self.temp_assumption1]
        # temporary question
        self.name = "Lorem Ipsum{}".format(random.randint(0,1000)) # randomize string inputs
        self.rw_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.ideal_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.temp_question = Question(self.name,self.rw_model,self.ideal_model,self.assumptions)
        self.assertEqual(self.temp_question.getName(),self.name)
    # check whether assumptions list could be retrieved with a right order
    def test_getAssumptions(self):
        self.temp_assumption = get_random_assumption()
        self.temp_assumption1 = get_random_assumption()
        self.assumptions = [self.temp_assumption,self.temp_assumption1]
        # temporary question
        self.name = "Lorem Ipsum{}".format(random.randint(0,1000)) # randomize string inputs
        self.rw_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.ideal_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.temp_question = Question(self.name,self.rw_model,self.ideal_model,self.assumptions)
        self.assertEqual(self.temp_question.getAssumptions(),self.assumptions)
    # test whether ideal model image path cpuld be retrieved
    def test_getIdealizedModel(self):
        self.temp_assumption = get_random_assumption()
        self.temp_assumption1 = get_random_assumption()
        self.assumptions = [self.temp_assumption,self.temp_assumption1]
        # temporary question
        self.name = "Lorem Ipsum{}".format(random.randint(0,1000)) # randomize string inputs
        self.rw_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.ideal_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.temp_question = Question(self.name,self.rw_model,self.ideal_model,self.assumptions)
        self.assertEqual(self.temp_question.getIdealizedModel(),self.ideal_model)
    # test wheter realworld image path could be retrieved
    def test_getRealWorldModel(self):
        self.temp_assumption = get_random_assumption()
        self.temp_assumption1 = get_random_assumption()
        self.assumptions = [self.temp_assumption,self.temp_assumption1]
        # temporary question
        self.name = "Lorem Ipsum{}".format(random.randint(0,1000)) # randomize string inputs
        self.rw_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.ideal_model = "Lorem Ipsum{}".format(random.randint(0,1000))
        self.temp_question = Question(self.name,self.rw_model,self.ideal_model,self.assumptions)
        self.assertEqual(self.temp_question.getRealWorldModel(),self.rw_model)



if __name__ == '__main__':
    unittest.main()