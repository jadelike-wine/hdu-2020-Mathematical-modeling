import numpy as np
import pandas as pd
import math

#china = pd.read_csv('123.csv', encoding='GBK')

n=11000000
i0=1
k2=list()
k=[1,1,2,5,5,5,8,8,12,14,16,25,29,37,40,45,47,49,59,68,78,90,102]
for i in range(3,len(k)):
    cnt=(n*i0/k[i]-i0)/(n-i0)
    k2.append((-math.log(cnt))/(i+1))
print(k2)
'''
p/=len(k)-2
print(str(p))
'''
#p=0.2534751872377965