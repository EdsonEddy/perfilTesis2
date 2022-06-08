def secuencia(z):
    a=z%6
    m=pow(2,a)
    j=2*m
    s=0
    while j>=10:
            d=j%10
            j=j//10
            s=d+j
            j=s
    return j
numero=int(input())
for j in range(1,numero+1,1):
    lista=int(input())
    d=secuencia(lista)
    print(d)