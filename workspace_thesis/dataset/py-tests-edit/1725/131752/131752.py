while True:
    n1,n2=map(int,input().split())
    cont=0
    a=0
    while    n1<=n2:
        cont=(cont+1)
        a=cont
        n1=(n1*2)
    print (a)
