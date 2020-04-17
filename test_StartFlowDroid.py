from unittest import TestCase
from StartFlowDroid import runFlowDroid
from os import path
import os
longtime_apk='F:\Project\App\MX_Player_v1.14.5_apkpure.apk'
# you can download this app if want or try any other app but make sure it takes more than 5 min with FD (https://apkpure.com/mx-player/com.mxtech.videoplayer.ad/download)
shortime_apk='F:\Project\App\Angry Birds 1_3_5.apk'
jar_dir='c:/tools/platforms' #changed to your jars directory
Anaylsis_output=os.getcwd()+'/Analysis_Output/'

class TestTimeout(TestCase):
    def test_run_flow_droid(self): #testing long time analysis
       self.assertFalse(runFlowDroid(longtime_apk,'',jar_dir))


class TestResult(TestCase):
    def test_run_flow_droid(self): #testing short time analysis
        result=Anaylsis_output+path.basename(shortime_apk).replace('.apk', '_FD.txt').replace(" ","_")
        result=result.replace('/','_').replace('\\','_')
        self.assertEqual(runFlowDroid(shortime_apk,'',jar_dir).replace('\\','_').replace('/','_'),result)


