from sys import stdin
for k in stdin:
    n=int(k)
    s=0
    for i in range(1,n+1):
        for j in range(i):
            c=2**i+2**j
            if s!=n-1:
                print(c,end=' ')
            else:
                print(c)
            s=s+1
            if s==n:
                break
        if s==n:

            break