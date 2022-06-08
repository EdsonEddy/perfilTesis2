n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    mcd = 1
    m = min(a,b)
    while m > 0:
        if a % m == 0 and b % m == 0:
            mcd = m
            break
        m = m - 1
    print(mcd)