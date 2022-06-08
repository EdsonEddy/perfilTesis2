n=int(input())
for n in range(n):
    r,p=map(int,input().split())
    if p==0:
        print(0,r)
    elif r==0:
        print(0,p)
    else:
        m=r//3
        m1=p//2
        s=r%3
        s1=p%2
        if m<m1:
            for i in range(m):
                p=p-2
            print(m,p+s)
        else:
            for i in range(m1):
                r=r-3
            print(m1,s1+r)