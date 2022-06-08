while True:
    est=int(input())
    verb=list(map(int,input().split()))
    num = list(map(int, input().split()))
    notas=[]
    for i in range(est):
        suma=verb[i]+num[i]
        notas.append(suma)
    prom=sum(notas)/est
    reprov=0
    for i in notas:
        if i<prom:
            reprov+=1
    print(reprov)