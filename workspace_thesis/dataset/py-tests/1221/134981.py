import math
a,b,c=map(int,input().split())
if (a<b and a<c):
    if(b<c):
        print(a,b,c)
    else:
        print(a,c,b)
if (b<c and b<a):
    if(a<c):
        print(b,a,c)
    else:
        print(b,c,a)
else:
    if(c<b and c<a):
        if(b<a):
            print(c,b,a)
        else:
            print(c,a,b)