while 1>0:
    n,x=map(int,input().split())
    a,b=0,1
    c,d,e=-1,0,2
    s=0
    l=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]
    for i in range(1,n+1,1):
        g=c+d+e
        f=g*(x**l[i-1])
        if i%2==0:
            h=f/b
            s=s-h
        else:
            k=f/b
            s=s+k
        a,b=b,a+b
        c,d,e=d,e,g
    print("{0:.2f}".format(s))