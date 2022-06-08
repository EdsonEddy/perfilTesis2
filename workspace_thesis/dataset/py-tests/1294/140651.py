def sum(v,a,b):
    res = 0
    for i in range(a,b +1):
        res += int(v[i])
    return res


a = int(input())
for i in range (a):
    n,a,b = map(int, input(). split())
    v = input().split()
    print(sum(v,a,b))
