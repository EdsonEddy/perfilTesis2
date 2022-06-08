x=int(input())
for f in range (x):
    y=input()
    a=input().split()
    c=int(a[0])
    d=0
    e=0
    for b in a:
        b=int(b)
        if b<c and c>e:
            d=d+1
        e=c
        c=b
    print(d)