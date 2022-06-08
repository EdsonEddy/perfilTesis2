from math import*
def epicentro(n,tam):
    while tam>0:
        n=n//10
        tam=tam-1
    return n%10

n=int(input())
tam=int(log10(n))+1
if tam%2==0:
    print("*")
else:
    tam=tam//2
    print(epicentro(n,tam))