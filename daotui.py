import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math

s=11000000
a0 = 1.399633073448364E-15
a1 =-1.940500838329903E-13
a2 = 9.258889167520508E-12
a3=-1.576344244255012E-10
a4=-2.525278076622344E-10
a5 = 2.653645633889905E-8
b0 =-7.417684077355750E-6
b1 = 8.544100242301858E-4
b2 = 0.003315039360847


data = pd.read_csv('wuhan_30.csv', encoding='GBK')
data=data.iloc[::].values
for i in range(30):
    x=i+1
    #k=a0*x**5+a1*x**4+a2*x**3+a3*x**2+a4*x+a5
    k=b0*x**2+b1*x+b2
    num=data[i][4]*2-k*data[i][1]
    print(str(int(num)))

