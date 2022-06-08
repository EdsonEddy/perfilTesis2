from sys import stdin
for i in stdin:
    n=int(i)
    a=0
    b=1
    for j in range(n):
        a,b=b,a+b
    print(a)