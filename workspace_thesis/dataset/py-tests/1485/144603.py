def palindrono(x):
    inv=0
    y=x
    while y>0:
        d=y%10
        y=y//10
        inv=inv*10+d
    if inv==x:
        return True
while True:
    c=0
    for i in range(int(input())):
        x=int(input())
        if palindrono(x):
            c=c+1
    print(c)