from sys import *
for line in stdin:
    c1=input()
    c2=input()
    v=list(map(int,c1.split(" ")))
    v1=list(map(int,c2.split(" ")))
    v.sort()
    v1.sort(reverse=True)
    g=0
    for i in range(len(v1)):
        g+=v[i]*v1[i]
    print(g)
    