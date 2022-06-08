n = int(input())

while n>0:
    b = ''
    x = 0
    c = 1
    y = 0
    bin = ''
    while n // 2 != 0:
        bin = str(n % 2) + bin
        n = n // 2
    b=str(n) + bin
    b=b[::-1]
    b=int(b)
    ex=-1
    while b > 0:
        y=b%10

        b=b//10
        ex=ex+1

        x=(y*2**ex)+x
    print(x)
    n=int(input())
