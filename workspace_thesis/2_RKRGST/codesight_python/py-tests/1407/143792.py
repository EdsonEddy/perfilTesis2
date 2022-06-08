casos=int(input())
for i in range(casos):
    limite=int(input())
    valores=list(map(int,input().split()))
    c=1
    pico=0
    for j in range(len(valores)-1):
        if j!=0:
            if c<=len(valores):
                if valores[j]>valores[c] and valores[j-1]<valores[j]:
                    pico+=1
        c=c+1
    print(pico)