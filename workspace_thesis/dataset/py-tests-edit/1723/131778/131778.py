while 1>0:
    s=0
    x1,x2=map(int,input().split())
    if x1==x2:
        print('feliz')
    else:
        while x1!=0 and x2!=0:
            c1=x1%10
            c2=x2%10
            x1=x1//10
            x2=x2//10
            if c1!=c2:
                s=s+1
        if s==1:
            print('feliz')
        else:
            print('lentes')