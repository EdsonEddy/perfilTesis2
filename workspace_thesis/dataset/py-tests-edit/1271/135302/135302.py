n = int(input())
for i in range(1, n+1):
    x = int(input())
    z = x
    y = 0
    while x!=0:
        a = x%10
        s = 1
        f = 1
        while(s<=a):
            f = f*s
            s = s+1
        y = y + f
        x = int(x/10)
    if y == z:
        print("Y")
    else:
        print("N")