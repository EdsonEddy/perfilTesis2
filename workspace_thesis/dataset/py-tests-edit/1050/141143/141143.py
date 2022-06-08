num = int(input())

while num>0:
    b = ''
    x = 0
    c = 1
    y = 0
    bin = ''
    while num // 2 != 0:
        bin = str(num % 2) + bin
        num = num // 2
    b=str(num) + bin
    b=b[::-1]
    b=int(b)
    ex=-1
    while b > 0:
        y=b%10

        b=b//10
        ex=ex+1

        x=(y*2**ex)+x
    print(x)
    num=int(input())
