def antiacumulada(n):
    t=0
    cad=input()
    v=cad.split(" ")
    aux=[]
    for i in range(n):
        aux.append(v[i])
        sum=int(aux[i])-t
        t=int(v[i])
        if(i!=n-1):
            print(sum,end=" ")
        else:
            print(sum)
n=int(input())
antiacumulada(n)