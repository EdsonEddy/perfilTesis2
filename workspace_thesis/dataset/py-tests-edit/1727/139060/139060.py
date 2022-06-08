l,r,k=map(int,input().split(" "))
p=0
while l<=r:
    if l%k==0:
        p=p+1
    l=l+1
print(p)