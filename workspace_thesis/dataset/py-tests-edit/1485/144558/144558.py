while 1>0:
    n=int(input())
    c=0
    for i in range(n):
        s=str(input())
        if s==s[::-1]:
            c=c+1
    print(c)