from math import pi
n=int(input())
for i in range (n):
    x=input().split()
    sw=0
    area=1
    for j in (x):
        if sw==0:
            if j=='rectangle':
                sw=1
            else:
                sw=2
        else:
            if sw==1:
                area=area*float(j)
            else:
                area=pi*(float(j)**2)
    print("{0:.2f}".format(area))
