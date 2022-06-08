a=0
while (a != " "):
    a=int(input())
    b=int(bin(a)[2:])
    b=str(int(b))
    cadi = b[::-1]
    b=int(str(cadi))
    print(int(str(b), 2))