def solucion():
    l, r, k = map(int, input().split(" "))
    cont = 0
    for i in range(l, r+1):
        if(i % k == 0):
            cont+=1
    print(cont)

solucion()