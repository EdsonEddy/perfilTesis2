n = int(input())
i = 1
c = 0
while(i <= n):
    a = int(input())
    for y in range(a):
        b = input().split()
        for x in range(len(b)):
            if (int(b[x])%3==0):
                b[x] = int(b[x]) * 2
                c = c + b[x]
        print ("La suma es",c)
        c = 0
        break
    i = i + 1