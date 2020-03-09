import os
from os import path

import sys
from subprocess import Popen
from subprocess import TimeoutExpired
import subprocess

droidalicius_DIR = os.getcwd() + "/"

JARS_dir = "C:\Tools\platforms"  # change later
flowDroid_Dir = droidalicius_DIR + "Components/FlowDroid/"
Analysis_Output_dir = droidalicius_DIR + "Components/Analysis_Output"

cmd_Headr = " java -Xmx10G -cp soot-trunk.jar;soot-infoflow.jar;soot-infoflow-android.jar;slf4j-api-1.7.5.jar;slf4j-simple-1.7.5.jar;axml-2.0.jar soot.jimple.infoflow.android.TestApps.Test"
OPTIONS = "--static  --aliasflowsen --callbacks --layoutmode none --noarraysize --aplength 5 --pathalgo sourcesonly"


def runFlowDroid(apk_dir):
    apk_dir = Apk_dir_validity(apk_dir)  # cleaning the dir

    if (not path.exists(Analysis_Output_dir)):  # if the analysis folder not exists
        os.mkdir(Analysis_Output_dir)

    resultFile = os.path.basename(apk_dir).replace(".apk", "FlowDroidResult.txt")
    cmd = cmd_Headr + " \"" + apk_dir + "\" " + JARS_dir + " --static  --aliasflowsen --callbacks --layoutmode none --noarraysize --aplength 5 --pathalgo sourcesonly"

    os.chdir(flowDroid_Dir)  # go to FlowDroid folder to run the command
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    os.chdir(Analysis_Output_dir)
    timeout = False
    print("Flowdroid is working now ")

    try:
        stdout, stderr = process.communicate(timeout=5 * 60) # five minutes
    except TimeoutExpired:
        timeout = True
        process.terminate()

    if (not timeout):
        with open(resultFile, "w") as output:
            output.write(str(stdout).replace("\\n", "\n").replace("\\t", "\t").replace("\\r", " "))
            print("analysis is done")
        return True
    else:
        print("Static analysis timeout ")
        return False


def Apk_dir_validity(APK_dir): # add more
    apk_name = os.path.basename(APK_dir)
    if (' ' in apk_name):
        apk_name = apk_name.replace(" ", "_")
        apk_dir = APK_dir.replace(os.path.basename(APK_dir), apk_name)

        if ('\a' in apk_dir):
            apk_dir = apk_dir.replace('\a', '\\a')

        if ('\r' in apk_dir):
            apk_dir = apk_dir.replace('\r', '\\r')
    return APK_dir
