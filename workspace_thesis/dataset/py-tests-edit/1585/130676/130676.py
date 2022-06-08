from sys import stdin
for h in stdin:
    n=int(h)
    l=input().split()
    k=input().split()
    s=1
    d=1

    for i in l:

        if int(i)<n and int(i)>0:
            s=s+1
    for j in k:

        if int(j)<n and int(j)>0:
            d=d+1
    q=s*d
    print(q)