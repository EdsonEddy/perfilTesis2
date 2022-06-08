while True:
    a,b=map(int,input().split())
    e=0
    f=0

    while a>0 and b>0:
        c=a%10
        d=b%10
        a=a//10
        b=b//10
        if c != d:
            f=f+1


    if f>1:
            print("lentes")
    else:
            print("feliz")
