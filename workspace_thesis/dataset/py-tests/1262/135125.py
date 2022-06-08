n=int(input())
for i in range(n):
    a, b = map(int, input().split())
    while(b!=0):
        a=a%b
        aux=b
        b=a
        a=aux
    print(a)