def fibonasi(h):
    a = 0
    b = 1
    listaF = []
    for i in range(h):
        listaF.append(b)
        a, b = b, a + b
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
def Tribonaci(n):
    ListaTrib=[]
    a,b,c=1,3,6
    for i in range(n):
        ListaTrib.append(a)
        numsig=a+b+c
        a=b
        b=c
        c=numsig
    return ListaTrib
def positivos(n,x):
    positivos = 0
    a = (fibonasi(n))
    b = (NumPrimos(n))
    tri = (Tribonaci(n))
    for i in range(0, n, 2):
        positivos = positivos + (tri[i] *( x ** b[i])) / a[i]
    return positivos
def negativos(n,x):
    negativos = 0
    a = (fibonasi(n))
    b = (NumPrimos(n))
    tri = (Tribonaci(n))
    for u in range(1, n, 2):
        negativos = negativos + (tri[u] *(x ** b[u])) / a[u]
    return negativos
while True:
    try:
            n,x=map(int,input().split())
            if 1 <= n <= 5:
               if 1 <= x <= 20:
                   numero='{0:.2f}'.format((positivos(n,x))-(negativos(n,x)))
                   print(numero)
               else:
                  break
            else:
                break
    except ValueError:
        break
