from math import *
n=int(input())
tam=int(log10(n))+1
if  tam%2==0:
    print("*")
else:
    tam = tam//2
    while tam>0:
        n=n//10
        tam=tam-1
    print(n%10)
