while True:
    a=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(a):
        s+=l[i]
    print(s)
