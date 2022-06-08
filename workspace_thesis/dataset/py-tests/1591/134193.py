n = int(input())
for i in range(1, n+1):
    d = int(input())
    y = 0
    p = 1
    while(d!=0):
        x = d%10
        if(x==2 or x==3 or x==5 or x==7):
            y = x*p+y
            p = p*10
        d = d//10
    if (y!=0):
        print(y)
    else:
        print("-1")