while 1>0:
    n=int(input())
    s=0
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            s=s+1
    if s==0:
        print('ES PRIMO')
    else:
        print('NO ES PRIMO')