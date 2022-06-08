from sys import stdin
for i in stdin:
    n,y=map(int,i.split())
    p=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    a,b,c=1,3,6
    k,j=1,1
    
    l1=[]
    l=[]
    s=0
    for i in range(n):
        d=a+b+c
        f=a
        a=b
        b=c
        c=d
        h=k
        k,j=j,k+j
    
    
        g=p[i]
        if i%2!=0:
            s = s -((f / h) * y ** g)
        else:
            s = s + ((f / h) * y ** g)
    
    print("{0:.2f}".format(s))
