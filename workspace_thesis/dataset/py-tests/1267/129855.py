x=1
while x>0:
    n=int(input())
    if n>=0:
        cH=0
        cV=0
        s=0
        for i in range(0,n):
            cH=cH+1
            i+=2
        for j in range(1,n+2):
            j+=2
            cV=cV+1
        s=cV+cH
        print(s)
    if n==-1:
        break