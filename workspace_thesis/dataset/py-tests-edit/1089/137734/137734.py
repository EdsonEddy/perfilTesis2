numero=str(input())
a=len(numero)
if a%2==0:
    print("*")
else:
    d=int(a/2)
    r=numero[d]
    print(r)