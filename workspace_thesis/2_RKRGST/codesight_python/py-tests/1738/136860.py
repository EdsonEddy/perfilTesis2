while True:
    n = int(input())
    k1 = 10
    k2 = 1
    a = 11
    b = 5
    for i in range(1,n+1):
        if i == n:
            if i % 2 == 0:
                bd1 = 18 - k1
                if bd1 == 10:
                    b = b - bd1
                    print(b,end="")
                elif bd1 == 8:
                    b = b + bd1
                    print(b,end="")
                k1 = bd1
            else:
                bd2 = 4 - k2
                if bd2 == 1:
                    a = a + bd2
                    print(a,end="")
                elif bd2 == 3:
                    a = a - bd2
                    print(a,end="")
                k2 = bd2
        else:
            if i % 2 == 0:
                bd1 = 18 - k1
                if bd1 == 10:
                    b = b - bd1
                    print(b,end=" ")
                elif bd1 == 8:
                    b = b + bd1
                    print(b,end=" ")
                k1 = bd1
            else:
                bd2 = 4 - k2
                if bd2 == 1:
                    a = a + bd2
                    print(a,end=" ")
                elif bd2 == 3:
                    a = a - bd2
                    print(a,end=" ")
                k2 = bd2
    print()