l,r,k=map(int, input().split(" "))

x=0
s=0
while l<=r:
    x=l%k
    l=l+1
    if x==0:
        s=s+1
print(s)