c=int(input())
for j in range (c):
    n=int(input())
    nn=0
    c=0
    po=1
    while n!=0:
        d=n%10
        n=n//10
        for i in range(1,d+1):
            if d%i==0:
                c=c+1
        if c==2:
            nn=nn+d*po
            po=po*10
        c=0

        
    if nn>0:
        print(nn)
    else:
        nn=-1
        print(nn)