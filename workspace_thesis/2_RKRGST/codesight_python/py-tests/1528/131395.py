n = int(input())
i = 1
while (i <= n):
    m = -1
    x = 0
    e = 0
    a = int(input())
    while (a > 0):
        x = x + 1
        dig = a % 10
        a = a // 10
        if (dig > m):
            e = e + 1
            m = dig
        else:
            e = e + 0
    if (x == e):
        print ("SI!")
    else:
        print ("NO!")
    i = i + 1