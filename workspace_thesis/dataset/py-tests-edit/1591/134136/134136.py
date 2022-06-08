n=int(input())
for i in range(n):
    a=str(input())
    s=len(a)
    x=""
    l="2357"
    for g in range(s):
        if a[g] in l:
            x=x+a[g]
    if x=="":
        print(-1)
    else:
        print(x)