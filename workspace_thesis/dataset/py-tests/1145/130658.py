y=int(input())
while y>0:
    x=int(input())
    d,f=0,1
    for i in range(x):
        d,f=f,d+f
    print(d)
    y=y-1
