import os,sys
dirname = os.path.dirname(__file__)
dirname = "/".join(dirname.split("/")[:-1])
sys.path.append(dirname)

from MinMaxScale import MinMaxScale
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

if __name__=="__main__":
    # f=pd.read_csv("./unitTest/diabetes.csv")
    f=pd.read_csv("./unitTest/advertisements.csv").iloc[:,:5]
    s=MinMaxScale()
    # print(f.iloc[:5,:5])
    # s.fit(f.iloc[:5,:5])
    # print(s.transform(f.iloc[:5,:5]))
    org=pd.DataFrame(MinMaxScaler().fit_transform(f),columns=f.columns)
    my=s.fit_transform(f)
    print(np.allclose(org,my))
    # print(pd.DataFrame(MinMaxScaler().fit_transform(f),columns=f.columns))
    # print(s.fit_transform(f))