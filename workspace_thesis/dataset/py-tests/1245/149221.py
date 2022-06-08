n,m=map(int,input().split())
if n<m:
    print(m)
    while m>n:
        m=m-1
        print(m)
else:
    print(n)
    while n>m:
        n=n-1
        print(n)