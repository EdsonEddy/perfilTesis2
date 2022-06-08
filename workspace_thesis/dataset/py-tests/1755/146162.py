def fibo(numero, tipo):
    ls = [1]*tipo
    ls[-1] = (-1)*(tipo-2)
    for i in range(numero+1):
        # print(ls)
        ls.append(sum(ls))
        ls.remove(ls[0])
    print(ls[-1])


nveces = int(input())
for i in range(1,nveces+1):
    elemento, tipo = map(int,input().split())
    fibo(elemento, tipo)