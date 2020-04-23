from unittest import TestCase
import main
import sys
import unittest
import parser
import argparse
import os, random

apkFile="F:\Project\App\com_makeup_girls_tutorials-1.apk"
txtFile="F:\Project\App\com_makeup_girls_tutorials-1FlowDroidResults.txt"
emptyfile= "C:\\Users\shosho\Documents\\apks\Angry_Birds_1_3_5.apk"
sdk_dir="c:/tools/platforms"
benign_pool="C:\\Users\shosho\DroidLicious\TestSet\B"
mal_pool="C:\\Users\shosho\DroidLicious\TestSet\M"
Error_msgFD='F:\Project\App\Error_Msg.txt' # contain error masg (


class Test1(TestCase):
#Analyzing apk without sdk dir
    def test_main(self):
        apkFile = mal_pool + '\\' + random.choice(os.listdir(mal_pool))
        with self.assertRaises(SystemExit):
            main.main(apkFile,None,None,True)

class Test2(TestCase):
#Analyzing  empty file
    def test_main(self):
        with self.assertRaises(SystemExit):
            main.main(emptyfile,None,None,True)


class Test3(TestCase):
#Analyzing apk with Fd options
    def test_main(self):
           self.assertEqual(main.main(apkFile,'Alflow insen noback',sdk_dir,False),None)


class Test4(TestCase):
    # parsing txt file
    def test_main(self):
            self.assertEqual(main.main(txtFile, None, None,False),None)

class Test5(TestCase):
# input empty file
    def test_main(self):
        with self.assertRaises(SystemExit):
            main.main(emptyfile, None, None, False)

class Test6(TestCase):
    #testing malware
    def test_main(self):
        mal_file = mal_pool + '\\' + random.choice(os.listdir(mal_pool))
        print(mal_file)
        self.assertEqual(main.main(mal_file,None,sdk_dir,None),"has Malware like bahvior")

class Test7(TestCase):
    # testing benign apps
    def test_main(self):
        ben_file = benign_pool + '\\' + random.choice(os.listdir(benign_pool))
        self.assertEqual(main.main(ben_file, None, sdk_dir, None),"benign like bahvior")

class Test7(TestCase):
    # testing benign apps
    def test_main(self):
        with self.assertRaises(SystemExit):
            main.main(Error_msgFD, None, None, False)
