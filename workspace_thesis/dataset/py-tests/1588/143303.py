casos = int(input())
for i in range(casos):
    elementos=int(input())
    numeros=list(map(int,input().split()))
    others=[]
    for j in numeros:
        if j%3==0:
            producto=j*2
            others.append(producto)
    h=sum(others)
    print("La suma es",h)