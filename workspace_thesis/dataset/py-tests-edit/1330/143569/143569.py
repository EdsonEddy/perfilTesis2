a,b=map(str,input().split())
b=int(b)
c=b%len(a)
d=len(a)-c
print(a[d:]+a[0:d])