import unittest
from assumption import Assumption
from question import Question
import random
import reader
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




    # test cases for reader file
    # testing the function that reads the first line from the question list format
    # supposed to identify the name of the question
    def test_readQuestion(self):
        # create a random first line input (Question name)
        actual_question_name = 'Question {}'.format(random.randint(0,1000))
        # pass the first line the way it would be read from the textfile
        test_question_name = reader.readQuestion('Question: {}\n'.format(actual_question_name))
        self.assertEqual(test_question_name,actual_question_name)
    # testing the function that reads the second/third line from the question list format
    # supposed to identify the name of the idealized/realworld image path  
    def test_readImgPath(self):
        # create a random second line input(Idealized Model)
        actual_ideal_name = 'IdealizedModel1_{}.gif'.format(random.randint(0,1000))
        # pass the second line the way it would be read from the textfile
        test_ideal_name = reader.readImgPath("I",'Idealized Model: {}\n'.format(actual_ideal_name))
        self.assertEqual(test_ideal_name,actual_ideal_name)
    
    # testing the function that reads the fourth line from the question list format
    # supposed to identify the name of the assumption with the text & truth value
    def test_readAssumption(self):
        
        # instantiate an assumption object for the testing purposes
        actual_value = bool(random.getrandbits(1))
        actual_assumption_text = 'Hip acts as a pivot point (no lifting off the bed){}'.format(random.randint(0,1000))
        actual_assumption_input = '{} | {}'.format(actual_assumption_text,actual_value)
        # create the assumption object that should be returned

        actual_assumption = Assumption(actual_value,actual_assumption_text, [])
        # pass the fourth line the way it would be read from the textfile (supposed to return an assumption object)
        test_assumption = reader.readAssumption('Assumption: {}\n'.format(actual_assumption_input))
        self.assertEqual(test_assumption.getAssumptionText(),actual_assumption.getAssumptionText())

    def test_readReason(self):

        # instantiate  an reason object for the testing purposes
        actual_value = bool(random.getrandbits(1))
        actual_reason_text = 'Valid reason #1.1.{}'.format(random.randint(0,1000))
        actual_reason_input = '{} | {}'.format(actual_reason_text,actual_value)
        # create the reason tuple that should be returned

        actual_reason = (actual_value,actual_reason_text)
        # pass the fifth line the way it would be read from the textfile (supposed to return a reason tuple)
        test_reason = reader.readReason('Reason: {}\n'.format(actual_reason_input))
        self.assertEqual(test_reason,actual_reason)
    

    # def test_readFile(self):




if __name__ == '__main__':
    unittest.main()