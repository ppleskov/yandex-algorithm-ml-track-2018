#blend_all folder is here https://drive.google.com/open?id=1dzOJX4eBqFekAh5ZQPv31jq3qfyKwO0h

import pandas as pd
import numpy as np
from tqdm import tqdm
from os import listdir
from collections import defaultdict
import operator

path = "./blend_all/"
files  = listdir(path)

d = defaultdict(lambda:defaultdict(lambda:0))

for f in tqdm(files):
    df = pd.read_csv(path+f,sep="\t",header=None)
    if len(df.columns)==3:
        for i,j,k in zip(df[0],df[1],df[2]):
            if f.endswith("_r.tsv"):
                d[i][j]+=k/len(files)/2.22
            else:
                d[i][j]+=k/len(files)
    else:
        for i,j,k,l in zip(df[0],df[1],df[2],df[3]):
            d[i][j]+=(k/1.5+l)/len(files)*2.5

res = []
for i in sorted(list(set(df[0]))):
    for j in [c[0] for c in sorted(d[i].items(), key=operator.itemgetter(1), reverse=True)]:
        res.append(j)
        
df[1] = res
df.to_csv("blend_all.csv.gz", sep="\t", header=False, index=False, columns=[0,1], compression='gzip')

#87302 LB
