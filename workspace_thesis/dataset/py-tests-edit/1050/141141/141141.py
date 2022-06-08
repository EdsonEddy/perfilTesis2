a=int(input())
while a>0:
    b = ''
    x = 0
    c = 1
    y = 0
    bin = ''
    while a // 2 != 0:
        bin = str(a % 2) + bin
        a = a // 2
    b=str(a) + bin
    b=b[::-1]
    b=int(b)
    xe=-1
    while b > 0:
        y=b%10
        b=b//10
        xe=xe+1
        x=(y*2**xe)+x
    print(x)
    a=int(input())