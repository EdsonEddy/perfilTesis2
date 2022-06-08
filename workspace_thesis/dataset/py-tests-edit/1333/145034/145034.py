a=input()
a=a[::-1]
b=len(a)
c=[]
for d in range(b):
    e=(a[0:d+1])
    c.append(e[::-1])
c.sort()
for f in c:
    print(f)
