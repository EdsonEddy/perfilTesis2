n=int(input())
s=input().split()
s=[i for i in s]
l=[]
r=[]
for u in s:
    if u not in l:
        l.append(u)
for k in range(len(l)):
    x=s.count(l[k])
    r.append(x)
o=max(r)
p=0
for g in range(len(l)):
    if o==r[g]:
        p=p+s.count(l[g])
print(len(s)-p)