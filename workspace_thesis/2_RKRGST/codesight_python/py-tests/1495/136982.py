def fib(p):
    a=1
    b=0
    for i in range(p):
        c=a+b
        a,b=b,c
    return c
def prim(p):
    c2=0
    c=0
    while c2!=p:
        c1=0
        for i in range(c):
            if c%(i+1)==0:
                c1+=1
        if(c1==2):
            c2+=1
        c+=1
    return c-1
def trib(p):
    a,b,c=-1,0,2
    for i in range(p):
        d=a+b+c
        a,b,c=b,c,d
    return d
n, x = map(int, input().split())
while n!="" \
         "":
    s=0
    for i in range(n):
        if (i+1)%2==1:
            s=s+((trib(i+1)*(x**prim(i+1)))/fib(i+1))
        else:s=s-((trib(i+1)*(x**prim(i+1)))/fib(i+1))
    print("{0:.2f}".format(s))
    n,x=map(int,input().split())
