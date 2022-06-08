while True:
    def fib(n):
        a, b = 1,1
        li=[]
        for i in range(n):
            li.append(a)
            a, b = b, a + b
        return li
    n,y=map(int,input().split())
    a1=fib(n)
    def primos():
        li2=[]
        p=1
        for i in range(1,n+1):
            cd = 1
            while cd!=2:
                cd=0
                p=p+1
                for a in range(1,p+1):
                    if p%a==0:
                        cd=cd+1
            li2.append(p)
        return li2
    def suma():
        x=y
        s=0
        for i in range(n):
            nume=fib(n)[i]
            deno=primos()[i]*x
            frac=nume/deno
            s=s+frac
        return s
    print ("{0:.2f}".format(suma()))