n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    while(b!=0):
        a=a%b
        aux=b
        b = a
        a = aux
    print(a)