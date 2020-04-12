import pandas as pd
import os
import re
import timeit
from itertools import repeat


def readDataflows(path):
    names = []
    dataflows = []
    dataflow = []
    for filename in os.listdir(path):
        if (filename.endswith("_P.txt")):
            with open(path+"/"+filename) as f:
                names.append(os.path.basename(filename)[:-6])
                for line in f:
                    dataflow.append(line[:-1])
                dataflows.append(dataflow)
                dataflow = []
    return names, dataflows

M_path = "F:\Project\Parsed Dataset\M"
B_path = "F:\Project\Parsed Dataset\B"

M_names, M_dataflows = readDataflows(M_path)
B_names, B_dataflows = readDataflows(B_path)

M_label = [1]*(len(M_names))
B_label = [0]*(len(B_names))

df = pd.DataFrame({"Name":(M_names+B_names),"Dataflows":(M_dataflows+B_dataflows), "Label":(M_label+B_label)})

df.head()


###############################################
#FORM 2
def fillRows(df):
    col = ["NO_SENSITIVE_SOURCE ~> NO_SENSITIVE_SINK"]
    test = df.Dataflows
    for d in df.Dataflows:
        if (d == []):
            continue
        else:
            for x in d:
                col.append(x)

    print("before ", len(col))
    col_unique = list(dict.fromkeys(col))
    print("after ",len(col_unique))
    entries = []
    tempList = []
    length = len(df)
    for i in range (0, length):
        print("App#%d out of %d" % (i+1, length))
        if(df["Dataflows"][i] == []):
            tempList.append(df["Name"][i])
            tempList.append(1)
            tempList.extend(repeat(0, len(col_unique)-1))
            tempList.append(df["Label"][i])
            entries.append(tempList)
            tempList=[]
        else:
            tempList.append(df["Name"][i])
            for j in range (0, len(col_unique)):
                if col_unique[j] in df["Dataflows"][i]:
                    tempList.append(1)
                else:
                    tempList.append(0)

            tempList.append(df["Label"][i])

            entries.append(tempList)

            tempList = []
    
    col_unique.insert(0, "Name")
    col_unique.insert(len(col_unique)+1, "Label")
    df_new =  pd.DataFrame(entries, columns=col_unique)
    df_new.to_csv("FINAL_DATASET.csv")
    
    
fillRows(df)

###############################################

###############################################
#FORM 1
#name = []
#src = []
#snk = []
#label = []
#index = 0

#start = timeit.default_timer()
#length = len(df)
#for i in range (0, length):
#    print("App#%d out of %d" % (i, length))
#    for j in range (0, (len(df["Dataflows"][i]))):
#        if(df["Dataflows"][i] == []):
#            name.append(df["Name"][j])
#            src.append("NO_SENSITIVE_SOURCE")
#            snk.append("NO_SENSITIVE_SINK")
#            label.append(df["Label"][j])
#        else:
#            name.append(df["Name"][i])
#            index = re.match(r".*\s~>", df["Dataflows"][i][j]).span()[1]-1
#            src.append(df["Dataflows"][i][j][:(index-1)])
#            snk.append(df["Dataflows"][i][j][(index+2):-1])
#            label.append(df["Label"][i])
   
 
#end = timeit.default_timer()

#print('Time: ', end - start, "s")  

#df_final = pd.DataFrame({"Name":name,"Source":src, "Sink":snk, "Label":label})
#df_final.to_csv("Data/final.csv")
#df_final.head(10000)
###############################################
