import argparse
from os import path

from Components.StartFlowDroid  import runFlowDroid

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="get the result ", type=str , required=True)
    #parser.add_argument("-op", help=" Enter the option of FlowDroid ", type=str  , required=False)
    args = parser.parse_args()
    file_dir =args.a

    if(path.basename(file_dir).endswith(".apk")):
        if(not  runFlowDroid(file_dir)): exit()

    elif (path.basename(file_dir).endswith(".txt")):
        print("parser..................")
    else:
        print("file type is not supported")
        exit()






""" def Apk_dir_validity(apk_dir):
    apk_name=os.path.basename(apk_dir)
    print(apk_dir)
    if(' ' in apk_name):
        apk_name= apk_name.replace(" ","_")
        apk_dir= apk_dir.replace(os.path.basename(apk_dir),apk_name)
        print(apk_dir)

    if('\a' in apk_dir):
        apk_dir=apk_dir.replace('\a','\\a')
        print(apk_dir)

    if('\r' in apk_dir):
        apk_dir=apk_dir.replace('\r','\\r')
        print(apk_dir)


def runFD():
    resultFile= os.path.basename(apk).replace(".apk","FlowDroidResult.txt")
    cmd =FlowDroidcmd+" \""+ apk+"\" " +jar+" --static  --aliasflowsen --callbacks --layoutmode none --noarraysize --aplength 5 --pathalgo sourcesonly"

    print(cmd)

    origen_wd = os.getcwd()
    os.chdir(flowDroid_Dir)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    os.chdir(Analysis_Output_dir)
    timeout= False 

    try:
        stdout,stderr=  process.communicate(timeout=5*60)
    except TimeoutExpired:
        timeout=True
        process.terminate()

    if(not timeout):
     with open(resultFile, "w") as output:
            output.write(str(stdout).replace("\\n","\n").replace("\\t","\t").replace("\\r"," "))
            print("analysis is done")
    else:
        print("Static analysis timeout ")"""
















if __name__ == "__main__":
    main()