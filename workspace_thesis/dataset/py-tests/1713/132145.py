from sys import stdin
for n in stdin:
    n=int(n)
    s=0
    for j in range(n):
        x=int(input())
        s+=x
    print(s)
