continuar=True
while continuar:
    c=0
    n=int(input())
    for i in range(n):
        d=int(input())
        c=d+c
    print(c)
    c=0
continuar=(input().lower())