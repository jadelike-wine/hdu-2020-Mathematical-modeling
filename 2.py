import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math

n=11000000
i0=1
p=0
k=[1,1,2,5,5,5,8,8,12,14,16,25,29,37,40,45,47,49,59,68,78,90,102]
k2=list()
for i in range(3,len(k)):
    cnt=(n*i0/k[i]-i0)/(n-i0)
    k2.append((-math.log(cnt))/(i+1))
x = np.arange(1, len(k2)+1,1)
y = np.array(k2)
z1 = np.polyfit(x, y,5)#用5次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)
plot1=plt.plot(x, y, '*')
plot2=plt.plot(x, yvals, 'r')
plt.show()