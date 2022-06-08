from math import log10
def prim(x):
    k=2
    if x==1:
        pri=0
    else:
        while x%k!=0 and k<=(x//2):
            k=k+1
        if k>(x//2):
            pri=x
        else:
            pri=0
    return pri

n=int(input())
for i in range (n):
    x=int(input())
    cd = int(log10(x))
    s=0
    a = x
    s = 0
    while a!=0:
        d=a//(10**cd)
        pri=prim(d)
        a=a%(10**cd)
        cd=cd-1
        if pri!=0:
            s=s*10+pri
    print(s)