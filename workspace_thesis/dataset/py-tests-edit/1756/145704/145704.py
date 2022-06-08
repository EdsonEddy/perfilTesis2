def res(n):
    if n>6:
        f = n%6
        return f
    else:
        return n
while True:
    e = int(input())
    for x in range(e):
        n = int(input())
        a = [2,4,8,7,5,1]
        g = int(res(n))
        print(a[g])