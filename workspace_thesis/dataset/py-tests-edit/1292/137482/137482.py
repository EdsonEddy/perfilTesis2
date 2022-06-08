while True:
    m=int(input())
    if m==0:
        break
    else:
        n=list(map(int,input().split()))
        s=0
        for i in range (m):
            s=n[i]+s
        print(s)