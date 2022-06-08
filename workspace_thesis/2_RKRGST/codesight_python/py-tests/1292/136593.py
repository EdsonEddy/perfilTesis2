while True:
    l=int(input())
    if l==0:
        break
    j=list(map(int,input().split()))
    s=0
    b=len(j)
    if b==l:
        for g in j:
            s=s+g
        print(s)