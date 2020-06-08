# coding: utf-8
import requests 
import json
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

e = pd.read_csv('wuhan_30.csv', encoding='GBK')
s=11000000
#it=1
'''
for i in range(1,2):
    x=i
    la=1.387e-15*i**5 - 1.928e-13*x**4 + 9.214e-12*x**3 - 1.569e-10*x**2 - 2.564e-10*x + 2.653e-08
    u=-6.782e-06*x**2 + 0.0008275*x + 0.003428
    st=(la*it+1+u+la*(s-it)-math.sqrt(((la*it+1+u+la*(s-it))**2-4*la*(1+u))))/(2*la)
    it=it/(1+u+-la*st)
    print(str(it))
'''


for i in range(48,78):
    it=922
    x=i
    la=1.387e-15*i**5 - 1.928e-13*x**4 + 9.214e-12*x**3 - 1.569e-10*x**2 - 2.564e-10*x + 2.653e-08
    u=-6.782e-06*x**2 + 0.0008275*x + 0.003428
    st=(la*it+1+u+la*(s-it)-math.sqrt(((la*it+1+u+la*(s-it))**2-4*la*(1+u))))/(2*la)
    it=it/(1+u+-la*st)
    print(str(int(it)))
