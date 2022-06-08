n,a=map(str,input().split())
r=len(n)
x=r-int(a)
l=n[x:r+1]
m=n[0:x]
print(l+m)