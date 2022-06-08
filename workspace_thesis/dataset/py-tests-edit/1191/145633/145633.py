from sys import stdin
for line in stdin:
    lista = list(map(int, input().split()))
    m = int(input())
    lista.sort()
    for i in lista:
        if (m - i) in lista:
            print(i, (m-i))
            break
    else:
        print(-1)