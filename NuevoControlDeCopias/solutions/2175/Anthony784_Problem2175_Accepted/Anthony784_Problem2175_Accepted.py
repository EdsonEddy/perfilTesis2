k = int(input())
for i in range(k):
    n = int(input())
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        c = 2
        a=1
        b=1
        while True:
            s = a+b
            if s==n:
                c = c+1
                print(c)
                break
            else:
                a=b
                b=s
                c = c+1
