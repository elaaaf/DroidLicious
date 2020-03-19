#############################Parser##############################
#This compnent parse the output of flowdroid ti pass it to the 
#machine learning compnent and could be used to display to the 
#user the parsed output of flowdroid.
#################################################################

import pandas as pd
import os
import subprocess
import re
import timeit

#INPUT
pathFD = "*_FD.txt"
ParseFDclassPath = "*.class"


############################ParseFD##############################
#############################INPUT###############################
#classPath: put the path of the ParseFD.class file
#FDtxtPath: put the path of the output of flowdroid *_FD.txt
############################OUTPUT###############################
#The path of the new parsed file *_P.txt
##########################DESCRIPTION############################
#This function takes the output of flowdroid and parse it in the
#form of <src> ~> <snk>, It takes only one file The output could 
#be used to be displayed to the user directly through one of the
#commandline options or could be used to get to the final stage 
#of the parser (FD>P) in order to be used in the machine learning
#model to predict if the app have a malicious behavior.
#################################################################

def ParseFD(classPath, FDtxtPath):
    os.chdir(classPath)
    process = subprocess.Popen('java ParseFD '+FDtxtPath, shell=True, stdout=subprocess.PIPE, 
                           stderr=subprocess.STDOUT)
    return (FDtxtPath[:-6]+"P.txt")

############################ParseP###############################
#############################INPUT###############################
#path: put the path of the *_P.txt file
############################OUTPUT###############################
#List of ["AppName", "Source","Sink"]
##########################DESCRIPTION############################
#This function takes the parsed output of flowdroid and parse it
#in the form of a list as decribed above. It's the final stage 
#of the parser (FD>P) and the output is used in the machine 
#learning model to predict if the app have a malicious behavior.
#You can have the *_P.txt from the output of the 
#ParseFD(classPath, FDtxtPath) function
#################################################################
def parseP(path):
    
    #get the file name without the extension
    name = os.path.basename(path)[:-6]
    
    #read and add the dataflows of the app
    dataflows = []
    with open(path) as f:
        for line in f:
            dataflows.append(line)
    
    #prepare the app data to send it to the ML model
    names = []
    src=[]
    snk=[]
    if(dataflows==[]):
        names.append(name)
        src.append("NO_SENSITIVE_SOURCE")
        snk.append("NO_SENSITIVE_SINK")
    else:
        for data in dataflows:
            names.append(name)
            index = re.match(r".*\s~>", data).span()[1]-1 #get the index of the arrow
            src.append(data[:(index-1)]) #before the arrow: src
            snk.append(data[(index+2):-1]) #after the arrow: snk
    App = [names, src, snk] #zip them together
    return App
