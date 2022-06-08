l,r,k=map(int,input().split( ))
x=0
while (l<=r):
    if l%k==0:
        x=x+1
    l=l+1
print(x)
