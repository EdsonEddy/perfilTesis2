while 1>0:
    n=str(input())
    s=0
    n1=str(input())
    f=n+n1
    abc='abcdefghijklmnopqrstuvwxyz'
    for i in abc :
        if i not in f:

            s=1
    if s==0:
        print('Correcto')
    else:
        print('Incorrecto')
