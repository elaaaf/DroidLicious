import pandas as pd
import os
import re
import timeit

path = "Parsed .txt files path extracted from Parser_P1.java"
names = []
dataflows = []
dataflow = []
for filename in os.listdir(path):
    if (filename == ".DS_Store"):
        continue
    with open(path+"/"+filename) as f:
        names.append(os.path.basename(filename)[:-6])
        for line in f:
            file = open(path+"/"+filename,"r")
            #dataflow.append(line.rstrip('\n'))
            dataflow.append(line)
        dataflows.append(dataflow)
        dataflow = []

df = pd.DataFrame({"Name":names,"Dataflows":dataflows})

name = []
src = []
snk = []
index = 0

#for i in range (0, (len(df["Name"]))):

start = timeit.default_timer()
for i in range (0, len(df["Name"])):
    for j in range (0, (len(df["Dataflows"]))):
        if(df["Dataflows"][j] == []):
            name.append(df["Name"][j])
            src.append("NO_SENSITIVE_SOURCE")
            snk.append("NO_SENSITIVE_SINK")
        else:
            for w in range (0, (len(df["Dataflows"][j]))):
                name.append(df["Name"][j])
                #index = (re.search("<*...", df["Dataflows"][j][w]).start())+1
                index = re.match(r"<.*>\s~", df["Dataflows"][j][w]).span()[1]-1
                #print(re.match(r"<.*>\s~", df["Dataflows"][j][w]).span()[1]-1)
                snk.append(df["Dataflows"][j][w][:(index-1)])
                src.append(df["Dataflows"][j][w][(index+3):])

stop = timeit.default_timer()

print('Time: ', stop - start, "s")  

df_final = pd.DataFrame({"Name":name,"Source":src, "Sink":snk})
df_final.to_csv("final.csv")
