import math
cn=1
ct=1
a=int(input())
m=0
while a!=0:
    a=float(input())
    if a==0:
        break
    ct=ct+1
    m=max(a,m)
    if a<=0:
        cn=cn+1
p=int((cn/ct)*100)
print(p)
print(int(m))
