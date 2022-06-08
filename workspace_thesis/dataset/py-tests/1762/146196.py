while True:
    a=int(input())
    num=list(tuple(map(int,input().split())))
    contador=list(set(num))
    r=[]
    suma=0
    for i in range(len(contador)):
        cont=num.count(contador[i])
        r.append(cont)
    
    for j in range(len(r)):
        suma=suma+r[j]//2
    print(suma)  
