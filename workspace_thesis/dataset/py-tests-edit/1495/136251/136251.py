while True:
    def tribonacci():
        a, b ,c= 1, 3, 6
        li = []
        for i in range(n):
            li.append(a)
            a ,b,c= b,c,c+a+b
        return li
    n,m=map(int,input().split())
    def fibonacci():
        a, b = 1, 1
        li2 = []
        for i in range(n):
            li2.append(a)
            a, b = b, a + b
        return li2
    def primos():
        li3=[]
        p=1
        for i in range(1,n+1):
            cd = 1
            while cd!=2:
                cd=0
                p=p+1
                for a in range(1,p+1):
                    if p%a==0:
                        cd=cd+1
            li3.append(p)
        return li3
    def suma():
        s=0
        sgn=1
        for i in range(n):
            num=(tribonacci()[i])*(m**(primos()[i]))
            dem=fibonacci()[i]
            frac=num/dem
            s=s+(frac*sgn)
            sgn=-1*sgn
        return s
    print ("{0:.2f}".format(suma()))