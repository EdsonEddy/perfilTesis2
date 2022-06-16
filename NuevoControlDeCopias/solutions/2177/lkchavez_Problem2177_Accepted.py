
import math
numero_casos=int(input())
for i in range(numero_casos):
    num, digi=map( int, input(). split())
    n=num
    contador = len(str(num))
    pasos=0
    nuevo=0
    p=0
    total=0
    if contador<digi:
        print("")
    elif n%10000==0:
        print(n//10**(digi-1))
    elif digi==2:
        while n>0:
            x=n%10
            nuevo+=x*10**pasos
            contador = len(str(nuevo))
            if contador==digi:
                num=nuevo
                final=num
                ng=num
                t=int(math.log10(ng))+1
                k=0
                while t>0:
                    dig=ng//(10**(t-1))
                    ng=ng%(10**(t-1))
                    t=t-1
                    k=k+dig
                    while k>9:
                        ng=k
                        t=int(math.log10(ng))+1
                        k=0
                        while t>0:
                            dig=ng//(10**(t-1))
                            ng=ng%(10**(t-1))
                            t=t-1
                            k=k+dig
                suma=k
                total+=k*10**p
                p+=1
                pasos=0
                nuevo=x
            n=n//10
            pasos+=1
        print(total)
    else:
        n=num
        nuevo=0
        nuev=0
        pasos=0
        compu=0
        total=0
        p=0
        k=digi
        while n>0:
            x=n%10
            nuevo+=x*10**pasos
            contador = len(str(nuevo))
            if contador==k:
                compu=math.floor(nuevo/10)
                num=nuevo
                final=num
                ng=num
                t=int(math.log10(ng))+1
                g=0
                while t>0:
                    dig=ng//(10**(t-1))
                    g+=dig
                    ng=ng%(10**(t-1))
                    t=t-1
                while g>9:
                    ng=g
                    t=int(math.log10(ng))+1
                    g=0
                    while t>0:
                        dig=ng//(10**(t-1))
                        ng=ng%(10**(t-1))
                        t=t-1
                        g=g+dig
                suma=g
                total=total+g*10**p
                p+=1
                nuevo=compu
                pasos=k-2
            n=n//10
            pasos+=1
        print(total)
