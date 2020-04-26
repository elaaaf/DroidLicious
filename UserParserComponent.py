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
MLcolumnsList = ['<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.util.Log: int w(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: int getInt(java.lang.String)> ~> <android.util.Log: int i(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getDeviceId()> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putInt(java.lang.String,int)>',
 '<android.telephony.TelephonyManager: java.lang.String getLine1Number()> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <org.apache.http.impl.client.DefaultHttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest)>',
 '<android.telephony.TelephonyManager: java.lang.String getSubscriberId()> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putString(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.util.Log: int i(java.lang.String,java.lang.String)> ',
 '<android.widget.EditText: android.text.Editable getText()> ~> <org.apache.http.impl.client.DefaultHttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest)>',
 '<android.telephony.TelephonyManager: java.lang.String getLine1Number()> ~> <android.util.Log: int v(java.lang.String,java.lang.String)>',
 '<com.kuguo.ad.MainActivity: android.content.Intent getIntent()> ~> <android.util.Log: int e(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getDeviceId()> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<android.location.LocationManager: android.location.Location getLastKnownLocation(java.lang.String)> ~> <android.util.Log: int e(java.lang.String,java.lang.String)>',
 '<com.airpush.android.PushAds: android.content.Intent getIntent()> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,java.lang.String)>',
 '<java.net.URL: java.net.URLConnection openConnection()> ~> <java.io.FileOutputStream: void write(byte[],int,int)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.telephony.SmsManager: void sendMultipartTextMessage(java.lang.String,java.lang.String,java.util.ArrayList,java.util.ArrayList,java.util.ArrayList)>',
 '<android.telephony.TelephonyManager: java.lang.String getLine1Number()> ~> <android.os.Bundle: void putString(java.lang.String,java.lang.String)>',
 '<org.apache.http.impl.client.DefaultHttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest)> ~> <android.util.Log: int i(java.lang.String,java.lang.String)>',
 '<android.database.Cursor: java.lang.String getString(int)> ~> <android.content.ContentResolver: android.database.Cursor query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)>',
 '<org.apache.http.util.EntityUtils: java.lang.String toString(org.apache.http.HttpEntity)> ~> <java.io.FileOutputStream: void write(byte[])>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <java.io.FileOutputStream: void write(byte[])>',
 '<com.google.ads.AdActivity: android.content.Intent getIntent()> ~> <android.util.Log: int e(java.lang.String,java.lang.String)> ',
 '<android.widget.EditText: android.text.Editable getText()> ~> <android.telephony.SmsManager: void sendTextMessage(java.lang.String,java.lang.String,java.lang.String,android.app.PendingIntent,android.app.PendingIntent)>',
 '<android.app.Activity: android.content.Intent getIntent()> ~> <java.net.URL: void init(java.lang.String)> ',
 '<org.apache.http.util.EntityUtils: java.lang.String toString(org.apache.http.HttpEntity,java.lang.String)> ~> <android.util.Log: int d(java.lang.String,java.lang.String)>',
 '<com.bypush.PushActivity: android.content.Intent getIntent()> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,android.os.Parcelable)>',
 '<com.unity3d.stream.c: android.os.Message obtainMessage(int,java.lang.Object)> ~> <com.unity3d.stream.c: boolean sendMessage(android.os.Message)>',
 '<android.database.Cursor: java.lang.String getString(int)> ~> <android.util.Log: int e(java.lang.String,java.lang.String)>',
 '<com.itframework.installer.util.InstallNonMarketFromUrlActivity: android.content.Intent getIntent()> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: java.io.Serializable getSerializable(java.lang.String)> ~> <android.os.Bundle: void putSerializable(java.lang.String,java.io.Serializable)> ',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.util.Log: int e(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getDeviceId()> ~> <java.io.FileOutputStream: void write(byte[])>',
 '<org.apache.http.HttpResponse: org.apache.http.HttpEntity getEntity()> ~> <org.apache.http.client.HttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest)>',
 '<android.os.Bundle: int getInt(java.lang.String)> ~> <java.net.HttpURLConnection: void setRequestProperty(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getLine1Number()> ~> <java.io.OutputStream: void write(byte[])>',
 '<android.widget.EditText: android.text.Editable getText()> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putLong(java.lang.String,long)>',
 '<android.widget.EditText: android.text.Editable getText()> ~> <android.widget.TextView: void setText(java.lang.CharSequence)>',
 '<com.sk.cm.yo.csi.alay: android.content.Intent getIntent()> ~> <android.util.Log: int d(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getSubscriberId()> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<android.os.Handler: android.os.Message obtainMessage(int,java.lang.Object)> ~> <android.os.Handler: boolean sendMessage(android.os.Message)>',
 '<com.tutusw.onekeyvpn.EnterPassphrase: android.content.Intent getIntent()> ~> <android.widget.TextView: void setText(java.lang.CharSequence)>',
 '<android.os.Handler: android.os.Message obtainMessage(int,java.lang.Object)> ~> <android.os.Handler: boolean sendMessage(android.os.Message)> ',
 '<android.app.Activity: android.content.Intent getIntent()> ~> <android.util.Log: int w(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.os.Bundle: void putString(java.lang.String,java.lang.String)> ',
 '<android.telephony.gsm.GsmCellLocation: int getLac()> ~> <java.io.FileOutputStream: void write(byte[])>',
 '<android.telephony.TelephonyManager: java.lang.String getLine1Number()> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putString(java.lang.String,java.lang.String)>',
 '<android.widget.EditText: android.text.Editable getText()> ~> <android.os.Bundle: void putInt(java.lang.String,int)>',
 '<com.google.android.vending.expansion.downloader.impl.CustomIntentService$ServiceHandler: android.os.Message obtainMessage()> ~> <com.google.android.vending.expansion.downloader.impl.CustomIntentService$ServiceHandler: boolean sendMessage(android.os.Message)> ',
 '<java.net.URL: java.net.URLConnection openConnection()> ~> <java.io.OutputStream: void write(byte[],int,int)>',
 '<android.widget.EditText: android.text.Editable getText()> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,android.os.Parcelable)>',
 '<java.net.URL: java.net.URLConnection openConnection()> ~> <java.net.HttpURLConnection: void setRequestProperty(java.lang.String,java.lang.String)>',
 '<android.app.PendingIntent: android.app.PendingIntent getActivity(android.content.Context,int,android.content.Intent,int)> ~> <android.telephony.SmsManager: void sendTextMessage(java.lang.String,java.lang.String,java.lang.String,android.app.PendingIntent,android.app.PendingIntent)>',
 '<android.telephony.TelephonyManager: java.lang.String getSubscriberId()> ~> <android.os.Bundle: void putInt(java.lang.String,int)>',
 '<android.telephony.TelephonyManager: java.lang.String getDeviceId()> ~> <org.json.JSONObject: org.json.JSONObject put(java.lang.String,int)>',
 '<android.os.Bundle: android.os.Parcelable getParcelable(java.lang.String)> ~> <android.os.Bundle: void putParcelable(java.lang.String,android.os.Parcelable)>',
 '<android.os.Bundle: int getInt(java.lang.String,int)> ~> <android.os.Bundle: void putInt(java.lang.String,int)>',
 '<android.database.Cursor: java.lang.String getString(int)> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<java.util.Locale: java.lang.String getCountry()> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putLong(java.lang.String,long)>',
 '<android.os.Bundle: java.lang.Object get(java.lang.String)> ~> <android.util.Log: int d(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putString(java.lang.String,java.lang.String)>',
 '<com.google.ads.AdActivity: android.content.Intent getIntent()> ~> <android.util.Log: int e(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getSubscriberId()> ~> <android.util.Log: int v(java.lang.String,java.lang.String)>',
 '<java.net.URL: java.net.URLConnection openConnection()> ~> <java.net.HttpURLConnection: void setRequestMethod(java.lang.String)>',
 '<android.os.Bundle: java.lang.Object get(java.lang.String)> ~> <android.content.Intent: android.content.Intent setAction(java.lang.String)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.widget.TextView: void setText(java.lang.CharSequence)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.os.Bundle: void putSerializable(java.lang.String,java.io.Serializable)> ',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putInt(java.lang.String,int)>',
 '<com.zhuaz.moban.MSecondHtmlActivity: android.content.Intent getIntent()> ~> <android.widget.TextView: void setText(java.lang.CharSequence)>',
 '<android.content.pm.PackageManager: java.util.List getInstalledPackages(int)> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,java.lang.String)>',
 '<android.widget.EditText: android.text.Editable getText()> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,int)>',
 '<android.app.PendingIntent: android.app.PendingIntent getBroadcast(android.content.Context,int,android.content.Intent,int)> ~> <android.telephony.SmsManager: void sendTextMessage(java.lang.String,java.lang.String,java.lang.String,android.app.PendingIntent,android.app.PendingIntent)>',
 '<android.content.ContentResolver: android.database.Cursor query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)> ~> <android.content.ContentResolver: android.database.Cursor query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)> ',
 'NO_SENSITIVE_SOURCE ~> NO_SENSITIVE_SINK',
 '<android.database.Cursor: java.lang.String getString(int)> ~> <android.util.Log: int d(java.lang.String,java.lang.String)>',
 '<android.app.Activity: android.content.Intent getIntent()> ~> <android.content.Intent: android.content.Intent setAction(java.lang.String)> ',
 '<android.net.wifi.WifiInfo: java.lang.String getMacAddress()> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<android.widget.EditText: android.text.Editable getText()> ~> <android.telephony.SmsManager: void sendMultipartTextMessage(java.lang.String,java.lang.String,java.util.ArrayList,java.util.ArrayList,java.util.ArrayList)>',
 '<ru.jabox.android.smsbox.log.SendLogActivity: android.content.Intent getIntent()> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,java.lang.String[])>',
 '<com.doumob.main.WebViewActivity: android.content.Intent getIntent()> ~> <android.content.Intent: android.content.Intent setData(android.net.Uri)>',
 '<android.app.Activity: android.content.Intent getIntent()> ~> <android.os.Bundle: void putString(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: java.lang.Object get(java.lang.String)> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getDeviceId()> ~> <java.io.OutputStream: void write(byte[])>',
 '<android.app.Activity: android.content.Intent getIntent()> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putFloat(java.lang.String,float)>',
 '<android.app.PendingIntent: android.app.PendingIntent getBroadcast(android.content.Context,int,android.content.Intent,int)> ~> <android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putString(java.lang.String,java.lang.String)> ',
 '<java.net.URL: java.net.URLConnection openConnection()> ~> <java.net.URL: void init(java.lang.String)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.util.Log: int e(java.lang.String,java.lang.String)> ',
 '<com.startapp.android.publish.AppWallActivity: android.content.Intent getIntent()> ~> <java.net.URL: void init(java.lang.String)>',
 '<com.appflood.AFInterstitialActivity: android.content.Intent getIntent()> ~> <android.util.Log: int e(java.lang.String,java.lang.String)>',
 '<android.content.pm.PackageManager: java.util.List getInstalledPackages(int)> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,android.os.Parcelable)>',
 '<android.app.PendingIntent: android.app.PendingIntent getBroadcast(android.content.Context,int,android.content.Intent,int)> ~> <android.content.Context: android.content.ComponentName startService(android.content.Intent)> ',
 '<android.app.Activity: android.content.Intent getIntent()> ~> <android.util.Log: int d(java.lang.String,java.lang.String)> ',
 '<android.os.Bundle: int getInt(java.lang.String)> ~> <android.util.Log: int w(java.lang.String,java.lang.String)>',
 '<com.droidhen.api.scoreclient.ui.HighScoresActivity: android.content.Intent getIntent()> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<android.telephony.TelephonyManager: java.lang.String getSimSerialNumber()> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<android.content.ContentResolver: android.database.Cursor query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)> ~> <android.content.ContentResolver: android.database.Cursor query(android.net.Uri,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String)>',
 '<java.util.Locale: java.lang.String getCountry()> ~> <org.apache.http.message.BasicNameValuePair: void init(java.lang.String,java.lang.String)>',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <android.util.Log: int d(java.lang.String,java.lang.String)> ',
 '<android.os.Bundle: java.lang.String getString(java.lang.String)> ~> <java.net.HttpURLConnection: void setRequestProperty(java.lang.String,java.lang.String)>',
 '<com.facebook.LoginActivity: android.content.Intent getIntent()> ~> <android.os.Bundle: void putString(java.lang.String,java.lang.String)>',
 '<android.database.Cursor: java.lang.String getString(int)> ~> <android.content.Intent: android.content.Intent putExtra(java.lang.String,java.io.Serializable)>',
 '<android.os.Bundle: android.os.Parcelable getParcelable(java.lang.String)> ~> <android.content.Context: void startActivity(android.content.Intent)>']


featureNames = []


def parser_run(FDtxtPath ,Analysis_Output_dir):
    result=fillTemplate(FDtxtPath,Analysis_Output_dir)
    return result



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
def fillTemplate(pathFD,Analysis_Output_dir):
    
    os.chdir(classPath)
    parsedFilePath = Analysis_Output_dir + "/" + path.basename(pathFD).replace('_FD', '_P')
    process = subprocess.Popen('java ParseFD ' + pathFD + ' ' + Analysis_Output_dir, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    process=process.communicate()
    print("-------------------------------------------")

    dataflows = []
    tempList = []

    with open(parsedFilePath) as f:
        for line in f:
            dataflows.append(line[:-1])

    tempList.append(os.path.basename(parsedFilePath)[:-6])
    
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

