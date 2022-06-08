import collections
x=int(input())
l=[int(e) for e in input().split()]
h=collections.Counter(l)
j=list(h)
t=max(h,key=h.get)
dij=t
c=0
for d in range(0,len(l)):
    if l[d]!= dij:
          c+=1
print(c)