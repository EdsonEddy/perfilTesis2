a,b,c=input().split()

if int(a)>int(b):
    aux=a
    a=b
    b=aux
if int(a)>int(c):
    aux=a
    a=c
    c=aux
if int(b)>int(c):
    aux=b
    b=c
    c=aux
print(a,b,c)