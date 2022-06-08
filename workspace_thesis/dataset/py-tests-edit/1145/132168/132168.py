n = int(input())
for i in range(n):
    A = int(input())
    m=0
    n=1
    for j in range(A):
        k = n
        n = n+m
        m = k
    print(m)