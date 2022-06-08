l,r,k=map(int,input().split(" "))
z=0
y=0
while l<=r:
    z=l%k
    l=l+1
    if z==0:
        y=y+1
print(y)