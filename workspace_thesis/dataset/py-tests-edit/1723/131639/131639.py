while 1>0:
    cont=0
    a1,a2=map(int,input().split())
    if a1==a2:
        print('feliz')
    else:
        while a1!=0 and a2!=0:
            dig1=a1%10
            dig2=a2%10
            a1=a1//10
            a2=a2//10
            if dig1!=dig2:
                cont=cont+1
        if cont==1:
            print('feliz')
        else:
            print('lentes')