while True:
    c=0
    m=0
    d=0
    a,b  = map(int,input().split())
    while a!=0:
        d1=a%10
        if d1!=b%10:
            c=c+1
        a=a//10
        b=b//10
    if c>1:
        print('lentes')
    else:
        print('feliz')