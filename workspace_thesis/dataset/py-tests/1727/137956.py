a,b,c=map(int,input().split())
cd=0
for i in range(a,b+1):
    if (i/c==i//c):
        cd=cd+1
print(cd)     