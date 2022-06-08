from math import *
a,b=map(int,input().split())
tam=cd=int(log10(a))
pos=0
while a>0:
    dig=a//(10**tam)
    pos+=1
    a=a%(10**tam)
    tam-=1
    if pos==b:
        print(cd+1,dig)
        break