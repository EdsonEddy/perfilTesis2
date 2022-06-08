s1=0
s2=0
while 1>0:
    n=int(input())
    c=1
    s1 = 0
    s2 = 0
    while n!=0:
        if c%2==0:
            d = n % 10
            s1=s1+d
        else:
            d = n % 10
            s2 = s2 + d
        n=n//10
        c=c+1
    if s1==s2:
        print('SI')
    else:
        print('NO')