while True:
    a=1
    b,c=map(int,input().split())
    d=1
    e=0
    while (d==1):
        x=(a+b)//2
        e =e+1
        if(x<c):
            a=x+1
        elif(x>c):
            b=x-1
        elif(x==c):
            print(e)
            break