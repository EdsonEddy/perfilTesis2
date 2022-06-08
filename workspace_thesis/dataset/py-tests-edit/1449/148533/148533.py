while True:
    a,b=map(int,input().split())
    n=int(input())
    v=input().split()
    s=0
    for i in range(n):
        if a<=int(v[i])and int(v[i])<=b:
            s=s+int(v[i])
    print(s)
