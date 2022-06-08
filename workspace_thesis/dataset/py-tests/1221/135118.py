a,b,c =map(int,input().split())
import math

if a<b and a<c:
    if b<c:
        print(a,b,c)
    else:
        print(a,c,b)
else:
    if b<c and b<a:
        if a<c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        if a<b:
            print(c,a,b)
        else:
            print(c,b,a)