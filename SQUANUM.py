# tim so chinh phuong
from math import sqrt
fi=open("SQUANUM.INP","r")
x=int(fi.readline())
fi.close()
fo=open("SQUANUM.OUT","w")
if (sqrt(x)%1==0):
    print("1",file=fo)
else:
    print("0",file=fo)
fo.close()
