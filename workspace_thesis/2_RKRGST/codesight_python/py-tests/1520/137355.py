n=int(input())
numerador=1
denominador=1
k='/'
q=n
p=n
while (n!=0):
    while(p!=0):
        z=str(numerador)+str(k)+str(denominador)
        print(z)
        denominador=denominador+1
        p=p-1
    n=n-1
    denominador=1
    numerador=numerador+1
    p=q