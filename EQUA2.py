# Phuong trinh pac bo
from math import sqrt
fi=open("EQUA2.INP","r")
a=int(fi.readline())
b=int(fi.readline())
c=int(fi.readline())
fi.close()
D= (b**2)-(4*a*c)
fo=open("EQUA2.OUT","w")
if a==0:
    if b==0:
        if c==0:
            print("VSN",file=fo)
        else:
            print("VN",file=fo)
    else:
        if c==0:
            print(0,file=fo)
        else:
            print(((-c)/b),file=fo)
else:
    if D<0:
        print("VN",file=fo)
    else:
        print(float((-b-sqrt(D))/(2*a)),file=fo)
        print(float((-b+sqrt(D))/(2*a)),file=fo)
fo.close()

