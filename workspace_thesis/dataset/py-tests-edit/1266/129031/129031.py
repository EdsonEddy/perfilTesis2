from sys import stdin
for k in stdin:
    a,b=map(int,k.split())
    l=input().split()
    l = l[::-1]
    h=0
    s=0
    for i in l:
        f=int(i)
        s=s+f*(b**h)
        h=h+1
    print(float(s))
