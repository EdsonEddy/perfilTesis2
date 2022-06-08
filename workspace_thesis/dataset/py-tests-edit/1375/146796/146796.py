n=str(input())
nn=n.upper()
va="ORO"
a=[]
for i in range(0,len(n)):
    if nn[i]in va:
        a.extend([i])
v = sorted(a)
m = max(v)
mn = min(v)
if m-mn==1 or m-mn==2:
    print(mn, m)
else:
    print("-1")