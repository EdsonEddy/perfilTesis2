import math
n=int(input())
for i in range (n):
    a,b,c=map(int,input().split())
    may=0
    men=100000000000
    med=0
    if a>may:
        may=a
    if b>may :
        may=b
    if c>may :
        may=c
    if a<men :
        men=a
    if b<men :
        men=b
    if c<men :
        men=c
    if a!=may and a!=men:
        med=a
    if(b!=may and b!=men):
        med=b
    if(c!=may and c!=men):
        med=c
    print("Case " + str(i + 1) + ": " + str(med))