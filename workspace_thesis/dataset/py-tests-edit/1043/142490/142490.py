h=int(input())
for i in range(1,h+1):
    a,b=map(int,input().split())
    c=a//3
    d=b//2
    e=a%3
    f=b%2
    if d>c:
        g=d-c
        g=g*2
        print(c,e+g+f)
    elif c>d:
        g=c-d
        g=g*3
        print(d,g+f+e)
    else:
        print(d,e+f)