sec=int(input())
while sec>0:
    a=int(input())
    b=1
    a=a%6
    for i in range(a+1):
        b=b*2
        if b>=10:
            b=b%10+b//10
    print(b)
    sec-=1