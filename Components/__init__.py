
from os import path


def finderror():
    pathfile = 'F:\Project\Flowdroid\\apk\APp\MX_FD.txt'
    with open(pathfile) as f:
        if (path.getsize(pathfile) == 0):
            print("Error during the analysis:you may need to check sdk path")

def main():
    print(set_option("af len 6 stat src"))

def set_option(input_option):
    fd_option = ""
    space=' '
    arr=input_option.split(' ')
    if(arr.__contains__('af')):
        fd_option+='--aliasflowins'+space

    if (arr.__contains__('stat')):
        fd_option += '--static'+space
    elif(arr.__contains__('nostat')):
        fd_option += '--nostatic'+space

    if (arr.__contains__('len')):
        i = arr.index('len')+1
        fd_option += '--aplength ' + arr[i]+space
        if(not arr[i].isdecimal()):
            print("enter length correctly")
            exit()

    if (arr.__contains__('noback')):
        fd_option += '--nocallbacks'+space

    if (arr.__contains__('src')):
        fd_option += '--pathalgo sourcesonly'+space
    if (arr.__contains__('sen')):
        fd_option += '--pathalgo contextsensitive'+space
    if (arr.__contains__('insen')):
        fd_option += '--pathalgo contextinsensitive'+space

    if (arr.__contains__('nopaths')):
        fd_option += '--nopaths'+space

    if (arr.__contains__('nosize')):
        fd_option += '--noarraysize'+space

    if (arr.__contains__('nopaths')):
        fd_option += '--nopaths'+space

    return fd_option

if __name__ == "__main__":
    main()