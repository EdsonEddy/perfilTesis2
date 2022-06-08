n=int(input())
for i in range(n):
    c=0
    a=input().split()
    le=len(a)
    for y in range(1,le):
        m = int(a[y - 1])
        A = int(a[y])
        if y+1==le:
            print(c)
            break
        elif m<A:
            c=c+1
        else:
            continue