n,m=map(str,input().split())
p=int(m)
n1=len(n)-p
n2=n[0:n1]
n12=len(n)
n3=n[n1:n12]
o=n3+n2
print(o)