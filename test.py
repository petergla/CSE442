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

        # temporary assumptions
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

        # temporary assumptions
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

        # temporary assumptions
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
    
    def test_readWeight(self):

        # create a random weight for the function to read
        actual_weight = round(random.uniform(0.1, 1000.0),3)
        # pass the "Reason Weight" line the way it would be read from the textfile
        test_weight = reader.readWeight("R",'Reason Weight: {}\n'.format(actual_weight))
        self.assertEqual(test_weight,actual_weight)


    # testing the function that is supposed to be reading the text file that defines question format. It is supposed to be returning list of question objects
    # the test will read the text predefined. Afterwards, it will choose a random assumption from a random question to compare to the actual assumption
    def test_readFile(self):

        # temporary assumptions for question 1
        Numerical_truth_value = True 
        assumption_text = 'Hip acts as a pivot point (no lifting off the bed)'
        reason_list = []
        temp_assumption1 = Assumption(Numerical_truth_value,assumption_text,reason_list)

        Numerical_truth_value2 = False 
        assumption_text2 = 'Incorrect Assumption #1.1'
        reason_list2 = [(True, "Valid reason #1.1.1"), (False,"Invalid Reason #1.1.2"),(False, "Invalid Reason #1.1.3")]
        temp_assumption2 = Assumption(Numerical_truth_value2,assumption_text2,reason_list2)

        Numerical_truth_value3 = True 
        assumption_text3 = 'Hip acts as a pivot point (no lifting off the bed)'
        reason_list3 = []
        temp_assumption3 = Assumption(Numerical_truth_value2,assumption_text2,reason_list2)
        assumptions1 = [temp_assumption1,temp_assumption2,temp_assumption3]

        # temporary question 1
        name1 = "Question 1"
        rw_model1 = "RealWorld_1.gif"
        ideal_model1 = "IdealizedModel1_1.gif"
        temp_question = Question(name1,rw_model1,ideal_model1,assumptions1)



        # temporary assumptions for question 2
        Numerical_truth_value2_1 = True 
        assumption_text2_1 = 'Forces are reasonably approximated using static analysis'
        reason_list2_1 = []
        temp_assumption2_1 = Assumption(Numerical_truth_value2_1,assumption_text2_1,reason_list2_1)

        Numerical_truth_value2_2 = True 
        assumption_text2_2 = 'Lower leg remains approximately perpendicular to upper leg'
        reason_list2_2 = []
        temp_assumption2_2 = Assumption(Numerical_truth_value2_2,assumption_text2_2,reason_list2_2)

        Numerical_truth_value2_3 = True 
        assumption_text2_3 = 'Hip acts as a pivot point (no lifting off the bed)'
        reason_list2_3 = []
        temp_assumption2_3 = Assumption(Numerical_truth_value2_3,assumption_text2_3,reason_list2_3)

        Numerical_truth_value2_4 = True 
        assumption_text2_4 = 'Patient does not slide on the bed'
        reason_list2_4 = []
        temp_assumption2_4 = Assumption(Numerical_truth_value2_4,assumption_text2_4,reason_list2_4)
        assumptions2 = [temp_assumption2_1,temp_assumption2_2,temp_assumption2_3,temp_assumption2_4]

        # temporary question 2
        name2 = "Question 2"
        rw_model2 = "RealWorld_1.gif"
        ideal_model2 = "IdealizedModel2.gif"
        temp_question2 = Question(name2,rw_model2,ideal_model2,assumptions2)
        
        actual_questions = [temp_question,temp_question2]
        testing_questions = reader.readFile("test_questions.txt")
        random_question = random.randint(0,1)
        random_assumption = random.randint(0,3)
        

        # Comparison
        self.assertEqual(testing_questions[random_question].getAssumptions()[random_assumption].getAssumptionText(),actual_questions[random_question].getAssumptions()[random_assumption].getAssumptionText())


if __name__ == '__main__':
    unittest.main()