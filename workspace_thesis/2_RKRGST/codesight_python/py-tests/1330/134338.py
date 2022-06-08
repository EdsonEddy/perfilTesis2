n,m=input().split()
k=int(m)
if(k==0):
    c=n
else:
    for i in range(1,k+1,1):
        x=len(n)
        c=n[x-1]+n[:x-1]
        n=c
print(c)
