a,b = map(int, input().split())
if b>a:
    aux=a
    a=b
    b=aux
for i in range(a,b-1,-1):
    print(i)