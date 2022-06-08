import sys
for l in sys.stdin:
    n=int(l)
    s,r,i=0,0,1
    while n!=0:
        if i%2==0:
            a=n%10
            n=n//10
            s=s+a
        else:
            a=n%10
            n=n//10
            r=r+a
        i=i+1
    if r==s:
        print("SI")
    else:
        print("NO")