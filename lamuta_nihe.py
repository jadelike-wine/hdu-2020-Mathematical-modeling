# coding: utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

s=11000000
china = pd.read_csv('wuhan_30.csv', encoding='GBK')
data=china.iloc[::].values
k=list()
for i in range(30):
    k.append(data[i][4]/((s-data[i][1])*data[i][1]))
    print(k[i])
'''
for i in range(30):
    k.append(data[i][1]/((s-data[i][2])*data[i][2]))
    print(k[i])
'''


x = np.arange(1, len(k)+1, 1)
y = np.array(k)
z1 = np.polyfit(x, y,5)#用5次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)
plot1=plt.plot(x, y, '*')
plot2=plt.plot(x, yvals, 'r')
plt.legend(loc=4)
plt.show()
#           5             4             3             2
#1.387e-15 x - 1.928e-13 x + 9.214e-12 x - 1.569e-10 x - 2.564e-10 x + 2.653e-08