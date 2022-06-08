from sys import stdin
for i in stdin:
    n=int(i)
    c=bin(n)
    d=c[2:]
    print(len(d))