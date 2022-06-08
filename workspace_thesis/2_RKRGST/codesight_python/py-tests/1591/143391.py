k=int(input())
for j in range(1,k+1,1):
    h=0
    c=1
    g=int(input())
    while g!=0:
        d=g%10
        g=g//10
        if d==2 or d==3 or d==5 or d==7 :
            h=h+d*c
            c=c*10
    if h!=0:
        print(h)
    else:
        print("-1")
