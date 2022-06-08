while 1>0:
    contador=0
    x1,x2=map(int,input().split())
    if x1==x2:
        print('feliz')
    else:
        while x1!=0 and x2!=0:
            digito1=x1%10
            digito2=x2%10
            x1=x1//10
            x2=x2//10
            if digito1!=digito2:
                contador=contador+1
        if contador==1:
            print('feliz')
        else:
            print('lentes')