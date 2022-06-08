n=str(input())
g=len(n)
c=0
b=8
r=""
while b<g+8:
    d=n[c:b]
    x=int(d,2)
    a=chr(x)
    r+=str(a)
    c+=8
    b+=8
print(r)