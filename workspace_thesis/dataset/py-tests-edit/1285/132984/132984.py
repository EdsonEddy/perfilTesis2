from sys import stdin
for l in stdin:
    n = int(l)
    c1 , cp , b = 0,0,0
    while n > 0:
        if b == 0:
            c1+=n%10
            b = 1
        else:
            cp+=n%10
            b = 0
        n//=10
    if c1==cp:
        print("SI")
    else:
        print("NO")
