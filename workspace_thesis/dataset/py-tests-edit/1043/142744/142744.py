c=int(input())
for i in range(c):
    a,b=map(int,input().split())
    e=a//3
    f=b//2
    if f<e:
        p=f*(3+2)
        s=a+b
        t=s-p
        print(f,t)
    else:
        p=e*(3+2)
        s=a+b
        t=s-p
        print(e,t)
