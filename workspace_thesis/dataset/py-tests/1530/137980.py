def casa(n):
    import math
    num,i = 0,0
    while n>0:
        d = n%10
        if d==2 or d==3 or d==5 or d==7:
            num = int(num+ d*math.pow(10,i))
            i=i+1
        n = int(n/10)
    print(num)


T = int(input())
for i in range(T):
    x = int(input())
    casa(x)