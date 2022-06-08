import sys 
def compara(tam,cad):
    cont=0
    v=s.split(" ")
    for i in range(len(v)):
        if(v[i]==v[tam-1]):
            cont=cont+1
    return(cont)


for n in sys.stdin:
    n=int(n)
    s=input()
    print(compara(n,s))