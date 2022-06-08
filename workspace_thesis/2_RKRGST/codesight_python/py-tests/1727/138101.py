l,r,k=map(int,input().split(" "))
p=0
for i in range (l,r+1):
    if l%k==0:
        p=p+1
    l=l+1
print(p)
