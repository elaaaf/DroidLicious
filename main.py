import argparse
from os import path

from Components.StartFlowDroid import runFlowDroid

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str , help="get the result")
    parser.add_argument("--fd_options", type=str , required=False, help=" Enter the option of FlowDroid ")
    args = parser.parse_args()
    file_dir = args.file
    fd_options=args.fd_options.__str__()


    if(path.basename(file_dir).endswith(".apk")):
        if(not runFlowDroid(file_dir,fd_options)): exit()


    elif (path.basename(file_dir).endswith(".txt")):
        print("parser..................")
    else:
        print("file type is not supported")
        exit()









if __name__ == "__main__":
    main()