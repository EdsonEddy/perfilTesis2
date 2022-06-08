from math import log10
def prim(h):
    y=2
    if h==1:
        pri=0
    else:
        while h%y!=0 and y<=(h//2):
            y=y+1
        if y>(h//2):
            pri=h
        else:
            pri=0
    return pri

n=int(input())
for i in range (n):
    h=int(input())
    cd = int(log10(h))
    s=0
    a = h
    s = 0
    while a!=0:
        d=a//(10**cd)
        pri=prim(d)
        a=a%(10**cd)
        cd=cd-1
        if pri!=0:
            s=s*10+pri
    print(s)
