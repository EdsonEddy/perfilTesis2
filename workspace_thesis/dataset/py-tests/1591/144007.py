z=int(input())
for p in range(z):
    s=0
    h=1
    ss=0
    x = int(input())
    while x>0:
        n=x%10
        x=x//10
        ss=n
        c = 0
        verificar = True
        for i in range(1, n + 1):
            if (n % i) == 0:
                c = c + 1
            if c >= 3:
                verificar = True
                break
        if c == 2 or verificar == False:
            s=s+ss*h
            h=h*10
    if s>1:
        print(s)
    else:
        print("-1")