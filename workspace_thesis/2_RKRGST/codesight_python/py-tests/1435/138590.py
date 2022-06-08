from math import*
n,k=map(int,input().split())
tam=int(log10(n))+1
c=tam-k
print(tam,end=" ")
while c>0:
        n//=10
        c-=1
print(n%10)