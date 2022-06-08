n=int(input())
if 1<=n<=100:
    l=[str(e)for e in input().split()]
    if len(l)==n:
        if (l[::-1])==l:
            print("SI")
        else:
            print("NO")
