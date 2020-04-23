import argparse
from os import path
from StartFlowDroid import runFlowDroid
from UserParserComponent import parser_run ,get_featureNames
import os
import pickle
import sklearn
import numpy as np
from colorama import Fore,init
import sklearn.ensemble._forest


drd_dir = os.getcwd() + "/"  #droidlicious working dircroty
output_folder = drd_dir + "Analysis_Output/"

init(autoreset=True)# color




def  main(file_path,input_options,sdk_path,report):# the working flow start from here

    fd_options= set_option(input_options) # parsing the option to match for flowdroid

    isDirValide(file_path)
####################################################Flowdroid step####################################################
    if (not path.exists(output_folder)):  # if the ouput folder not exists
        os.mkdir(output_folder)

    if(path.basename(file_path).endswith(".apk")):

        if(sdk_path.__eq__('None')): #must  enter SDK folder
            print("To analyze apk file, must enter -sdk")
            exit()
        elif (not path.isdir(sdk_path)):
            print(Fore.RED+ 'No such directory : '+sdk_path)
            exit()

        analysis_Result_file= runFlowDroid(file_path,fd_options,sdk_path)

        if(not analysis_Result_file): exit() #exit if analysis time out

    ####################################################parser step####################################################

    elif (path.basename(file_path).endswith(".txt")): # .txt file only need parsing
             analysis_Result_file = file_path
    else:
     print(Fore.RED+"file type  not supported")
    # return "file type  not supported"
     exit()

    finderror(analysis_Result_file)

    print("Parsing the analysis output")

    App= parser_run(analysis_Result_file,output_folder)
    featuresName=get_featureNames()
    print("Parsing is done")

    if(report):
        if(featuresName=='None'):
            print("The app dataflow does not found in the features ")
        else:
            print(Fore.GREEN+"the founded features :")
            print(featuresName)

    print("Parsing is done")

    os.chdir(drd_dir)
    delete_Output()  # delete all the outpute during the analysis and parsing :)
    print("Classifiying the app")
    ####################################################prediction step####################################################
    result = predict(App)
    if(result[0]==1):
        print(Fore.GREEN+path.basename(file_path)+ " has malicious-like behavior")
    else:
       print(Fore.GREEN+path.basename(file_path) + " does has not has malicious-like behavior")

def isDirValide(file_dir):
    if(not path.exists(file_dir)):
        print(Fore.RED+' No such file or directory: '+file_dir)
        exit()
    if(path.getsize(file_dir)==0):
        print (Fore.RED+"File is empty")
        exit()


def predict(X_test):
    sample=np.array(X_test[1:]) ##
    k= sample.reshape(1,-1)
   # print(k)
    model_file ='rndfst.sav'
    load_lr_model = pickle.load(open(model_file, 'rb'))
    y=  load_lr_model.predict(k)
    return y.tolist()


def delete_Output():
   os.chdir(output_folder)
   for root,dir,files in os.walk(output_folder):
       for f in files:
           if (path.isfile(f)):
            os.remove(f)
   os.chdir(drd_dir)

def finderror(path):
    with open(path) as f:
        for line in f:
            if (line.__contains__('Exception in thread "main"')): # error msg from flowdroid
                i =line.find(':')+1
                print(Fore.RED+'Error massage from FlowDroid:'+line[i:])
                exit(0)



def set_option(input_option):
    if(input_option.__eq__('None')):
        return 'None'

    fd_option = ""
    space = ' '
    arr = input_option.split(' ')
    if (arr.__contains__('Aflow')):
        fd_option += '--aliasflowins' + space

    if (arr.__contains__('stat')):
        fd_option += '--static' + space
    elif (arr.__contains__('nostat')):
        fd_option += '--nostatic' + space

    if (arr.__contains__('len')):
        i = arr.index('len') + 1
        fd_option += '--aplength ' + arr[i] + space
        if (not arr[i].isdecimal()):
            print("enter length correctly")
            exit()
    else:
        fd_option +='--aplength 2'+ space  # defult option
    if (arr.__contains__(' ')):
        fd_option += '--nocallbacks' + space

    if (arr.__contains__('src')):
        fd_option += '--pathalgo sourcesonly' + space
    if (arr.__contains__('sen')):
        fd_option += '--pathalgo contextsensitive' + space
    if (arr.__contains__('insen')):
        fd_option += '--pathalgo contextinsensitive' + space

    if (arr.__contains__('nopaths')):
        fd_option += '--nopaths' + space

    if (arr.__contains__('nosize')):
        fd_option += '--noarraysize' + space

    if (arr.__contains__('nopaths')):
        fd_option += '--nopaths' + space
    return fd_option


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help="")
    parser.add_argument("-op", type=str, required=False, dest='options', help=" FlowDroid options")
    parser.add_argument('-sdk', type=str, required=False, action='store', dest="sdks", help="Android SDK directory")
    parser.add_argument('-report', required=False,action='store_true',dest='report',help='Get the features name')
    parser.add_argument('-version', action='version', version='DroidLicious 1.0')

    args = parser.parse_args()
    file_path = args.file
    input_options = args.options
    sdk_path = args.sdks
    report=args.report
    main(file_path,input_options,sdk_path,report)