a,b=map(str,input().split())
o=int(b)
c1=len(a)-o
c2=a[0:c1]
c3=len(a)
c4=a[c1:c3]
r=c4+c2
print(r)