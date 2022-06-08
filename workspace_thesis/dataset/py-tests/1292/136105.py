while 2>0:
    num=int(input())
    n=list(map(int,input().split()))
    if num==len(n):
        s=sum(n)
        print(s)
    else:
        exit()