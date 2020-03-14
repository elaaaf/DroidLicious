import argparse
from os import path
from Components.StartFlowDroid import runFlowDroid
import os
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str , help="get the result")
    parser.add_argument("--fd_options", type=str , required=False, help=" Enter the option of FlowDroid ")
    args = parser.parse_args()

    file_dir =args.file
    fd_options=args.fd_options.__str__()

    isDirValide(file_dir)

    if(path.basename(file_dir).endswith(".apk")):

        if(not runFlowDroid(file_dir,fd_options)): exit()


    elif (path.basename(file_dir).endswith(".txt")):
        print("parser..................")
    else:
        print("file type is not supported")
        exit()



def isDirValide(file_dir): # add more

    if(not path.exists(file_dir)):
        print("Cant find the file")
        exit()


    file_name = path.basename(file_dir)

    if (not path.isdir(file_dir.replace(file_name, ""))):
        print("The path does not exists")
        exit()




if __name__ == "__main__":
    main()
