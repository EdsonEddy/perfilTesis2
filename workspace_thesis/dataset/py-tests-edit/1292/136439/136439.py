while True:
    m=int(input())
    if m==0:
        break
    l=list(map(int,input().split()))
    s=0
    b=len(l)
    if b==m:
        for i in l:
            s=s+i
        print(s)