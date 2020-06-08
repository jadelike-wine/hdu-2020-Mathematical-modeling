import requests 
import json
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

s=66488991
e = pd.read_csv('123.csv', encoding='GBK')
data=e.iloc[::].values
for i in range(1,31):
    x=i
    la=7.69e-15*x**5 - 6.74e-13* x**4 + 2.163e-11* x**3 - 3.067e-10* x**2 + 1.695e-09* x + 1.225e-09
    #u=(data[i-1][4]*2-data[i-1][5])/data[i-1][1]
    u=-0.0001924*x**2 - 0.008273*x + 0.5168
    st=(la*data[i-1][2]+1+u+la*(s-data[i-1][2])-math.sqrt(((la*data[i-1][2]+1+u+la*(s-data[i-1][2]))**2-4*la*(1+u))))/(2*la)
    it=data[i-1][2]/(1+u+-la*st)
    it=it*50
    print(str(st)+' '+str(it))