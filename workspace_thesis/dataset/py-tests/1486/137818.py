n=int(input())
i=1
p=0
im=0
c=1
r=0

while (i<=n):
    if (i%2==0):
        p=p+2
        print (p)
    else:
        im=r
        r=im+c
        print(r)
        c=im
        
        
    i=i+1
