# tim so chan le
fi=open("EVENODD.INP","r")
x=int(fi.readline())
fi.close()
fo=open("EVENODD.OUT","w")
if (x%2==0):
    print("0",file=fo)
else:
    print("1",file=fo)
fo.close()

