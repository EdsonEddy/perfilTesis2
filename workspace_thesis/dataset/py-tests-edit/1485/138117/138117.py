def invierte(n):
    m=0
    while n > 0:
        d = n%10
        m = m * 10 + d
        n = int(n/10)
    return m
n=int(input())
c=0
for i in range(n):
    x=int(input())
    y=invierte(x)
    if x == y:
        c=c+1
print(c)
k=int(input())
cont=0
for i in range(k):
    p=int(input())
    o=invierte(p)
    if p == o:
        cont=cont+1
print(cont)
