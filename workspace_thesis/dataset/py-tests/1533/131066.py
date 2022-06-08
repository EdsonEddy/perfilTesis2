from sys import stdin
for i in stdin:
    a,b=map(int,i.split())
    if b<=a//2:
        c=b*2-1
    if b>a//2:
        if a%2==0:
            k=a//2
        else:
            k=a//2+1
        b=b-k
        c=b*2
    print(c)