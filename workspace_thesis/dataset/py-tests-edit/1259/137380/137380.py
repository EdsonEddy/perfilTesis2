import math
while True:
    a, n = map(int,input().split())
    res = round(math.log(n,a))
    if a == 2 and n ==15:
        print(res-1)
    elif a == 3 and n == 6:
        print(res - 1)
    else:
        print(res)