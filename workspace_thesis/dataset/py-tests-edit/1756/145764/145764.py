e=int(input())
for f in range(e):
    a=int(input())
    a=a%6
    b=(2**a)*2
    while b>=10:
        b=str(b)
        d=0
        for c in b:
            d=d+int(c)
        b=d
    print(b)