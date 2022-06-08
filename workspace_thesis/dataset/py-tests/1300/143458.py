f = ''
while True:
    t = 0
    n = input()
    if (str(n) == str(f)):
        break
    else:
        n = int(n)
        for x in range(n):
            c = input().split()
            break
        l = int(c[n - 1])
        n = n - 1
        while(n >= 0):
            s = int(c[n-1])
            n = n - 1
            if(s == l):
                t = t + 1       
        print(t)