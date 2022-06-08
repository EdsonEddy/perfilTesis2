a,b,c=map(int, input().split(" "))

if a>b:
    aux=a
    a=b
    b=aux
    if a>c:
     aux=a
     a=c
     c=aux
     if b>c:
      aux=b
      b=c
      c=aux
    elif b>c:
      aux=b
      b=c
      c=aux
elif a>c:
    aux=a
    a=c
    c=aux
    if b>c:
     aux=b
     b=c
     c=aux
    elif b>c:
     aux=b
     b=c
     c=aux
elif b>c:
    aux=b
    b=c
    c=aux
print(a,b,c)
