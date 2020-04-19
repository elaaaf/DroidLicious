from unittest import TestCase
import UserParser.UserParserComponent
import os
Error_msgFD='C:\\Users\shosho\DroidLicious\Analysis_Output\\4G_Speed_UC_FD.txt' # contain error masg (
file='F:\Project\AndroMalyZer_Dataset\APK_NotYetIncluded\\apk_storage1_114apk\com-kiddoware-kidspictureviewer\com_kiddoware_kidspictureviewer-8_FD.txt'
output_folder = os.getcwd() + "/Analysis_Output/"

class TestCase1(TestCase):

    def test_finderror(self):# print the error massge and exit
        with self.assertRaises(SystemExit):
            UserParser.UserParserComponent.finderror(Error_msgFD)



class TestCase2(TestCase):
    def test_finderror(self): #no error find
        self.assertEqual(UserParser.UserParserComponent.finderror(file),None)

    def test_fill_template(self): # ensure the output of the temp list equle to the number of the model's features
        self.assertEqual(UserParser.UserParserComponent.fillTemplate(file,output_folder).__len__(),16)