import argparse
from os import path
from Components.StartFlowDroid import runFlowDroid
from UserParser.UserParserComponent import  parseP
from UserParser.UserParserComponent import ParseFD
import UserParser.UserParserComponent
import os
import glob
droidalicius_DIR = os.getcwd() + "/"
output_folder = droidalicius_DIR + "Components/Analysis_Output/"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str , help="get the result")
    parser.add_argument("--fd_options", type=str , required=False, help=" Enter the option of FlowDroid ")
    args = parser.parse_args()

    file_dir =args.file
    fd_options=args.fd_options.__str__()

    isDirValide(file_dir)

    if(path.basename(file_dir).endswith(".apk")):
        analysis_Result_file= runFlowDroid(file_dir,fd_options)
        if(not analysis_Result_file): exit() #exit if time out
        print(analysis_Result_file)
    elif (path.basename(file_dir).endswith(".txt")):
             analysis_Result_file = file_dir
    else:
     print("file type  not supported")
     exit()

    print("parsing the analysis output")
    #path_FD_Result = findTxtFile(analysis_Result_file)

    #UserParser.UserParserComponent.finderror(analysis_Result_file)

    App= parseP(ParseFD(droidalicius_DIR+"UserParser/", analysis_Result_file,output_folder ))
    print (App)
    print("Parser done")

  #  delete_Output() # delete all the outpute during the analysis and parsing :)

def isDirValide(file_dir):
    if(not path.exists(file_dir)):
        print("Cant find the file")
        exit()


    file_name = path.basename(file_dir)

    if (not path.isdir(file_dir.replace(file_name, ""))):
        print("The path does not exists")
        exit()

def findTxtFile(analysis_Result_file):
    current_dir=os.getcwd()
    return (current_dir + "/Components/Analysis_Output/"+analysis_Result_file)

def delete_Output():
   os.chdir(output_folder)
   for root,dir,files in os.walk(output_folder):
       for f in files:
           if (path.isfile(f)):
            print(path.basename(f))
            os.remove(f)
os.chdir(droidalicius_DIR)




if __name__ == "__main__":
    main()
