# coding: utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

e = pd.read_csv('eguo.csv', encoding='GBK')
data=e.iloc[::].values

k=list()
for i in range(len(data)):
    k.append(data[i][3])
print(k)


x = np.arange(1, len(k)+1, 1)
y = np.array(k)
z1 = np.polyfit(x, y,3)#用5次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)
plot1=plt.plot(x, y, '*')
plot2=plt.plot(x, yvals, 'r')
plt.legend(loc=4)
plt.show()