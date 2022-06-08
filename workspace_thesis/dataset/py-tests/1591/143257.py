n = int(input())
i = 1
while(i <= n):
    x = 0
    e = 0
    a = int(input())
    while(a > 0):
        dig = a % 10
        a = a // 10
        if(dig==2 or dig==3 or dig==5 or dig==7):
            x = x + dig*(10**e)
            e = e + 1
    if (x > 0):
        print(x)
        i = i + 1
    else:
        print("-1")
        i = i + 1