def fib(n):
    a,b=1,0
    for i in range (n):
        a,b=b,a+b
    return b
def pr(n,x):
    t=n-1
    lista=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269]
    p=lista[t]
    d=int(p*x)
    return d
while 2>1:
    dig,x=map(int,input().split())
    s=0
    for n in range(1,dig+1,1):
        e=fib(n)
        j=pr(n,x)
        s=s+e/j
    print("{0:.2f}".format(s))