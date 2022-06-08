sp=0
si=0
while 1>0:
    n=int(input())
    c=1
    sp = 0
    si = 0
    while n!=0:
        if c%2==0:
            d = n % 10
            sp=sp+d
        else:
            d = n % 10
            si = si + d
        n=n//10
        c=c+1
    if si==sp:
        print('SI')
    else:
        print('NO')