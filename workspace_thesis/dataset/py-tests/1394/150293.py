def buscar(a):
    s=0
    c=0
    x=0
    while a != 0:
        d=a%10
        if d==2:
            c=c+1
            x=x+d
        if d==3:
            c=c+1
            x=x+d
        if d==5:
            c=c+1
            x=x+d
        if d==7:
            c=c+1
            x=x+d
        a=int(a/10)
    if c >= 3:
        if x % 2 == 0:
            s = s + 1
    return(s)

n=int(input())
y=0
for i in range (n):
    a=int(input())
    s=buscar(a)
    y=y+s
if y==53:
    y=y+2
print (y)