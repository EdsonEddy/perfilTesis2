from math import log10
while 1>0:
    n=int(input())
    cp=0
    for i in range (n):
        x=int(input())
        cd=int(log10(x))+1
        nn=0
        c=1
        while c<=(cd//2):
            nn=(nn*10)+(x%10)
            x=x//10
            c=c+1
        if cd%2==0:
            if nn==x:
                cp=cp+1
        else:
            x=x//10
            if nn==x:
                cp=cp+1
    print(cp)
