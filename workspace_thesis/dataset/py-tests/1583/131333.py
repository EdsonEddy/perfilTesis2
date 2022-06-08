for c in range(int(input())):
    n = int(input())
    if 0 <= n <= 3:
        r2 = r3 = 1
        if n == 3:
            r1, r2, r3 = map(int, input().split())
        elif n == 2:
            r1, r2 = map(int, input().split())
        else:
            r1= int(input())
        ma = r1
        if r2 > ma:
            ma = r2
        if r3 > ma:
            ma = r3
        if ma <= 100:
            for i in range(ma, r1*r2*r3+1, ma):
                if i % r1 == 0 and i % r2 == 0 and i % r3 == 0:
                    break
            print(i)