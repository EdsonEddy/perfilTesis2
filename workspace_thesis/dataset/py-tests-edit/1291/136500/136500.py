while True:
    n=list(map(int,input().split()))
    t=len(n)
    j=t-1
    s=0
    for i in range (j):
        s=n[i]+s
    print(s)