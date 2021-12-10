# so lon nhat trong 3 so
fi=open("MAX3.INP","r")
a=int(fi.readline())
b=int(fi.readline())
c=int(fi.readline())
fi.close()
fo=open("MAX3.OUT","w")
if a>=b and a>=c:
    print(a,file=fo)
elif  b>=a and b>=c:
    print(b,file=fo)
else:
    print(c,file=fo)
fo.close()
