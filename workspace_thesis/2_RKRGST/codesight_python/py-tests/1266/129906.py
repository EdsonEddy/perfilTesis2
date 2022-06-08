from sys import*
while 2>0:
    e1, v=map(int,input().split())
    x=input().split()
    s=0
    for o in range(e1):
        for i in x:
            e1=e1-1
            e = e1
            y=(int(i))
            p=v**e
            r = y*p
            s=s+r
        print(float(s))
        break