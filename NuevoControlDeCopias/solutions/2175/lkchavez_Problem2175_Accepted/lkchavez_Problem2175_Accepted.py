numero_casos=int(input())
for i in range(numero_casos):
    n=int(input())
    a=-1
    b=1
    c=0
    pasos=0
    for i in range(100):
        c=a+b
        if c==n:
            print(pasos)
            break
        a=b
        b=c
        pasos+=1
