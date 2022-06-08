n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    m=0
    if a>b:
        for n in range(1,b,1):
            if b%n==0 and a%n==0:
                m=n
    else:
        for n in range(1,a,1):
            if b%n==0 and a%n==0:
                m=n
    print(m)