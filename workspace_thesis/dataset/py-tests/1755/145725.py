a=int(input())
for i in range(a):
    k, n = map(int, input().split())
    if k < n:
        print(1)
    else:
        v = [1] * n
        for i in range(0, k + 1 - n):
            p = sum(v)
            v = v[1:]
            v.append(p)
        print(v[n - 1])
