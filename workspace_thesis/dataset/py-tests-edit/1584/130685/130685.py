from sys import *
for datos in stdin:
        n=int(datos)
        m=0
        l=0
        if n <= 100 and n >= 0:
            e = list(map(str, input().split()))
            f = len(e)
            f = int(f)
            if n == f:
                mayor = e[0]
                menor = e[0]
                for i in range(0,f):
                    if int(e[i]) > int(mayor):
                         mayor = int(e[i])
                    elif int(e[i]) < int(menor):
                         menor = int(e[i])
                m=int(mayor)
                l=int(menor)
                x=m-l
                print(x)