import sys
def contar(tam,cad):
    v=s.split(" ")
    c=0
    for i in range(len(v)):
        if(v[i]==v[tam-1]):
            c=c+1
    return c
           
for n in sys.stdin:
    n=int(n)
    s=input()
    print(contar(n,s))

