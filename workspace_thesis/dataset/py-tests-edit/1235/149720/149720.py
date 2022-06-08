def leeVector(v,n):
    cad=input()
    v=cad.split(" ")
    for i in range(n):
        v[i]=int(v[i])
    return v
n=int(input())
v=[]
v=leeVector(v,n)
if (n%2==0):
    a=n/2
    b=n/2
else:
    a=int(n/2)+1
    b=n//2
x=0
y=0
c=0
for i in range(a):
    x=x+v[i]
    c=c+1

for j in range(c,n):
    y=y+v[j]
if (y>x):
    p=y-x
else:
    p=x-y
print(p)