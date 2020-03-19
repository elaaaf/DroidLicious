import pandas as pd
import os
import re
import timeit


def readDataflows(path):
    names = []
    dataflows = []
    dataflow = []
    for filename in os.listdir(path):
        if (filename.endswith("_P.txt")):
            with open(path+"/"+filename) as f:
                names.append(os.path.basename(filename)[:-6])
                for line in f:
                    file = open(path+"/"+filename,"r")
                    #temp = file.readlines()
                    dataflow.append(line)
                    #file.close()
                dataflows.append(dataflow)
                dataflow = []
    return names, dataflows

M_path = "Malicious Parsed .txt files path extracted from Parser_P1.java"
B_path = "Benign Parsed .txt files path extracted from Parser_P1.java"

M_names, M_dataflows = readDataflows(M_path)
B_names, B_dataflows = readDataflows(B_path)

M_label = [1]*(len(M_names))
B_label = [0]*(len(B_names))

df = pd.DataFrame({"Name":(M_names+B_names),"Dataflows":(M_dataflows+B_dataflows), "Label":(M_label+B_label)})

df.head()

name = []
src = []
snk = []
label = []
index = 0

start = timeit.default_timer()
length = len(df)
for i in range (0, length):
    print("App#%d out of %d" % (i, length))
    for j in range (0, (len(df["Dataflows"][i]))):
        if(df["Dataflows"][i] == []):
            name.append(df["Name"][j])
            src.append("NO_SENSITIVE_SOURCE")
            snk.append("NO_SENSITIVE_SINK")
            label.append(df["Label"][j])
        else:
            name.append(df["Name"][i])
            index = re.match(r".*\s~>", df["Dataflows"][i][j]).span()[1]-1
            src.append(df["Dataflows"][i][j][:(index-1)])
            snk.append(df["Dataflows"][i][j][(index+2):-1])
            label.append(df["Label"][i])
   
 
end = timeit.default_timer()

print('Time: ', end - start, "s")  

df_final = pd.DataFrame({"Name":name,"Source":src, "Sink":snk, "Label":label})
df_final.to_csv("Data/final.csv")
df_final.head(10000)