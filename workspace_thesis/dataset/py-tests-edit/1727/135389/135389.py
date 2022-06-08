l,r,k=map(int,input().split(" "))
m=0
while l<=r:
    if l%k==0:
        m=m+1
    l=l+1
print(m)