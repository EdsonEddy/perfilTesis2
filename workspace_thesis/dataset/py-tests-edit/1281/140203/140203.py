import math
while True:
    n = int(input())
    div = []
    raiz = int(math.sqrt(n))
    if n>10:
        for i in range(1,raiz+1):
            if n%i == 0:
                if n/i==i:
                    div.append(i)
                else:
                    div.append(i)
                    div.append(n//i)
    else:
        for i in range(1,n+1):
            if n%i==0:
                div.append(i)
    div=sorted(div)
    print('Divisores de ',n,': ',sep='',end='');print(*div,sep=' ')