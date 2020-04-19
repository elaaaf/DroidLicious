from unittest import TestCase
import main
import sys
import unittest
import parser
import argparse

apkFile="F:\Project\AndroMalyZer_Dataset\Summer\SET10_106APK\com_makeup_girls_tutorials-1.apk"
txtFile="F:\Project\AndroMalyZer_Dataset\Summer\SET10_106APK\com_makeup_girls_tutorials-1FlowDroidResults.txt"
emptyfile= "C:\\Users\shosho\Documents\\apks\Angry_Birds_1_3_5.apk"
sdk_dir="c:/tools/platforms"


class Test1(TestCase):
#Analyzing apk without sdk dir
    def test_main(self):
        with self.assertRaises(SystemExit):
            main.main(apkFile,None,None,True)



class Test2(TestCase):
#Analyzing apk with Fd options
    def test_main(self):
           self.assertEqual(main.main(apkFile,'Alflow insen noback',sdk_dir,True),None)


class Test3(TestCase):
    # parsing txt file
    def test_main(self):
            self.assertEqual(main.main(txtFile, None, None,False),None) # no error

class Test4(TestCase):
# parsing txt file
    def test_main(self):
        with self.assertRaises(SystemExit):
            main.main(emptyfile, None, None, False) # no error