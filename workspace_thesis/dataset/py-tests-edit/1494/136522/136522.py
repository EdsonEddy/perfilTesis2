def fibonasi (h):
    a=0
    b=1
    listaF=[]
    for i in range(h):
        listaF.append(b)
        a,b=b,a+b
    return listaF

def factorial(g):
    f = 1
    for c in range(1, g + 1):
        f = f * c
    return f

def NumPrimos(n):
    ListaP=[]
    for i in range (2,500):
        if int(len(ListaP))==n:
            break
        elif int(factorial(i-1)+1)%int(i)==0:
            ListaP.append(i)
    return ListaP
def Sumar(a,b):
    sum=0
    for u in range(0, n):
        sum = sum + (a[u] / (b[u] * x))
    return sum

while True:
    try:
            n,x=map(int,input().split())
            if 1 <= n <= 40:
               if 1 <= x <= 40:
                   a = (fibonasi(n))
                   b = (NumPrimos(n))
                   numero='{0:.2f}'.format(Sumar(a,b))
                   print(numero)
    except ValueError:
        break