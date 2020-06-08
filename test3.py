import math

for i in range(1,101):
    k=math.e**(-i*0.254596492)
    k=k*(11000000-1)+1
    k=11000000/k
    print(str(int(k)))