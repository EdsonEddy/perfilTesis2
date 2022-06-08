n=int(input())
while n>0:
    c=0
    u=0
    ss=0
    x=input().split()
    y=input().split()
    for i in range(n):
        s=0
        s = int(x[i]) + int(y[i])
        ss = s + ss
        u = ss / n
    for i in range(n):
        s=0
        s=int(x[i])+int(y[i])

        if s<u:
            c=c+1
    print(c)

    n=int(input())