while 1>0:
    b=0
    X1,X2=map(int,input().split())
    if X1==X2:
        print('feliz')
    else:
        while X1!=0 and X2!=0:
            C1=X1%10
            C2=X2%10
            X1=X1//10
            X2=X2//10
            if C1!=C2:
                b=b+1
        if b==1:
            print('feliz')
        else:
            print('lentes')