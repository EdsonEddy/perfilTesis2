from sys import stdin
for line in stdin:
    n=int(line)
    ci,cp,b=0,0,0
    while n>0:
        if b==0:
            ci=ci+n%10
            b=1
        else:
            cp=cp+n%10
            b=0
        n=n//10
    if ci==cp:
        print("SI")
    else:
        print("NO")
