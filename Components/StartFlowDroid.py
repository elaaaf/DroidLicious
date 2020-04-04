import os
from os import path

import sys
from subprocess import Popen
from subprocess import TimeoutExpired
import subprocess

droidalicius_DIR = os.getcwd() + "/"

flowDroid_Dir = droidalicius_DIR + "Components/FlowDroid/"
JARS_dir = "C:/Tools/platforms "  # change later , still trying to find better way
# PERHAPS BETTER TO GET THE PATH FROM USER

Analysis_Output_dir = droidalicius_DIR + "Components/Analysis_Output"

cmd_Headr = " java -Xmx10G -cp soot-trunk.jar;soot-infoflow.jar;soot-infoflow-android.jar;slf4j-api-1.7.5.jar;slf4j-simple-1.7.5.jar;axml-2.0.jar soot.jimple.infoflow.android.TestApps.Test"


def runFlowDroid(apk_dir, option):
    OPTIONS = "--static  --aliasflowsen --callbacks --layoutmode none --noarraysize --aplength 5 --pathalgo sourcesonly"
    # --aplength 5  [ BTTR TO RELAX THE OPTION TO ENSURE EXECUTION OF FD]

    if(not option.__contains__("None")): # if user change the defualt options
        OPTIONS=option

    if (not path.exists(Analysis_Output_dir)):  # if the analysis folder not exists
        os.mkdir(Analysis_Output_dir)

    resultFile = os.path.basename(apk_dir).replace(".apk", "_FD.txt").replace(" ","_")

    cmd = cmd_Headr + " \"" + apk_dir + "\" " + JARS_dir + OPTIONS
    #print(cmd)

    os.chdir(flowDroid_Dir)  # go to FlowDroid folder to run the command
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    os.chdir(Analysis_Output_dir) # go to the output folder to write the file
    timeout = False
    print("Flowdroid is working now ")

    try:
        stdout, stderr = process.communicate(timeout=5 * 60) # five minutes for timeout
    except TimeoutExpired:
        timeout = True
        process.terminate()

    if (not timeout):
        with open(resultFile, "w") as output:
           output.write(str(stdout).replace("\\n", "\n").replace("\\t", "\t").replace("\\r", ""))
        print("analysis is done")
        os.chdir(droidalicius_DIR) # back to working directory
        return (Analysis_Output_dir+"/"+resultFile)
    else:
        print("Static analysis timeout ")
        os.chdir(droidalicius_DIR)
        return False


