l,r,k=map(int,input().split(" "))
f=0
while l<=r:
    if l%k==0:
        f=f+1
    l=l+1
print(f)