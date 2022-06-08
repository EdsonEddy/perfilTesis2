n = int(input())
for i in range(1, n+1):
    x = int(input())
    y = 0
    p = 1
    while x!=0:
        a = int(x%10)
        if a==2 or a==3 or a==5 or a==7:
            y = a*p+y
            p = p*10
        x = x/10
    if y!=0:
        print(y)
    else:
        print("0")