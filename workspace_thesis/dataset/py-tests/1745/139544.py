c=-1
b=0
s=[0]
a=123
while a!=0:
    a=str(input())
    if a==0:
        break
    if a!=0:
        c=c+1
    a=float(a)
    if a<0:
        b=b+1
    s.append(a)
d=max(s)
p=(b/c)*100
print(int(p))
print(int(d))
