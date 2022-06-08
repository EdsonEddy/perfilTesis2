y=1
while y>0:
    x=int(input())
    if x>=0:
        n=0
        m=0
        s = 0
        for i in range(0,x):
            n=n+1

        for j in range(1,x+2):
            m=m+1

        s=m+n
        print(s)
    if x==-1:
        break