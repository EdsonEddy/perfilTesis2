n=int(input())
for i in range(n):
    s=0
    h=1
    m=0
    x = int(input())
    while x>0:
        a=x%10
        x=x//10
        m=a
        c = 0
        verificar = True
        for i in range(1, a + 1):
            if (a % i) == 0:
                c = c + 1
            if c >= 3:
                verificar = True
                break
        if c == 2 or verificar == False:
            s=s+m*h
            h=h*10
    if s>1:
        print(s)
    else:
        print("-1")