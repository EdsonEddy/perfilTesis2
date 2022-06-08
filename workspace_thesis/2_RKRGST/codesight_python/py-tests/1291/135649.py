from sys import stdin
for i in stdin:
    l=list(map(int,i.split()))
    k=sum(l)
    print(k)