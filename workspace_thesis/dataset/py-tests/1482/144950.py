def serie(n):
    s=-1
    for k in range (1,n+1):
        s=s*k
        print(s)
        s=s*-1


n=int(input())
serie(n)