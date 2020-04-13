#############################Parser##############################
#This compnent parse the output of flowdroid ti pass it to the 
#machine learning compnent and could be used to display to the 
#user the parsed output of flowdroid.
#################################################################
  

import os
import subprocess
import re
import timeit
from os import path
from colorama import Fore
#INPUT
#pathFD = "/Users/elaafsalem/Downloads/AMD_Anlys/Test/357d366f9b43e8f1acb334d57e7559b3_FD.txt"
classPath = os.getcwd()+"/UserParser/"

MLcolumnsList = [
    '<java.net.URL: java.net.URLConnection openConnection()> ~> <java.net.HttpURLConnection: void setRequestMethod(java.lang.String)>',
    '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.widget.TextView: void setText(java.lang.CharSequence)>',
    '<android.telephony.TelephonyManager: java.lang.String getDeviceId()> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
    '<android.app.PendingIntent: android.app.PendingIntent getBroadcast(android.content.Context,int,android.content.Intent,int)> ~> <android.telephony.SmsManager: void sendTextMessage(java.lang.String,java.lang.String,java.lang.String,android.app.PendingIntent,android.app.PendingIntent)>',
    '<android.telephony.TelephonyManager: java.lang.String getSubscriberId()> ~> <android.os.Bundle: void putString(java.lang.String,java.lang.String)>',
    '<android.telephony.TelephonyManager: java.lang.String getLine1Number()> ~> <android.util.Log: int v(java.lang.String,java.lang.String)>',
    '<android.app.PendingIntent: android.app.PendingIntent getActivity(android.content.Context,int,android.content.Intent,int)> ~> <android.telephony.SmsManager: void sendTextMessage(java.lang.String,java.lang.String,java.lang.String,android.app.PendingIntent,android.app.PendingIntent)>',
    '<android.app.Activity: android.content.Intent getIntent()> ~> <android.util.Log: int w(java.lang.String,java.lang.String)>',
    '<android.app.PendingIntent: android.app.PendingIntent getBroadcast(android.content.Context,int,android.content.Intent,int)> ~> <android.content.Context: android.content.ComponentName startService(android.content.Intent)>',
    '<com.google.ads.AdActivity: android.content.Intent getIntent()> ~> <android.util.Log: int e(java.lang.String,java.lang.String)>',
    '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.os.Bundle: void putString(java.lang.String,java.lang.String)> ',
    '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.util.Log: int d(java.lang.String,java.lang.String)> ',
    '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.util.Log: int e(java.lang.String,java.lang.String)> ',
    '<android.os.Bundle: int getInt(java.lang.String)> ~> <android.os.Bundle: void putInt(java.lang.String,int)> ',
    '<android.os.Bundle: java.io.Serializable getSerializable(java.lang.String)> ~> <android.os.Bundle: void putSerializable(java.lang.String,java.io.Serializable)> ']
featureNames = []


def parser_steps(FDtxtPath ,Analysis_Output_dir):
    finderror(FDtxtPath)
    result=fillTemplate(MLcolumnsList,FDtxtPath,Analysis_Output_dir)
    return result

def finderror(path):
    with open(path) as f:
        for line in f:
            if (line.__contains__('Exception in thread "main"')): # error msg from flowdroid
                i =line.find(':')+1
                print(Fore.RED+'Error massage from FlowDroid:'+line[i:])
                exit(0)


#######CHANGED TO BE DELETED##########################################
def ParseFD(FDtxtPath ,Analysis_Output_dir):
    os.chdir(classPath)
    resultP= Analysis_Output_dir+"/"+ path.basename(FDtxtPath).replace('_FD','_P')
    process = subprocess.Popen('java ParseFD '+FDtxtPath+' '+Analysis_Output_dir, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    #with open(resultP, "w") as output:
     #   output.write(str(stdout))
    print(FDtxtPath+' '+Analysis_Output_dir)
    return (resultP)
  #  return (FDtxtPath[:-6]+"P.txt")
######################################################################




###########################fillTemplate###############################
#############################INPUT###############################
#MLcolumnsList: selected features (columns) from the dataset
#pathFD: flowdroid txt file path
############################OUTPUT###############################
#List of ["AppName", zeros and ones]
#example ["AppX", 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##########################DESCRIPTION############################
#This function takes the output of flowdroid and parse it
#in the form of "src ~> snk". Then it fit its dataflows to our
#dataset (exclude missing features). The output of this function 
#is used in the machine learning model to predict if the app have 
#a malicious behavior.
######################################################################
def fillTemplate(MLcolumnsList,pathFD,Analysis_Output_dir):
    os.chdir(classPath)
    parsedFilePath = Analysis_Output_dir + "/" + path.basename(pathFD).replace('_FD', '_P')
    process = subprocess.Popen('java ParseFD ' + pathFD + ' ' + Analysis_Output_dir, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    process=process.communicate()
    print("-------------------------------------------")

    #parsedFilePath = (pathFD[:-6]+"P.txt")
    #parsedFilePath=resultP
    dataflows = []
    tempList = []

    with open(parsedFilePath) as f:
        for line in f:
            dataflows.append(line[:-1])

    tempList.append(os.path.basename(parsedFilePath)[:-6])#DO WE need the app name ?


    
    if((dataflows == []) & ("NO_SENSITIVE_SOURCE ~> NO_SENSITIVE_SINK" in MLcolumnsList)):
        dataflows.append("NO_SENSITIVE_SOURCE ~> NO_SENSITIVE_SINK")
    
    for i in MLcolumnsList:    
        if i in dataflows:
            tempList.append(1)
            featureNames.append(i)
        else:
            tempList.append(0)
            
    return tempList

def get_featureNames():
    if(featureNames.__len__()==0):
        return 'None'
    return featureNames


###########################EXAMPLE###############################
#print(fillTemplate(MLcolumnsList,pathFD))

