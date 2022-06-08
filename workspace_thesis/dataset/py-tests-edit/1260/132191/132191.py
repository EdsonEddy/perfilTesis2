n=int(input())
r=0
for f in range(n):
    c,d=map(int,input().split())
    if(2<=c,d and c,d<=10**5):
        a=max(c,d)
        b=min(c,d)
        while b!=0:
            r=b
            b=a%b
            a=r
        print(r)
        r=0