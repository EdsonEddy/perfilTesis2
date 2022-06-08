nc=int(input())
for i in range (nc):
    import sys
    for i in sys.stdin:
        n,m=map(int,i.split())
        if n>=6 and m<=10000:
            n=n//3
            m=m//3
            a=n*m
            print(a)