while True:
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for j in range(n):
        if a[j]==a[n-1]:
            c += 1
    print(c)