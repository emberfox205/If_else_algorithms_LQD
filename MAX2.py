#Tim so lon nhat trong 2 so
fi=open("MAX2.INP","r")
x1=int(fi.readline())
x2=int(fi.readline())
fi.close()
fo=open("MAX2.OUT","w")
if x1>x2:
    print(x1,file=fo)
else:
    print(x2,file=fo)
fo.close()