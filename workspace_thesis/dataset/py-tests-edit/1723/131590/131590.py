while 1>0:
    a,b=map(int,input().split())
    c=0
    if a==b:
        print('feliz')
    else:
        while a!=0 and b!=0:
            d1=a%10
            d2=b%10
            a=a//10
            b=b//10
            if d1!=d2:
                c=c+1
        if c==1:
            print('feliz')
        else:
            print('lentes')