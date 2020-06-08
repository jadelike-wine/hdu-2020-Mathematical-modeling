# coding: utf-8
import requests 
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

s=11000000
china = pd.read_csv('wuhan_30.csv', encoding='GBK')

data=china.iloc[::].values
k=list()
for i in range(30):
    k.append((data[i][4]*2-data[i][5])/data[i][1])
    print(k[i])


x = np.arange(1, len(k)+1, 1)
y = np.array(k)
z1 = np.polyfit(x, y,2)#用2次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)
plot1=plt.plot(x, y, '*')
plot2=plt.plot(x, yvals, 'r')
plt.legend(loc=4)
plt.show()
#           2
#-6.84e-06 x + 0.0008303 x + 0.003564