#phuong trinh bac nhat
from math import sqrt
fi=open("EQUA1.INP","r")
a=int(fi.readline())
b=int(fi.readline())
fi.close()
fo=open("EQUA1.OUT","w")
if a==0:
    if b==0:
        print("VSN",file=fo)
    else:
        print("VN",file=fo)
else:
    x=((-b)/a)
    print(x,file=fo)
fo.close()
