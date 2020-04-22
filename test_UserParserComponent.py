from unittest import TestCase
import UserParserComponent
import os
Error_msgFD='F:\Project\App\Error_Msg.txt' # contain error masg (
file='F:\Project\App\com_kiddoware_kidspictureviewer-8_FD.txt'
noflowFile="F:\Project\App\\air_com_iojoe_A9FlowDroidResults.txt"
output_folder = os.getcwd() + "/Analysis_Output/"

class TestCase1(TestCase):
    def test_finderror(self):# print the error massge and exit
        with self.assertRaises(SystemExit):
            UserParserComponent.finderror(Error_msgFD)



class TestCase2(TestCase):
    def test_finderror(self): #no error
        self.assertEqual(UserParserComponent.finderror(file),None)

    def test_fill_template(self): # ensure the output of the temp list equle to the number of the model's features
        self.assertEqual(UserParserComponent.fillTemplate(file,output_folder).__len__(),101)