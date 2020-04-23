import os
from os import path
from colorama import Fore
import sys
from subprocess import Popen
from subprocess import TimeoutExpired
import subprocess

#droidalicius_DIR = + "/"

flowDroid_Dir =  os.getcwd() + "/Flowdroid"
Analysis_Output_dir = os.getcwd() + '/Analysis_Output'
cmd_Headr = " java -Xmx10G -cp soot-trunk.jar;soot-infoflow.jar;soot-infoflow-android.jar;slf4j-api-1.7.5.jar;slf4j-simple-1.7.5.jar;axml-2.0.jar soot.jimple.infoflow.android.TestApps.Test"



def runFlowDroid(apk_dir, options,sdk_path):
    OPTIONS = ""
    space=' '

    if(not options.__contains__("None")): # if user change the defualt options
        OPTIONS=options



    resultFile = os.path.basename(apk_dir).replace(".apk", "_FD.txt").replace(" ","_")

    cmd = cmd_Headr + " \"" + apk_dir + "\" " + sdk_path +space+OPTIONS
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
        print("Analysis is done")
        return (Analysis_Output_dir+"/"+resultFile)
    else:
        print(Fore.RED+"Static analysis timeout ")
        return False


