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


n, x = map(int, input().split())
while n!="" \
         "":
    s=0
    for i in range(n):
        s=s+(fib(i+1)/(prim(i+1)*x))
    print("{0:.2f}".format(s))
    n,x=map(int,input().split())