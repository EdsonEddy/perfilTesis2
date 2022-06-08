from sys import stdin
for a in stdin:
    n,b=int(a),0
    for i in range(1,n+1):
        for j in range(i):
            c=2**i+2**j
            if b!=n-1:
                print(c,end=' ')
            else:
                print(c)
            b=b+1
            if b==n:
                break
        if b==n:
            break
