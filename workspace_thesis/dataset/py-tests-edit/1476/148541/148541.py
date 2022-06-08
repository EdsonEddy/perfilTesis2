def ordenAsen(v,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(int(v[i])>int(v[j])):
                aux=v[i]
                v[i]=v[j]
                v[j]=aux
    return
from sys import *
n,m=map(int,input().split())
v1=stdin.readline().split()
v2=stdin.readline().split()
v1.extend(v2)
ordenAsen(v1,len(v1))
for i in range(len(v1)):
    stdout.write(v1[i])
    print()